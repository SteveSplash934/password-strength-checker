import re
from zxcvbn import zxcvbn



class PasswordChecker:
    """
    A class to check the strength of a password based on certain criteria.
    """

    """
    Sample Args:
     config = {
        "input_method": "single-input", # "single-input" or "txt-file" or "json-file" or "db-file" or "csv-file" or "sql-file"
        "input_file": None, # The file path if input_method is not "single-input"
        "file_cfg": {
            "password_row_key": "password", # The key in the file that contains the password,
            "limit": -1,
        },
        "min_length": 8,
        "max_length": 20,
        "special_characters": True,
        "uppercase": True,
        "lowercase": True,
        "digits": True
        }
    data = {
        "password": "Password123"
    }
    """

    def __init__(self, data: dict, config = {
        "input_method": "single-input", # "single-input" or "txt-file" or "json-file" or "db-file" or "csv-file" or "sql-file"
        "input_file": None, # The file path if input_method is not "single-input"
        "file_cfg": {
            "password_row_key": "password", # The key in the file that contains the password,
            "limit": -1,
        },
        "min_length": 8,
        "max_length": 20,
        "special_characters": True,
        "uppercase": True,
        "lowercase": True,
        "digits": True
        }):
        self.data = data
        self.config = config

    def check_password(self) -> dict:
        """
        Check if the password is strong using zxcvbn and custom criteria.
        :return: A dictionary with the password strength and feedback.
        """
        password = self.data.get("password")
        if not password:
            return {"valid": False, "feedback": "Password is required."}

        # Check password strength using zxcvbn
        zxcvbn_result = zxcvbn(password)
        score = zxcvbn_result["score"]
        feedback = zxcvbn_result["feedback"]

        # Check against custom criteria
        if len(password) < self.config["min_length"]:
            return {"valid": False, "feedback": f"Password must be at least {self.config['min_length']} characters long."}
        
        if not re.search(r"[A-Z]", password):
            return {"valid": False, "feedback": "Password must contain at least one uppercase letter."}
        
        if not re.search(r"[a-z]", password):
            return {"valid": False, "feedback": "Password must contain at least one lowercase letter."}
        
        if not re.search(r"[0-9]", password):
            return {"valid": False, "feedback": "Password must contain at least one digit."}
        
        if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
            return {"valid": False, "feedback": "Password must contain at least one special character."}

        # If all checks pass
        return {"valid": True, "feedback": feedback,  "score": score}

    def check_txt_password(self) -> dict:
       pass

    def check_json_password(self) -> dict:
       pass
    
    def check_db_password(self) -> dict:
       pass
    
    def check_csv_password(self) -> dict:
        pass
    
    def check_sql_password(self) -> dict:
        pass

    def run(self):
        """
        Run the password checker based on the input method specified in the config.
        :return: A dictionary with the password strength and feedback.
        """
        if self.config["input_method"] == "single-input":
            return self.check_password()
        elif self.config["input_method"] == "txt-file":
            return self.check_txt_password()
        elif self.config["input_method"] == "json-file":
            return self.check_json_password()
        elif self.config["input_method"] == "db-file":
            return self.check_db_password()
        elif self.config["input_method"] == "csv-file":
            return self.check_csv_password()
        elif self.config["input_method"] == "sql-file":
            return self.check_sql_password()
        else:
            return {"valid": False, "feedback": "Invalid input method specified."}