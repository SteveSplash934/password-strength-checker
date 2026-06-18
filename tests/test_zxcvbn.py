import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../')))


from password_checker.PasswordChecker import PasswordChecker

# Sample configuration and data for testing
config = {}
data = {
    "password": "Password123"
}

passwordChecker = PasswordChecker(config, data)
print(passwordChecker.check_password())
