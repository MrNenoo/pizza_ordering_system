import re

class ValidationError(Exception):
    pass

def validate_name(name: str):
    if not re.fullmatch(r"[A-Za-z ]{2,50}", name):
        raise ValidationError("Invalid name. Use letters and spaces only (2–50 characters).")
    return name.strip()

def validate_mobile(mobile: str):
    if not re.fullmatch(r"[6-9]\d{9}", mobile):
        raise ValidationError("Invalid mobile number. It should start with 6–9 and have 10 digits.")
    return mobile
