# SceneGraphParser

SceneGraphParser (`sng_parser`) is a python toolkit for parsing sentences (in natural language) into scene graphs (as symbolic representation) based on the dependency parsing. This project is inspired by the [Stanford Scene Graph Parser](https://nlp.stanford.edu/software/scenegraph-parser.shtml).

Different from the Stanford version, this parser is written purely by Python. It has an easy-to-use user interface and an easy-to-configure design.  It parses sentences into graphs where the nodes are nouns (with modifiers such as determinants or adjectives) and the edges are relations between nouns. Please see the example section for details.

> **Highlight: This project is still being developed. ALL APIs are subject to ANY change.**

> **Note**: As you may notice, the parsing is done by a set of human-written rules on the parsing tree. Thus, we need help from everyone on collecting failure/corner cases of the current program.
> Any kind of reports or help should be more than welcome.

## Example

The easiest way to use this tool is by calling the `parse` function. In design, `sng_parser` supports different backends. Currently, we only support the spaCy backend. To use it, you must install spaCy yourself by:

```bash
pip install spacy
python -m spacy download en  # to use the parser for English
```

```python
>>> import sng_parser
>>> graph = sng_parser.parse('A woman is playing the piano in the room.')
```
```python
>>> from pprint import pprint
>>> pprint(graph)
```
```
{'entities': [{'head': 'woman',
               'lemma_head': 'woman',
               'lemma_span': 'a woman',
               'modifiers': [{'dep': 'det', 'lemma_span': 'a', 'span': 'A'}],
               'span': 'A woman'},
              {'head': 'piano',
               'lemma_head': 'piano',
               'lemma_span': 'the piano',
               'modifiers': [{'dep': 'det',
                              'lemma_span': 'the',
                              'span': 'the'}],
               'span': 'the piano'},
              {'head': 'room',
               'lemma_head': 'room',
               'lemma_span': 'the room',
               'modifiers': [{'dep': 'det',
                              'lemma_span': 'the',
                              'span': 'the'}],
               'span': 'the room'}],
 'relations': [{'object': 1, 'relation': 'playing', 'subject': 0},
               {'object': 2, 'relation': 'in', 'subject': 0}]}
```
```python
>>> sng_parser.tprint(graph)  # we provide a tabular visualization of the graph.
```
```
Entities:
+--------+-----------+-------------+
| Head   | Span      | Modifiers   |
|--------+-----------+-------------|
| woman  | a woman   | a           |
| piano  | the piano | the         |
| room   | the room  | the         |
+--------+-----------+-------------+
Relations:
+-----------+------------+----------+
| Subject   | Relation   | Object   |
|-----------+------------+----------|
| woman     | playing    | piano    |
| woman     | in         | room     |
+-----------+------------+----------+
```

Alternatively, you can configure your own parser:

```python
>>> import sng_parser
>>> parser = sng_parser.Parser('spacy', model='en')  # the positional argument specifies the backend, and the keyward arguments are for the backend initialization.
>>> graph = parser.parse('A woman is playing the piano in the room.')
```

## Specification of the graph
We use the pure pythonic `dict` and `list` to represent a graph. Although this flexibility may bring some unwanted issues, we prefer this representation because:
  1. currently, the tool is still being developed, these APIs are subject to change.
  2. this makes the tool easy to be integrated into any python-based projects. You don't need to care about pickling/unpickling the results. Use it anywhere in your code!

The generated scene graphs match the following spec:

```python
{
  'entities': [  # a list of entities
    {
      'span': "the full span of a noun phrase",
      'lemma_span': "the lemmatized version of the span",
      'head': "the head noun",
      'lemma_head': "the lemmatized version of the head noun",
      'modifiers': [
        {
          'dep': "the dependency type",
          'span': "the span of the modifier",
          'lemma_span': "the lemmatized version of the span"
        },
        # other modifiers...
      ]
    },
    # other entities...
  ],
  
  'relations': [  # a list of relations
    # the subject and object fields are sometimes called "head" and "tail" in relation extraction papers.
    {
      'subject': "the entity id of the subject",
      'object': "the entity id of the object",
      'relation': "the relation"
    }
    # other relations...
  ]
}
```
