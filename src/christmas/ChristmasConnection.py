#!/usr/bin/python3
# -*- encoding:utf-8 -*-

import sys
import logging
from .Christmas import Christmas
from tests.TestChristmas import TestChristmas


class ChristmasConnection:
    """
    This is the console based api for accept commands and argument for christmas module
    """
    logger = logging.getLogger("christmas")

    def __init__(self):
        """
        initial supported command list
        """
        self.christmas = Christmas()

        self.commands = {
            "tree": self.tree_cmd,
            "x": self.x_cmd,
            "test": self.test_cmd,
            "quit": self.quit_cmd
        }

        self.argmap = {
            "tree": (1, 'Usage: print a christmas tree'),
            "x": (1, 'Usage: print a christmas X'),
            "test": (0, 'no argument need'),
            "quit": (0, 'no argument need')
        }

    def start_connection(self):
        """
        accept command and arguments
        """
        self.logger.info("Start up successful...")
        self.logger.info("We support [tree height | x height | test | quit]\n\n")
        line = sys.stdin.readline()
        while line:
            # self.logger.debug("[User input]: " + line)
            self.get_cmd(line)
            line = sys.stdin.readline()

    def get_cmd(self, command):
        if len(command.strip(' \r\t')) == 0:
            return

        elements = command.split()
        if not elements:
            return

        command_name = elements[0]
        args = elements[1:]

        if self.arg_error(command_name, len(args)):
            return
        if command_name in self.commands:
            try:
                self.commands[command_name](args)
            except Exception as e:
                self.logger.error("Error executing command {}\n".format(str(e)))
        else:
            self.logger.error("Unknown command: {}\n".format(command_name))

    def arg_error(self, cmd, argnum):
        """
        check if the argument and command are valid or not
        """
        if cmd in self.argmap and self.argmap[cmd][0] > argnum:
            self.logger.error(self.argmap[cmd][1])
            return True
        return False

    def tree_cmd(self, args):
        self.christmas.print_tree(int(args[0]))
        return True

    def x_cmd(self, args):
        self.christmas.print_x(int(args[0]))
        return True

    def test_cmd(self, _):
        test_christmas = TestChristmas()
        test_christmas.run()
        self.logger.info("All unit test done")
        return True

    def quit_cmd(self, _):
        self.logger.info("exit program successfully")
        exit(0)
