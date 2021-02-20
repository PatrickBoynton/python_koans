#!/usr/bin/env python
# -*- coding: utf-8 -*-

#
# Based on AboutArrays in the Ruby Koans
#

from runner.koan import *

class AboutLists(Koan):
    def test_creating_lists(self):
        empty_list = list()
        self.assertEqual(list, type(empty_list))
        self.assertEqual(0, len(empty_list))

    def test_list_literals(self):
        # Empty [] are the same as list()
        nums = list()
        self.assertEqual([], nums)
        # slicing with this syntax just gives one, because it's the only element.
        nums[0:] = [1]
        self.assertEqual([1], nums)
        # Slicing here gives out up to two.
        nums[1:] = [2]
        self.assertListEqual([1, 2], nums)

        # Appending does the same thing as just adding a number to the end of a list.
        nums.append(333)
        self.assertListEqual([1, 2, 333], nums)

    def test_accessing_list_elements(self):
        noms = ['peanut', 'butter', 'and', 'jelly']

        # You can access lists by slicing an index.
        # These are what this particular list returns.
        self.assertEqual('peanut', noms[0])
        self.assertEqual('jelly', noms[3])
        self.assertEqual('jelly', noms[-1])
        self.assertEqual('butter', noms[-3])

    def test_slicing_lists(self):
        noms = ['peanut', 'butter', 'and', 'jelly']
        # Returns just the first element in the list.
        self.assertEqual(['peanut'], noms[0:1])
        # Returns the first two elements in the list.
        self.assertEqual(['peanut', 'butter'], noms[0:2])
        # Returns nothing because it starts at two, then ends at two.
        self.assertEqual([], noms[2:2])
        # Just returns the end of the list when you slice too many.
        self.assertEqual(['and', 'jelly'], noms[2:20])
        self.assertEqual([], noms[4:0])
        # Returns nothing because there is not 4 elements of this list.
        self.assertEqual([], noms[4:100])
        # Same answer here There are not 5 elements in this list.
        self.assertEqual([], noms[5:0])

    def test_slicing_to_the_edge(self):
        noms = ['peanut', 'butter', 'and', 'jelly']
        # Slices up to the end of the list from index 2.
        self.assertEqual(['and', 'jelly'], noms[2:])
        # Slices from the beginning up to index 2.
        self.assertEqual(['peanut', 'butter'], noms[:2])

    def test_lists_and_ranges(self):
        # range is indeed a type of range.
        self.assertEqual(range, type(range(5)))
        # a list of 0-4 is not the same thing as a range of 1-6
        # It wouldn't be if it were comparing lists because it's asking for
        # different numbers.
        self.assertNotEqual([0, 1, 2, 3, 4], range(1,6))
        # This converts the range into a list.
        self.assertEqual([0, 1, 2, 3, 4], list(range(5)))
        # Same here, it converts the list into a range.
        self.assertEqual([5, 6, 7, 8], list(range(5, 9)))

    def test_ranges_with_steps(self):
        #  This steps backwards between 5 and 3, but not including 3.
        self.assertEqual([5, 4], list(range(5, 3, -1)))
        #  This steps forward with a step of two between 0 and 8 non inclusie.
        self.assertEqual([0, 2, 4, 6], list(range(0, 8, 2)))
        # This steps forward with a step of 3, between 1 and 8, non inclusive
        self.assertEqual([1, 4, 7], list(range(1, 8, 3)))
        # Range never includes the last element of what you want.
        self.assertEqual([5, 1, -3], list(range(5, -7, -4)))
        # Both of these return a list stepped  4, going backwards.
        self.assertEqual([5, 1, -3, -7], list(range(5, -8, -4)))

    def test_insertions(self):
        knight = ['you', 'shall', 'pass']
        knight.insert(2, 'not')
        # Inserting adds not at index two.
        self.assertEqual(knight, knight)
        # Inserting adds Arthur at index 0.
        knight.insert(0, 'Arthur')
        self.assertEqual(knight, knight)

    def test_popping_lists(self):
        stack = [10, 20, 30, 40]
        stack.append('last')
        # Append, adds to the last part of a list.
        self.assertEqual(stack, stack)

        popped_value = stack.pop()
        self.assertEqual('last', popped_value)
        # Removes last from the list.
        self.assertEqual(stack, stack)

        popped_value = stack.pop(1)
        # Removes 20 from the list
        self.assertEqual(20, popped_value)
        self.assertEqual(stack, stack)

        # Notice that there is a "pop" but no "push" in python?

        # Part of the Python philosophy is that there ideally should be one and
        # only one way of doing anything. A 'push' is the same as an 'append'.

        # To learn more about this try typing "import this" from the python
        # console... ;)

    def test_making_queues(self):
        queue = [1, 2]
        queue.append('last')

        self.assertEqual(queue, queue)

        # This pops off the first element of a list.
        popped_value = queue.pop(0)
        self.assertEqual(1, popped_value)
        self.assertEqual(queue, queue)

        # Note, popping from the left hand side of a list is
        # inefficient. Use collections.deque instead.

