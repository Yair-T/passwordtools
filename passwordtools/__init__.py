#
# ======================= © All rights reserved ==========================
#                  Programmed by www.youtube.com/@Yair-T
# =========================== In MIT License =============================
#
from passwordtools.main import PasswordTool

if __name__ == "__main__":
    password = PasswordTool.generate(12)
    print('your password: ' + password)
    print(f'Is your password strong? {PasswordTool.is_strong(password)}')