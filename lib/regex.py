import re

# Matches names like: John Cena, Anya Taylor-Joy, D'Angelo
name = r"^[A-Z][a-z]*(?:['-][A-Z][a-z]*)?(?:\s[A-Z][a-z]*(?:['-][A-Z][a-z]*)?)?$"
name_regex = re.compile(name)

# Matches: 555-555-5555, 555.555.5555, 5555555555, (555) 555-5555
phone_number = r"^(\(\d{3}\)\s|\d{3}[-. ]?)?\d{3}[-. ]?\d{4}$"
phone_regex = re.compile(phone_number)

# Email must start with a letter, allow . and - in name and domain
email_address = r"^[a-zA-Z][\w\.-]*@[a-zA-Z0-9.-]+\.\w+$"
email_regex = re.compile(email_address)
