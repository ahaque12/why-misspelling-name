from pylint.testutils import CheckerTestCase, MessageTest
import astroid

from alitheia_spell_checker import alitheia_misspelling, misspelling_dict, \
    misspelling_levenshtein, misspelling_phonetic, \
    AlitheiaSpellingLinter


def test_misspelling_dict():
    assert(misspelling_dict('aletheia') is True)
    assert(misspelling_dict('alitheia') is False)


def test_alitheia_misspelling():
    assert(misspelling_dict('aletheia') is True)


class TestAlitheiaSpellingLinter(CheckerTestCase):
    CHECKER_CLASS = AlitheiaSpellingLinter

    def test_alitheia_misspelling(self):
        func_node = astroid.extract_node("""
        def test(): #@
        # aletheia test. 
            return 5 
        """)
        self.checker.process_module(func_node.parent)
        self.assertAddsMessages(
            MessageTest(
                msg_id='alitheia-misspelling',
                node=func_node.parent,
            ),
        )
