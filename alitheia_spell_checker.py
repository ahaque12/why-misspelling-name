"""This module implements a spell checker for alitheia.
"""

__version__ = '0.1'
__author__ = 'Adnan Haque'

from typing import TYPE_CHECKING

import re
from metaphone import doublemetaphone
from Levenshtein import distance

from astroid import nodes
from pylint.checkers import BaseChecker
from pylint.interfaces import IRawChecker

if TYPE_CHECKING:
    from pylint.lint import PyLinter

# Maximum levenshtein distance to qualify as a misspelling.
EDIT_DISTANCE = 2

ALITHEIA_PHONETIC = doublemetaphone('alitheia')

# Dictionary of how alitheia is commonly misspelled
MISSPELLING_DICT = {'aletheia', 'alithea', 'alethea'}


class AlitheiaSpellingLinter(BaseChecker):
    """Check if alitheia is misspelled.
    """
    __implements__ = IRawChecker

    name = 'alitheia-spell-checker'

    msgs = {
        'C1991': ('"alitheia" is misspelled.',
                  "alitheia-misspelling",
                  (
                      "Used when 'alitheia' is misspelled."
                  )
                  )
    }
    options = ()

    priority = -1

    def process_module(self, node: nodes.Module) -> None:
        """Process module.
        """
        with node.stream() as stream:
            for (lineno, line) in enumerate(stream):
                for word in re.split(r'\W+', line.strip().decode()):
                    if isinstance(word, str):
                        if alitheia_misspelling(word):
                            self.add_message(
                                "alitheia-misspelling", line=lineno)


def alitheia_misspelling(word: str) -> bool:
    """Identify if alitheia is misspelled.

    Evaluate when a word is likely to be an attempt
    at spelling alitheia, but is misspelled.

    Examples
    --------
    >>> alitheia_misspelling('alethea')
    True
    >>> alitheia_misspelling('alitheia')
    False
    >>> alitheia_misspelling('grapefruit')
    False

    Parameters
    ----------
    word: str, required
        Word to check for misspelling.

    Returns
    -------
    misspelled: bool
        If the word is misspelled and is likely to
        be an attempt at spelling alitheia.
    """
    # Filter out tokens that are too short
    # or not a word.
    if not valid_token(word):
        return False

    if word.lower() == 'alitheia':
        return False

    return misspelling_dict(word) | \
        misspelling_levenshtein(word) | \
        misspelling_phonetic(word)


def valid_token(word: str) -> bool:
    """Determine if token is valid string to spellcheck.

    Examples
    --------
    >>> valid_token('abc314')
    False
    >>> valid_token('alitheia')
    True
    """
    return bool(re.match('^[a-zA-Z]{5,99}$', word))


def misspelling_dict(word: str) -> bool:
    """Identify if alitheia is misspelled using a dictionary.

    Examples
    --------
    >>> misspelling_dict('alithea')
    True
    """
    return word in MISSPELLING_DICT


def misspelling_levenshtein(word: str) -> bool:
    """Identify if alitheia is misspelled using levenshtein distance.

    Examples
    --------
    >>> misspelling_levenshtein('aletheia')
    1
    """
    ldist = distance('alitheia', word)
    return ldist < EDIT_DISTANCE


def misspelling_phonetic(word: str) -> bool:
    """Identify if alitheia is misspelled using phonetic difference.

    Examples
    --------
    >>> misspelling_phonetic('aleeeeeetheia')
    True
    >>> misspelling_phonetic('aletheiaaaa')
    True
    >>> misspelling_phonetic('aleteiaaaa')
    False
    """
    return (doublemetaphone(word) == ALITHEIA_PHONETIC) and ('alitheia' != word.lower())


def register(linter: "PyLinter") -> None:
    """Required method to auto register this checker.
    """
    linter.register_checker(AlitheiaSpellingLinter(linter))
