"""
File : core/utils.py
Description : Utility functions for validating user data
                (password security, formatting, pseudo security, etc.).
Autor : Alex Kamano
Version : 1.0
Project : PyPortal
Date : 9 March 2026
"""

import re
import os

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

def load_blacklist():
    """
            Function to get the list of blacklisted words
            :return list of blacklisted words
            """
    #Load the list of forbidden words
    file_path = os.path.join(os.path.dirname(__file__), 'blacklist.txt')
    if not os.path.isfile(file_path):
        return []
    with open(file_path, 'r', encoding='utf-8') as f:
        # Get all the ligns, delete all the space and put it in lower case
        return [line.strip().lower() for line in f if line.strip()]

def is_username_safe(username):
    """
            Function to check if username is safe
            :param username:
            :return a boolean value indicating if username is safe and a message:
            """
    # Check if the pseudo is on the blacklist
    username = username.lower()
    blacklist = load_blacklist()

    for bad_word in blacklist:
        #This regex (\b) check if the word is in between of wrong world
        # or if he's at beginning or at the end of the world to avoid to be block
        pattern = r'\b' + re.escape(bad_word.lower()) + r'\b'
        #check if the forbidden word is in the pseudo
        if re.search(pattern, username) or bad_word == username:
            return False, f"The word '{bad_word}' isn't allowed in the username"

    return True, "Username safe"

def is_username_format_valid(username):
    """
            Function to check if username is valid
            :param username:
            :return a boolean value indicating if username is valid and a message:
            """
    username = username.lower()
    blacklist = load_blacklist()

    pattern = r'^[a-zA-Z0-9_éèàêëîïôûùÇç]{3,20}$'

    if not re.match(pattern, username):
        return False, "The username need to be between 3 and 20 characters long and contain only letters, numbers, or underscore"
    return True, "Username format is valid"

def validate_username(username):
    """
            Function to validate username
            :param username:
            :return a boolean value indicating if username is valid and a message:
            """
    is_valid, message = is_username_format_valid(username)
    if not is_valid:
        return False, message

    is_safe, message_safe = is_username_safe(username)
    if not is_safe:
        return False, message_safe

    return True, "Perfect username"