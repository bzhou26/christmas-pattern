#!/usr/bin/python3
# -*- encoding:utf-8 -*-

import io
import sys
import unittest.mock
import logging
from src.christmas.Christmas import Christmas


class TestChristmas(unittest.TestCase):

    def assert_christmas_print(self, method, height, expected_output):
        captured_output = io.StringIO()
        sys.stdout = captured_output
        method(height)
        sys.stdout = sys.__stdout__
        # print(len(captured_output.getvalue()))
        # print(captured_output.getvalue())
        # print(len(expected_output))
        # print(expected_output)
        self.assertEqual(captured_output.getvalue(), expected_output)

    def run(self):
        logging.disable(logging.CRITICAL)
        test = TestChristmas()
        christmas = Christmas()

        """
        test christmas tree
        """

        # test height of 5
        expected_output = "    *    " + "\n" + "   ***   " + "\n" + "  *****  " + "\n" + " ******* " + "\n" + "*********" + "\n\n"
        test.assert_christmas_print(christmas.print_tree, 5, expected_output)

        # test height of 3
        expected_output = "  *  " + "\n" + " *** " + "\n" + "*****" + "\n\n"
        test.assert_christmas_print(christmas.print_tree, 3, expected_output)

        # test invalid float number
        expected_output = ""
        test.assert_christmas_print(christmas.print_tree, 2.5, expected_output)

        # test height 0
        expected_output = "\n"
        test.assert_christmas_print(christmas.print_tree, 0, expected_output)

        # test height 1
        expected_output = "*" + "\n\n"
        test.assert_christmas_print(christmas.print_tree, 1, expected_output)

        # test invalid string
        expected_output = ""
        test.assert_christmas_print(christmas.print_tree, "test", expected_output)

        # test invalid type
        expected_output = ""
        test.assert_christmas_print(christmas.print_tree, [1], expected_output)

        """
        Test shape x
        """
        # test valid odd number
        expected_output = "*   *" + "\n" + " * * " + "\n" + "  *  " + "\n" + " * * " + "\n" + "*   *" + "\n\n"
        test.assert_christmas_print(christmas.print_x, 5, expected_output)

        # test valid even number
        expected_output = "*  *" + "\n" + " ** " + "\n" + " ** " + "\n" + "*  *" + "\n\n"
        test.assert_christmas_print(christmas.print_x, 4, expected_output)

        # test height 1
        expected_output = "*" + "\n\n"
        test.assert_christmas_print(christmas.print_x, 1, expected_output)

        # test height 0
        expected_output = "\n"
        test.assert_christmas_print(christmas.print_x, 0, expected_output)

        # test invalid float number
        expected_output = ""
        test.assert_christmas_print(christmas.print_x, 2.5, expected_output)

        # test invalid string
        expected_output = ""
        test.assert_christmas_print(christmas.print_x, "test", expected_output)

        # test invalid type
        expected_output = ""
        test.assert_christmas_print(christmas.print_x, [1], expected_output)

        logging.disable(logging.NOTSET)


if __name__ == "__main__":
    logging.disable(logging.CRITICAL)
    test = TestChristmas()
    christmas = Christmas()

    """
    test christmas tree
    """

    # test height of 5
    expected_output = "    *    " + "\n" + "   ***   " + "\n" + "  *****  " + "\n" + " ******* " + "\n" + "*********" + "\n\n"
    test.assert_christmas_print(christmas.print_tree, 5, expected_output)

    # test height of 3
    expected_output = "  *  " + "\n" + " *** " + "\n" + "*****" + "\n\n"
    test.assert_christmas_print(christmas.print_tree, 3, expected_output)

    # test invalid float number
    expected_output = ""
    test.assert_christmas_print(christmas.print_tree, 2.5, expected_output)

    # test height 0
    expected_output = "\n"
    test.assert_christmas_print(christmas.print_tree, 0, expected_output)

    # test height 1
    expected_output = "*" + "\n\n"
    test.assert_christmas_print(christmas.print_tree, 1, expected_output)

    # test invalid string
    expected_output = ""
    test.assert_christmas_print(christmas.print_tree, "test", expected_output)

    # test invalid type
    expected_output = ""
    test.assert_christmas_print(christmas.print_tree, [1], expected_output)

    """
    Test shape x
    """
    # test valid odd number
    expected_output = "*   *" + "\n" + " * * " + "\n" + "  *  " + "\n" + " * * " + "\n" + "*   *" + "\n\n"
    test.assert_christmas_print(christmas.print_x, 5, expected_output)

    # test valid even number
    expected_output = "*  *" + "\n" + " ** " + "\n" + " ** " + "\n" + "*  *" + "\n\n"
    test.assert_christmas_print(christmas.print_x, 4, expected_output)

    # test height 1
    expected_output = "*" + "\n\n"
    test.assert_christmas_print(christmas.print_x, 1, expected_output)

    # test height 0
    expected_output = "\n"
    test.assert_christmas_print(christmas.print_x, 0, expected_output)

    # test invalid float number
    expected_output = ""
    test.assert_christmas_print(christmas.print_x, 2.5, expected_output)

    # test invalid string
    expected_output = ""
    test.assert_christmas_print(christmas.print_x, "test", expected_output)

    # test invalid type
    expected_output = ""
    test.assert_christmas_print(christmas.print_x, [1], expected_output)

    logging.disable(logging.NOTSET)