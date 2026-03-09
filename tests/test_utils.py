"""
File : tests/test_utils.py
Description : Test to check if the function for the verification of the password is working
Autor : Alex Kamano
Version : 1.0
Project : PyPortal
Date : 9 Mars 2026
"""

from core.utils import is_password_strong

class TestIsPasswordStrong:
    def test_password_too_short(self):
        is_strong, message = is_password_strong("test")
        assert is_strong is False
        assert message == "Password must be at least 8 characters long"

    def test_password_without_upper(self):
        is_strong, message = is_password_strong("password")
        assert is_strong is False
        assert message == "Password must contain at least one uppercase letter"

    def test_password_without_lower(self):
        is_strong, message = is_password_strong("PASSWORD")
        assert is_strong is False
        assert message == "Password must contain at least one lowercase letter"

    def test_password_without_digits(self):
        is_strong, message = is_password_strong("Password")
        assert is_strong is False
        assert message == "Password must contain at least one number"

    def test_password_without_symbols(self):
        is_strong, message = is_password_strong("Password8")
        assert is_strong is False
        assert message == "Password must contain at least one special character"

    def test_right_password(self):
        is_strong, message = is_password_strong("Passw0rd!")
        assert is_strong is True
        assert message == "Password is valid"
