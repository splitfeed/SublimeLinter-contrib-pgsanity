#
# linter.py
# Linter for SublimeLinter3, a code checking framework for Sublime Text 3
#
# Written by Niklas
# Copyright (c) 2014 Niklas
#
# License: MIT
#

"""This module exports the Pgsanity plugin class."""

from SublimeLinter.lint import Linter, util


class Pgsanity(Linter):

    """Provides an interface to pgsanity."""

    syntax = ('sql', 'postgresql')
    cmd = 'pgsanity'
    executable = None
    # version_args = '--version'
    # version_re = r'(?P<version>\d+\.\d+\.\d+)'
    # version_requirement = '>= 1.0'
    regex = r'line (?P<line>\d+): ERROR: (?P<message>.+)'
    multiline = False
    line_col_base = (1, 1)
    tempfile_suffix = None
    error_stream = util.STREAM_BOTH
    selectors = {}
    word_re = None
    defaults = {}
    inline_settings = None
    inline_overrides = None
    comment_re = None
