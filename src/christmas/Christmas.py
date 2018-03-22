#!/usr/bin/python3
# -*- encoding:utf-8 -*-

import logging

logger = logging.getLogger("christmas")


class Christmas:
    logger = logging.getLogger("christmas")
    """
    This is a class to print christmas pictures
    """

    def __init__(self):
        pass

    def print_tree(self, height):
        """
        print a christmas tree using "*"
        :param height: the height of the tree. If it's a float, it will be rounded to the nearest integer
        :return:
        """
        if type(height) != int:
            self.logger.error("input is not an integer")
            return
        result_pattern = ""
        if height >= 0:
            line_length = (height * 2) - 1
            centre = line_length // 2
            for level in range(height):
                result_pattern += self.__print_line_pattern("*", [centre], level + 1, line_length) + "\n"
            print(result_pattern)
            return result_pattern
        else:
            print("height cannot be negative")

    def print_x(self, height):
        """
        print a shape of X using "*"
        :param height: the height of the X. If it's a float, it will be rounded to the nearest integer
        :return:
        """
        if type(height) != int:
            self.logger.error("input is not an integer")
            return
        if height >= 0:
            result_pattern = ""
            for level in range(height):
                centres = set()
                centres.add(level)
                centres.add((height - 1) - level)
                result_pattern += self.__print_line_pattern("*", list(centres), 1, height) + "\n"
            print(result_pattern)
            return result_pattern


    def __print_line_pattern(self, pattern, centre_list, extend_length, total_length):
        """
        This method is to create one line of pattern
        :param (str) pattern: the pattern will be print
        :param (Set<int>) centre_list: a list of the centres of the pattern appearance in this line
        :param (int) extend_length: the length will be extended from each centre
        :param (int) total_length: the length of the line
        :return: (str) the line
        """
        line = [" "] * total_length
        pattern_index_list = set()
        for pos in centre_list:
            for distance in range(extend_length):
                pattern_index_list.add(pos - distance)
                pattern_index_list.add(pos + distance)
        for pos in pattern_index_list:
            line[pos] = pattern

        return "".join(line)


if __name__ == "__main__":
    test = Christmas()

    test.print_x(5)
    test.print_tree(None)
