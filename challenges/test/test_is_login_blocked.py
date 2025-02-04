#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
A module to test the function is_login_blocked
"""

import unittest
from ..is_login_blocked import is_login_blocked

class TestIsLoginBlocked(unittest.TestCase):
    """"""

    def test_valid_credentials_and_trusted_device(self):
        """it should return False, not blocked"""
        self.assertEqual(is_login_blocked(True, True), False)

    def test_invalid_credentials_and_untrusted_device(self):
        """it should return True, blocked"""
        self.assertEqual(is_login_blocked(False, False), True)

    def test_valid_credentials_and_untrusted_device(self):
        """it should return False, not blocked"""
        self.assertEqual(is_login_blocked(True, False), False)

    def test_invalid_credentials_and_trusted_device(self):
        """it should return True, blocked"""
        self.assertEqual(is_login_blocked(False, True), True)
