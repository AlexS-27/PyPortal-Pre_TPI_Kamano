"""
File : tests/test_utils.py
Description : Test to check if the function for the verification of the password is working
Autor : Alex Kamano
Version : 1.0
Project : PyPortal
Date : 9 Mars 2026
"""
from pyexpat.errors import messages

from core.utils import is_password_strong, validate_username

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

class TestIsUsernameCorrect:
    def test_blacklist_username(self):
        bad_user = "branler"
        is_correct, message = validate_username(bad_user)
        assert is_correct is False
        assert f"'{bad_user}'" in message

    def test_least_than_3_caracters(self):
        bad_user = "lo"
        is_correct, message = validate_username(bad_user)
        assert is_correct is False
        assert message == "The username need to be between 3 and 20 characters long and contain only letters, numbers, or underscore"

    def test_higher_than_20_caracters(self):
        bad_user = "lowestandhighestusername"
        is_correct, message = validate_username(bad_user)
        assert is_correct is False
        assert message == "The username need to be between 3 and 20 characters long and contain only letters, numbers, or underscore"

    def test_unauthorized_caracters(self):
        bad_user = "unauthorized!"
        is_correct, message = validate_username(bad_user)
        assert is_correct is False
        assert message == "The username need to be between 3 and 20 characters long and contain only letters, numbers, or underscore"

    def test_correct_username(self):
        correct_user = "Clément_88"
        is_correct, message = validate_username(correct_user)
        assert is_correct is True
        assert message == "Perfect username"
