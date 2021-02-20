#!/usr/bin/env python
# -*- coding: utf-8 -*-

from runner.koan import *

class AboutStringManipulation(Koan):

    def test_use_format_to_interpolate_variables(self):
        value1 = 'one'
        value2 = 2
        # Replaces 0 and 1 with value1, and value2's value.
        string = "The values are {0} and {1}".format(value1, value2)
        self.assertEqual("The values are one and 2", string)

    def test_formatted_values_can_be_shown_in_any_order_or_be_repeated(self):
        value1 = 'doh'
        value2 = 'DOH'
        # Does this regardless of order.
        string = "The values are {1}, {0}, {0} and {1}!".format(value1, value2)
        self.assertEqual("The values are DOH, doh, doh and DOH!", string)

    def test_any_python_expression_may_be_interpolated(self):
        import math # import a standard python module with math functions

        decimal_places = 4
        # Finds the square root of 5, and formats it to 4 decimal places.
        string = "The square root of 5 is {0:.{1}f}".format(math.sqrt(5),
            decimal_places)
        self.assertEqual("The square root of 5 is 2.2361", string)

    def test_you_can_get_a_substring_from_a_string(self):
        string = "Bacon, lettuce and tomato"
        # Returns the letters between 7 and not including 10.
        self.assertEqual("let", string[7:10])

    def test_you_can_get_a_single_character_from_a_string(self):
        string = "Bacon, lettuce and tomato"
        # Gives the letter at index 1.
        self.assertEqual("a", string[1])

    def test_single_characters_can_be_represented_by_integers(self):
        # a is the ordinal number 97. B is the ordinal number 98.
        self.assertEqual(97, ord('a'))
        self.assertEqual(True, ord('b') == (ord('a') + 1))

    def test_strings_can_be_split(self):
        string = "Sausage Egg Cheese"
        words = string.split()
        # Split splits a string into a list.
        self.assertListEqual(["Sausage", "Egg", "Cheese"], words)

    def test_strings_can_be_split_with_different_patterns(self):
        import re #import python regular expression library

        string = "the,rain;in,spain"
        pattern = re.compile(',|;')

        words = pattern.split(string)
        # Removes everything with those scharacters, and splits the string into a list.
        self.assertListEqual(["the", "rain", "in", "spain"], words)

        # Pattern is a Python regular expression pattern which matches ',' or ';'

    def test_raw_strings_do_not_interpret_escape_characters(self):
        string = r'\n'
        # Raw strings ignore escape characters for things like paths on windows machines.
        self.assertNotEqual('\n', string)
        self.assertEqual('\\n', string)
        self.assertEqual(2, len(string))

        # Useful in regular expressions, file paths, URLs, etc.

    def test_strings_can_be_joined(self):
        words = ["Now", "is", "the", "time"]
        # Joins the list into a single string on spaces.
        self.assertEqual('Now is the time', ' '.join(words))

    def test_strings_can_change_case(self):
        # Capitalizes the first letter.
        self.assertEqual("Guido", 'guido'.capitalize())
        # Capitalizes all letters.
        self.assertEqual("GUIDO", 'guido'.upper())
        # Removes the capital letters.
        self.assertEqual("timbot", 'TimBot'.lower())
        # Every word's first character is capitalized.
        self.assertEqual("Guido Van Rossum", 'guido van rossum'.title())
        # Reverses what is capitalized.
        self.assertEqual("tOtAlLy AwEsOmE", 'ToTaLlY aWeSoMe'.swapcase())
