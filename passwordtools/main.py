#
# ======================= © All rights reserved ==========================
#                  Programmed by www.youtube.com/@Yair-T
# =========================== In MIT License =============================
#
import re
import secrets
import string

class PasswordTool():
    @staticmethod
    def is_strong(password) -> bool:
        """
        Returns T if password is str of 12+ chars with 1+ of each: lower, upper, digit, special. F otherwise.
        :param password: Password to check
        :return: bool for password strength
        """
        if len(password) < 12:
            return False
        return bool(re.match(r"(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[!@#$%^&*)(}{][><?.|\",:']).+", password))

    @staticmethod
    def generate(length: int = 12) -> str:
        """
        Returns a random strong password of length, which is 12+ chars with letters, digits, punctuation. 
        Returns ValueError if length < 12. Sets length to 12 if None.
        :param length: Desired password length
        :return: A strong password
        """
        if length < 12:
            raise Exception("The length of the password must be 12 or more!")
        else:
            alphabet = string.ascii_letters + string.digits + string.punctuation
            password: str = ''.join(secrets.choice(alphabet) for i in range(length))
            while not PasswordTool.is_strong(password):
                alphabet = string.ascii_letters + string.digits + string.punctuation
                password: str = ''.join(secrets.choice(alphabet) for i in range(length))
            return password
