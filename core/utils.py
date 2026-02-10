"""
File : core/utils.py
Description : Utility functions for validating user data
                (password security, formatting, etc.).
Autor : Alex Kamano
Version : 1.0
Project : PyPortal
Date : 10 février 2026
"""

import re

def is_password_strong(password):
    """
        Function to check if password is strong
        :param password:
        :return a boolean value indicating if password is strong and a message:
        """
    if len(password) < 8:
        return False, "Password must be at least 8 characters long"
    if not re.search('[A-Z]', password):
        return False, "Password must contain at least one uppercase letter"
    if not re.search('[a-z]', password):
        return False, "Password must contain at least one lowercase letter"
    if not re.search('[0-9]', password):
        return False, "Password must contain at least one number"
    if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        return False, "Password must contain at least one special character"
    return True, "Password is valid"