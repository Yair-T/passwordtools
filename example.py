#
# ======================= © All rights reserved ==========================
#                  Programmed by www.youtube.com/@Yair-T
# =========================== In MIT License =============================
#

from passwordtools import PasswordTool # To install: `pip install passwordtools-yt`
import pyperclip # To install: `pip install pyperclip`

password: str = PasswordTool.generate(length=12)
strength: bool = PasswordTool.test_strong(password)

if __name__ == '__main__':
    print(f'Your password is: {password}')
    print(f'Is your password strong? {strength}')

    input: str = input('Press enter to copy password to clipboard...\nTo log out of the program press any character.\n>>>')
    if input == "":
        pyperclip.copy(password)
        print('Password copied to clipboard!')
        
