import getpass
import bcrypt

password = getpass.getpass("Enter the password to hash")
hashed_password = bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt())
print("Your hashed password is"+hashed_password.decode())