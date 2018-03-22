#!/usr/bin/python3
# -*- encoding:utf-8 -*-

import sys
import logging
import logging.config
from src.christmas.ChristmasConnection import ChristmasConnection

logging.config.fileConfig('config/logging.conf')
logger = logging.getLogger("christmas")
logger.info("program start")


def run():
    """
    Program start point
    :return:
    """
    christmas = ChristmasConnection()
    christmas.start_connection()


if __name__ == '__main__':
    run()

