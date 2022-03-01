#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# File   : demo.py
# Author : Jiayuan Mao
# Email  : maojiayuan@gmail.com
# Date   : 08/22/2018
#
# This file is part of SceneGraphParser.
# Distributed under terms of the MIT license.
# https://github.com/vacancy/SceneGraphParser

"""
A small demo for the scene graph parser.
"""

import sng_parser


def demo(sentence):
    print('Sentence:', sentence)

    # Here we just use the default parser.
    sng_parser.tprint(sng_parser.parse(sentence))

    print()


def main():
    demo('A woman is playing the piano in the room.')
    demo('A woman playing the piano in the room.')
    demo('A piano is played by a woman in the room.')
    demo('A woman is playing the space craft at NASA.')
    demo('A woman is playing with a space craft at NASA.')
    demo('A woman next to a piano.')
    demo('A woman in front of a piano.')
    demo('A woman standing next to a piano.')
    demo('The woman is a pianist.')
    demo('A giraffe grazing a tree in the wildness with other wildlife.')
    demo('Cow standing on sidewalk in city area near shops.')

    print('Input your own sentence. Type q to quit.')
    while True:
        sent = input('> ')
        if sent.strip() == 'q':
            break
        demo(sent)


if __name__ == '__main__':
    main()

