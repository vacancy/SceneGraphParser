#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# File   : spacy_parser.py
# Author : Jiayuan Mao
# Email  : maojiayuan@gmail.com
# Date   : 08/21/2018
#
# This file is part of SceneGraphParser.
# Distributed under terms of the MIT license.
# https://github.com/vacancy/SceneGraphParser

from sng_parser.parser import Parser

__all__ = ['SpacyParser']


@Parser.register_backend
class SpacyParser(object):
    """
    Scene graph parser based on spaCy.
    """

    __identifier__ = 'spacy'

    def __init__(self, model='en'):
        """
        Args:
            model (str): a spec for the spaCy model. (default: en). Please refer to the
            official website of spaCy for a complete list of the available models.
            This option is useful if you are dealing with languages other than English.
        """

        self.model = model

        try:
            import spacy
        except ImportError as e:
            raise ImportError('Spacy backend requires the spaCy library. Install spaCy via pip first.') from e

        try:
            self.nlp = spacy.load(model)
        except OSError as e:
            raise ImportError('Unable to load the English model. Run `python -m spacy download en` first.') from e

    def parse(self, sentence):
        """
        The spaCy-based parser parse the sentence into scene graphs based on the dependency parsing
        of the sentence by spaCy.

        All entities (nodes) of the graph come from the noun chunks in the sentence. And the dependencies
        between noun chunks are used for determining the relations among these entities.

        The parsing is performed in three steps:
        
            1. find all the noun chunks as the entities, and resolve the modifiers on them.
            2. determine the subject of verbs (including nsubj, acl and pobjpass). Please refer to the comments
            in the code for better explanation.
            3. determine all the relations among entities.
        """
        doc = self.nlp(sentence)

        # Step 1: determine the entities.
        entities = list()
        for entity in doc.noun_chunks:
            ent = dict(
                span=entity.text,
                lemma_span=entity.lemma_,
                head=entity.root.text,
                lemma_head=entity.root.lemma_,
                modifiers=[]
            )

            for x in entity.root.children:
                # TODO(Jiayuan Mao @ 08/21): try to determine the number.
                if x.dep_ == 'det':
                    ent['modifiers'].append({'dep': x.dep_, 'span': x.text, 'lemma_span': x.lemma_})
                elif x.dep_ == 'nummod':
                    ent['modifiers'].append({'dep': x.dep_, 'span': x.text, 'lemma_span': x.lemma_})
                elif x.dep_ == 'amod':
                    ent['modifiers'].append({'dep': x.dep_, 'span': x.text, 'lemma_span': x.lemma_})

            entities.append(ent)

        # Step 2: determine the subject of the verbs.
        # To handle the situation where multiple nouns may be the same word,
        # the tokens are represented by their position in the sentence instead of their text.
        relation_subj = dict()
        for token in doc:
            # E.g., A [woman] is [playing] the piano. 
            if token.dep_ == 'nsubj':
                relation_subj[token.head.i] = token.i
            # E.g., A [woman] [playing] the piano...
            elif token.dep_ == 'acl':
                relation_subj[token.i] = token.head.i
            # E.g., The piano is [played] by a [woman].
            elif token.dep_ == 'pobj' and token.head.dep_ == 'agent' and token.head.head.pos_ == 'VERB':
                relation_subj[token.head.head.i] = token.i

        # Step 3: determine the relations.
        relations = list()
        for entity in doc.noun_chunks:
            # Again, the subjects and the objects are represented by their position.
            relation = None

            # E.g., A woman is playing the piano. 
            if entity.root.dep_ == 'dobj' and entity.root.head.i in relation_subj:
                relation = {
                    'subj': relation_subj[entity.root.head.i],
                    'obj': entity.root.i,
                    'rel': entity.root.head.text
                }
            elif entity.root.dep_ == 'pobj':
                # E.g., The piano is played [by] a [woman].
                if entity.root.head.dep_ == 'agent':
                    pass
                # E.g., A [piano] in the [room].
                elif entity.root.head.head.pos_ == 'NOUN':
                    relation = {
                        'subj': entity.root.head.head.i,
                        'obj': entity.root.i,
                        'rel': entity.root.head.text
                    }
                # E.g., A [woman] is playing the piano in the [room].
                # Note that room.head.head == playing.
                elif entity.root.head.head.pos_ == 'VERB' and entity.root.head.head.i in relation_subj:
                    relation = {
                        'subj': relation_subj[entity.root.head.head.i],
                        'obj': entity.root.i,
                        'rel': entity.root.head.text
                    }
            # E.g., The [piano] is played by a [woman]
            elif entity.root.dep_ == 'nsubjpass' and entity.root.head.i in relation_subj:
                # Here, we reverse the passive phrase. I.e., subjpass -> obj and objpass -> subj.
                relation = {
                    'subj': relation_subj[entity.root.head.i],
                    'obj': entity.root.i,
                    'rel': entity.root.head.text
                }

            if relation is not None:
                # Use a helper function to map the subj/obj represented by the position
                # back to one of the entity nodes.
                relation['subj'] = self.__locate_noun(doc.noun_chunks, relation['subj'])
                relation['obj'] = self.__locate_noun(doc.noun_chunks, relation['obj'])
                if relation['subj'] != None and relation['obj'] != None:
                    relations.append(relation)
        
        return {'entities': entities, 'relations': relations}

    @staticmethod
    def __locate_noun(chunks, i):
        for j, c in enumerate(chunks):
            if c.start <= i < c.end:
                return j
        return None

