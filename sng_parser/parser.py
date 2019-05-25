#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# File   : parser.py
# Author : Jiayuan Mao
# Email  : maojiayuan@gmail.com
# Date   : 08/21/2018
#
# This file is part of SceneGraphParser.
# Distributed under terms of the MIT license.
# https://github.com/vacancy/SceneGraphParser

__all__ = ['Parser', 'get_default_parser', 'parse']


def _load_backends():
    from . import backends


class Parser(object):
    """
    The scene graph parser. To instantiate a scene graph parser,
    you need to specify a backend (default: spacy) and the initialization
    keyword arguments for the backend (optional).

    Once the backend has been specified, you can call parser.parse(sentence)
    to parse a sentence in natural language into a scene graph.
    Note that, the function `parse` also supports extra keyword arguments
    which will be passed to the backend for the parsing.
    To use this feature, you may refer to the implementation of your parser
    backend.

    Example::
    >>> parser = Parser(backend, **init_kwargs)
    >>> graph = parser.parse('A woman is playing the piano,')
    """

    def __init__(self, backend=None, **kwargs):
        _load_backends()

        self.backend = backend
        if self.backend is None:
            self.backend = type(self)._default_backend
        if self.backend not in type(self)._backend_registry:
            raise ValueError('Unknown backend: {}.'.format(self.backend))

        self._init_kwargs = kwargs
        self._inst = type(self)._backend_registry[self.backend](**kwargs)

    @property
    def init_kwargs(self):
        """
        Get the keyward arguments used for initializing the backend.
        """
        return self._init_kwargs

    @property
    def unwrapped(self):
        """
        Get the backend.
        """
        return self._inst

    def parse(self, sentence, **kwargs):
        """
        Parse a sentence into a scene graph.

        Args:
            sentence (str): the input sentence.

        Returns:
            graph (dict): the parsed scene graph. Please refer to the
            README file for the specification of the return value.
        """
        return self.unwrapped.parse(sentence, **kwargs)

    _default_backend = 'spacy'
    _backend_registry = dict()

    @classmethod
    def register_backend(cls, backend):
        """
        Register a class as the backend. The backend should implement a
        method named `parse` having the following signature:
        `parse(sentence, <other_keyward_arguments>)`.

        To register your customized backend as the parser, use this class
        method as a decorator on your class.

        Example::
        >>> @Parser.register_backend
        >>> class CustomizedBackend(Backend):
        >>>     # Your implementation follows...
        >>>     pass
        """
        try:
            cls._backend_registry[backend.__identifier__] = backend
        except Exception as e:
            raise ImportError('Unable to register backend: {}.'.format(backend.__name__)) from e


_default_parser = None


def get_default_parser():
    """
    Get the default parser.

    The default parser is a global one (singleton).
    """
    global _default_parser
    if _default_parser is None:
        _default_parser = Parser()
    return _default_parser


def parse(sentence, **kwargs):
    """
    Parse the sentence using the default parser. This ia an easy-to-use
    feature for those who do not want to configure their own parsers
    and want to use the parser at different places in their codes.

    Please note that the default parser is a singleton. Thus,
    if you are using a stateful parser, you need to be careful about sharing
    this parser everywhere.
    """
    return get_default_parser().parse(sentence, **kwargs)

