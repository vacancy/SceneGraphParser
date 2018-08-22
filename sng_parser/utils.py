#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# File   : utils.py
# Author : Jiayuan Mao
# Email  : maojiayuan@gmail.com
# Date   : 08/21/2018
#
# This file is part of SceneGraphParser.
# Distributed under terms of the MIT license.
# https://github.com/vacancy/SceneGraphParser

import functools
import tabulate


__all__ = ['tprint']


def tprint(graph, file=None, show_entities=True, show_relations=True):
    """
    Print a scene graph as a table.
    The printed strings contains only essential information about the parsed scene graph.
    """

    _print = functools.partial(print, file=file)

    if show_entities:
        _print('Entities:')

        entities_data = [
            [e['head'].lower(), e['span'].lower(), ','.join([ x['span'].lower() for x in e['modifiers'] ])]
            for e in graph['entities']
        ]
        _print(tabulate.tabulate(entities_data, headers=['Head', 'Span', 'Modifiers'], tablefmt=_tabulate_format))

    if show_relations:
        _print('Relations:')

        entities = graph['entities']
        relations_data = [
            [
                entities[rel['subject']]['head'].lower(),
                rel['relation'].lower(),
                entities[rel['object']]['head'].lower()
            ]
            for rel in graph['relations']
        ]
        _print(tabulate.tabulate(relations_data, headers=['Subject', 'Relation', 'Object'], tablefmt=_tabulate_format))


_tabulate_format = tabulate.TableFormat(
        lineabove=tabulate.Line("+", "-", "+", "+"),
        linebelowheader=tabulate.Line("|", "-", "+", "|"),
        linebetweenrows=None,
        linebelow=tabulate.Line("+", "-", "+", "+"),
        headerrow=tabulate.DataRow("|", "|", "|"),
        datarow=tabulate.DataRow("|", "|", "|"),
        padding=1, with_header_hide=None
)
