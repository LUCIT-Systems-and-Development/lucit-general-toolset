#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# File: lucit_general_toolset.py
#
# Project website: https://github.com/LUCIT-Systems-and-Development/lucit_general_toolset
# Documentation: https://lucit-systems-and-development.github.io/lucit_general_toolset
# PyPI: https://pypi.org/project/lucit_general_toolset
#
# Author: LUCIT Systems and Development
#
# Copyright (c) 2022-2022, LUCIT Systems and Development (https://www.lucit.tech) and Oliver Zehentleitner
# All rights reserved.
#
# Permission is hereby granted, free of charge, to any person obtaining a
# copy of this software and associated documentation files (the
# "Software"), to deal in the Software without restriction, including
# without limitation the rights to use, copy, modify, merge, publish, dis-
# tribute, sublicense, and/or sell copies of the Software, and to permit
# persons to whom the Software is furnished to do so, subject to the fol-
# lowing conditions:
#
# The above copyright notice and this permission notice shall be included
# in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS
# OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABIL-
# ITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT
# SHALL THE AUTHOR BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY,
# WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS
# IN THE SOFTWARE.

from configparser import ConfigParser, ExtendedInterpolation
import datetime
import logging
import math
import os
import requests


class LucitGeneralToolset:
    @staticmethod
    def get_config(root_path=""):
        config_file_name = ".lucit_trading_tools.ini"
        path_to_home = f"{os.path.expanduser('~')}/{config_file_name}"
        if os.path.isfile(path_to_home):
            config_file = path_to_home
        else:
            config_file = f"{root_path}/config/{config_file_name}"
        logging.info(f"Loading configuration file {config_file}")
        cfg = ConfigParser(interpolation=ExtendedInterpolation())
        cfg.read(config_file)
        return cfg

    @staticmethod
    def send_telegram_message(bot_message: str = None,
                              telegram_bot_token: str = None,
                              telegram_send_to: str = None) -> bool:
        """
        Sending message via Telegram.

        :param bot_message: Message to send.
        :type bot_message: str
        :param telegram_bot_token: Token to use for authentication against Telegram API. (Add @botFather and and write /newbot)
        :type telegram_bot_token: strNotifications
        :param telegram_send_to: Telegram chat_id (Add contact @chat_id_echo_bot and click /start!)
        :type telegram_send_to: str
        :return: bool
        """
        date = datetime.datetime.now().strftime("%H:%M:%S")
        msg = bot_message.replace("%25", "%")
        logging.info(" ".join([msg, "at", date]))
        request_url = f"https://api.telegram.org/bot{telegram_bot_token}/sendMessage?chat_id=" \
                      f"{telegram_send_to}&parse_mode=HTML&text={bot_message}"
        response = requests.get(request_url)
        logging.info(f"send_telegram_message() response: {response}")
        return True

    @staticmethod
    def round_decimals_down(number: float,
                            decimals: int = 2) -> float:
        """
        Returns a value rounded down to a specific number of decimal places.

        :param number: The decimal number to round down.
        :type number: float
        :param decimals: How many decimals you want to keep.
        :type decimals: int
        :return: float
        """
        if not isinstance(decimals, int):
            raise TypeError("Decimal places must be an integer")
        elif decimals < 0:
            raise ValueError("Decimal places has to be 0 or more")
        elif decimals == 0:
            return math.floor(number)
        else:
            factor = 10 ** decimals
            return math.floor(number * factor) / factor

