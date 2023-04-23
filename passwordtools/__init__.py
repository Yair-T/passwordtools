from main import PasswordTool

if __name__ == "__main__":
    password = PasswordTool.generate()
    print('your password: ' + password)
    print(f'Is your password strong? {PasswordTool.test_strong(password)}')
