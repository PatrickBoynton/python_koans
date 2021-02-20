#!/usr/bin/env python
# -*- coding: utf-8 -*-

from runner.koan import *


class AboutStrings(Koan):

    def test_double_quoted_strings_are_strings(self):
        string = "Hello, world."
        # self.assertEqual(__, isinstance(string, str))
        # Returns true, because string and str are the same type.
        self.assertEqual(True, isinstance(string, str))

    def test_single_quoted_strings_are_also_strings(self):
        string = 'Goodbye, world.'
        # Again, returns true, because single quotes are the same as str.
        self.assertEqual(True, isinstance(string, str))

    def test_triple_quote_strings_are_also_strings(self):
        string = """Howdy, world!"""
        # Triple double quotes are str as well.
        self.assertEqual(True, isinstance(string, str))

    def test_triple_single_quotes_work_too(self):
        # Triple single quotes are str.
        string = '''Bonjour tout le monde!'''
        self.assertEqual(True, isinstance(string, str))

    def test_raw_strings_are_also_strings(self):
        string = r"Konnichi wa, world!"
        # Raw strings are still str.
        self.assertEqual(True, isinstance(string, str))

    def test_use_single_quotes_to_create_string_with_double_quotes(self):
        string = 'He said, "Go Away."'
        # You can use single quotes to create double quotes.
        self.assertEqual('He said, "Go Away."', string)

    def test_use_double_quotes_to_create_strings_with_single_quotes(self):
        string = "Don't"
        # You can use this to avoid escape
        # characters so that it doesn't look so messy.
        self.assertEqual("Don't", string)

    def test_use_backslash_for_escaping_quotes_in_strings(self):
        a = "He said, \"Don't\""
        b = 'He said, "Don\'t"'
        # self.assertEqual(__, (a == b))
        # These two are equal because they are essentially strings.
        self.assertEqual(True, (a == b))

    def test_use_backslash_at_the_end_of_a_line_to_continue_onto_the_next_line(
            self):
        string = "It was the best of times,\n\
It was the worst of times."
        # The escape characters don't count.
        self.assertEqual(52, len(string))

    def test_triple_quoted_strings_can_span_lines(self):
        string = """
Howdy,
world!
"""
        # self.assertEqual(__, len(string))
        # I think the extra lines are counted as characters.
        self.assertEqual(15, len(string))

    def test_triple_quoted_strings_need_less_escaping(self):
        a = "Hello \"world\"."
        b = """Hello "world"."""
        # self.assertEqual(__, (a == b))
        # Escaped quotes are equal to actual quotes.
        self.assertEqual(True, (a == b))

    def test_escaping_quotes_at_the_end_of_triple_quoted_string(self):
        string = """Hello "world\""""
        # self.assertEqual(__, string)
        # The above is the same thing as having a double inside of triple quotes.
        self.assertEqual('Hello "world"', string)

    def test_plus_concatenates_strings(self):
        string = "Hello, " + "world"
        # self.assertEqual(__, string)
        # Concatenated double str are the same as single str not.
        self.assertEqual('Hello, world', string)

    def test_adjacent_strings_are_concatenated_automatically(self):
        string = "Hello" ", " "world"
        # self.assertEqual(__, string)
        # Strings are concatenated automatically, no need for the + operator.
        self.assertEqual('Hello, world', string)

    def test_plus_will_not_modify_original_strings(self):
        hi = "Hello, "
        there = "world"
        string = hi + there
        # self.assertEqual(__, hi)
        # self.assertEqual(__, there)
        # Doing anything with a string returns a modified copy.
        self.assertEqual(hi, hi)
        self.assertEqual(there, there)

    def test_plus_equals_will_append_to_end_of_string(self):
        hi = "Hello, "
        there = "world"
        hi += there
        # self.assertEqual(__, hi)
        # Plus equals works to concatenate strings.
        self.assertEqual("Hello, world", hi)

    def test_plus_equals_also_leaves_original_string_unmodified(self):
        original = "Hello, "
        hi = original
        there = "world"
        hi += there
        # self.assertEqual(__, original)
        # Modifying strings always returns a new copy.
        self.assertEqual("Hello, ", original)

    def test_most_strings_interpret_escape_characters(self):
        string = "\n"
        self.assertEqual('\n', string)
        self.assertEqual("""\n""", string)
        # self.assertEqual(__, len(string))
        # All characters, including escape characters are
        # apparently counted in the length of strings.
        self.assertEqual(1, len(string))
