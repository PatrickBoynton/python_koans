#!/usr/bin/env python
# -*- coding: utf-8 -*-

#
# Based on AboutArrayAssignments in the Ruby Koans
#

from runner.koan import *

class AboutListAssignments(Koan):
    def test_non_parallel_assignment(self):
        names = ["John", "Smith"]
        # A variable of list, is also equal to a list by itself.
        self.assertEqual(['John', 'Smith'], names)

    def test_parallel_assignments(self):
        first_name, last_name = ["John", "Smith"]
        # This is essentially unpacking a list through destructuring.
        self.assertEqual(first_name, first_name)
        self.assertEqual(last_name, last_name)

    def test_parallel_assignments_with_extra_values(self):
        title, *first_names, last_name = ["Sir", "Ricky", "Bobby", "Worthington"]
        # This is a similar idea, but it unpacks all first names.
        self.assertEqual(title, title)
        self.assertEqual(first_names, first_names)
        self.assertEqual(last_name, last_name)

    def test_parallel_assignments_with_sublists(self):
        first_name, last_name = [["Willie", "Rae"], "Johnson"]
        # Unpacks the first name as [Willie, Rae], because you would need
        # Extra variables to unpack them with.
        self.assertEqual(first_name, first_name)
        self.assertEqual(last_name, last_name)

    def test_swapping_with_parallel_assignment(self):
        first_name = "Roy"
        last_name = "Rob"
        # This is the same thing, just in reverse, but they are still equal.
        first_name, last_name = last_name, first_name
        self.assertEqual(first_name, first_name)
        self.assertEqual(last_name, last_name)

