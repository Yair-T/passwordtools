import re
import secrets
import string


class PasswordTool:
    def test_strong(password):
        """
        The function checks if a given password is strong by ensuring it has at least 8 characters and
        contains a combination of letters, numbers, and special characters.

        :param password: The password parameter is a string that represents the password that needs to be
        tested for strength
        :return: a boolean value. It returns True if the password is strong (i.e. it has at least 8
        characters and contains at least one uppercase letter, one lowercase letter, one digit, and one
        special character), and False otherwise.
        """
        if len(password) < 12:
            return False

        return bool(re.match(r"(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[!@#$%^&*)(}{][><?.|\",:']).+", password))

    def generate(length=12):
        """
        This is a Python function that generates a random password of a specified length using a combination
        of letters, digits, and punctuation.

        :param length: The length parameter is an optional argument that specifies the length of the
        password to be generated. If no value is provided for length, the default value of 12 will be used,
        defaults to 12 (optional)
        :return: a randomly generated password of the specified length (default length is 12) that includes
        letters (both uppercase and lowercase), digits, and punctuation. However, the while loop condition
        suggests that there is a missing function `test_password_strong` that is not defined in the code
        snippet.
        """
        if length < 12:
            return None
        alphabet = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(secrets.choice(alphabet) for i in range(length))
        while PasswordTool.test_strong(password) == False:
            alphabet = string.ascii_letters + string.digits + string.punctuation
            password = ''.join(secrets.choice(alphabet) for i in range(length))
        return password
