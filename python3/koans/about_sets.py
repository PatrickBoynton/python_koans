#!/usr/bin/env python
# -*- coding: utf-8 -*-

from runner.koan import *

class AboutSets(Koan):
    def test_sets_make_keep_lists_unique(self):
        highlanders = ['MacLeod', 'Ramirez', 'MacLeod', 'Matunas', 'MacLeod', 'Malcolm', 'MacLeod']

        there_can_only_be_only_one = set(highlanders)
        # There can be only one unique item in Python sets.
        self.assertEqual({'MacLeod', 'Ramirez', 'Matunas', 'Malcolm'}, there_can_only_be_only_one)

    def test_empty_sets_have_different_syntax_to_populated_sets(self):
        # You can create a literal set, or use the method
        # There is no empty literal set in python since it is the same as the
        # dict.
        self.assertEqual({1, 2, 3}, {1, 2, 3})
        self.assertEqual(set(), set())

    def test_dictionaries_and_sets_use_same_curly_braces(self):
        # Note: Literal sets using braces were introduced in python 3.
        #       They were also backported to python 2.7.
        # This makes it clear that dicts, and sets are different.
        self.assertEqual(set, {1, 2, 3}.__class__)
        self.assertEqual(dict, {'one': 1, 'two': 2}.__class__)

        self.assertEqual(dict, {}.__class__)

    def test_creating_sets_using_strings(self):
        # If you do a set with the set method it splits the string into chars.
        self.assertEqual({'12345'}, {'12345'})
        self.assertEqual({'1', '2', '3', '4', '5'}, set('12345'))
    # sorted returns a sorted list of whatever you pass in, in this case a set of chars.
    def test_convert_the_set_into_a_list_to_sort_it(self):
        self.assertEqual(['1', '2', '3', '4', '5'], sorted(set('12345')))

    # ------------------------------------------------------------------

    def test_set_have_arithmetic_operators(self):
        scotsmen = {'MacLeod', 'Wallace', 'Willie'}
        warriors = {'MacLeod', 'Wallace', 'Leonidas'}

        # Willie is the difference though I'm not sure why Leonidas is not there too.
        self.assertEqual({'Willie'}, scotsmen - warriors)
        # A union is everything in both sets.
        self.assertEqual({'MacLeod', 'Wallace', 'Willie', 'Leonidas'}, scotsmen | warriors)
        # This returns everything that is the same in both sets.
        self.assertEqual({'Wallace', 'MacLeod'}, scotsmen & warriors)
        # I assume that this returns the difference in both sets.
        self.assertEqual({'Leonidas', 'Willie'}, scotsmen ^ warriors)

    # ------------------------------------------------------------------

    def test_we_can_query_set_membership(self):
        self.assertEqual(True, 127 in {127, 0, 0, 1} )
        self.assertEqual(True, 'cow' not in set('apocalypse now') )

    def test_we_can_compare_subsets(self):
        self.assertEqual(True, set('cake') <= set('cherry cake'))
        self.assertEqual(True, set('cake').issubset(set('cherry cake')) )

        self.assertEqual(False, set('cake') > set('pie'))
