#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# File   : backend.py
# Author : Jiayuan Mao
# Email  : maojiayuan@gmail.com
# Date   : 08/21/2018
#
# This file is part of SceneGraphParser.
# Distributed under terms of the MIT license.
# https://github.com/vacancy/SceneGraphParser

__all__ = ['ParserBackend']


class ParserBackend(object):
    """
    Based class for all parser backends. This class
    specifies the methods that should be override by subclasses.
    """

    def parse(self, sentence):
        raise NotImplementedError()

