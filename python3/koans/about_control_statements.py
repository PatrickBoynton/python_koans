#!/usr/bin/env python
# -*- coding: utf-8 -*-

from runner.koan import *

class AboutControlStatements(Koan):

    def test_if_then_else_statements(self):
        if True:
            result = 'true value'
        else:
            result = 'false value'
        # It checks if True == True, so true value will be the result.
        self.assertEqual("true value", result)

    def test_if_then_statements(self):
        result = 'default value'
        if True:
            result = 'true value'
        #  Result is overwritten by the new value because True == True.
        self.assertEqual("true value", result)

    def test_if_then_elif_else_statements(self):
        if False:
            result = 'first value'
        elif True:
            result = 'true value'
        else:
            result = 'default value'
        # It's either because True is True, or because strings are True.
        self.assertEqual("true value", result)

    def test_while_statement(self):
        i = 1
        result = 1
        while i <= 10:
            result = result * i
            i += 1
        # This is the result of running this loop.
        self.assertEqual(3628800, result)

    def test_break_statement(self):
        i = 1
        result = 1
        while True:
            if i > 10: break
            result = result * i
            i += 1
        # This is the result of running the while loop.
        self.assertEqual(3628800, result)

    def test_continue_statement(self):
        i = 0
        result = []
        while i < 10:
            i += 1
            if (i % 2) == 0: continue
            result.append(i)
        # The loop appends odd numbers between 1 and 10 to the list.
        self.assertEqual([1, 3, 5, 7, 9], result)

    def test_for_statement(self):
        phrase = ["fish", "and", "chips"]
        result = []
        for item in phrase:
            result.append(item.upper())
        # Capitalizes the items in the list.
        self.assertEqual(["FISH", "AND", "CHIPS"], result)

    def test_for_statement_with_tuples(self):
        round_table = [
            ("Lancelot", "Blue"),
            ("Galahad", "I don't know!"),
            ("Robin", "Blue! I mean Green!"),
            ("Arthur", "Is that an African Swallow or European Swallow?")
        ]
        result = []
        for knight, answer in round_table:
            result.append("Contestant: '" + knight + "'   Answer: '" + answer + "'")
        # The text is what is being checked against, there is only one Robin.
        text = "Contestant: 'Robin'   Answer: 'Blue! I mean Green!'"

        self.assertRegex(result[2], text)

        self.assertNotRegex(result[0], text)
        self.assertNotRegex(result[1], text)
        self.assertNotRegex(result[3], text)
