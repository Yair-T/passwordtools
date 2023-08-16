# passwordtools.
This Python package provides functions for generating and testing passwords. The password generator can create passwords of different lengths and complexity, and the password strength tester can assess the security of a password. The password generator uses a random number generator to generate random passwords. The Password Strength Checker uses a variety of factors to assess password security, including password length, and password complexity. This package is an invaluable tool for anyone who needs to create or test passwords.
    
### Features.
- Generates random passwords of a specified length.
- Includes letters (both uppercase and lowercase), digits, and punctuation.
- used to generate strong passwords.
- Checking the strength of passwords.
## Installation.
To install passwordtools, use the following command:

    pip install passwordtool-yt

To build from source follow these steps:
execute the command, `git clone https://github.com/Yair-T/passwordtools.git`.

Go to the project and execute the command `py -m build`.

## Documentation.
To use a package, first import it:
```python
from passwordtools import PasswordTool
```

After that, to generate the password we will execute the `generate()` command: 
```python
password: str = PasswordTool.generate()
print(password)
```

To check the strength of the password, execute the command below:
```python
print(PasswordTool.is_strong(password))
```

The full code:
```python
from passwordtools import PasswordTool
password: str = PasswordTool.generate()
print(password)
print(PasswordTool.is_strong(password))
```
### License
passwordtools is licensed under the MIT License.
This project is licensed under the MIT License. - see the [LICENSE](https://github.com/Yair-T/passwordtools/blob/main/LICENCE) file for details.