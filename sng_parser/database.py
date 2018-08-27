#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# File   : database.py
# Author : Jiayuan Mao
# Email  : maojiayuan@gmail.com
# Date   : 08/23/2018
#
# This file is part of SceneGraphParser.
# Distributed under terms of the MIT license.
# https://github.com/vacancy/SceneGraphParser

import os.path as osp


_caches = dict()


def load_list(filename):
    if filename not in _caches:
        out = set()
        for x in open(osp.join(osp.dirname(__file__), '_data', filename)):
            x = x.strip()
            if len(x) > 0:
                out.add(x)
        _caches[filename] = out
    return _caches[filename]


def is_phrasal_verb(verb):
    return verb in load_list('phrasal-verbs.txt')


def is_phrasal_prep(prep):
    return prep in load_list('phrasal-preps.txt')


def is_scene_noun(noun):
    head = noun.split(' ')[-1]
    s = load_list('scene-nouns.txt') 
    return noun in s or head in s

