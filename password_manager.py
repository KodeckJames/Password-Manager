from cryptography.fernet import Fernet
# Fernet is a module that allows you to encrypt text

# To encrypt passwords, you need to use a module and you install it from the terminal by typing pip install cryptography then installs.Alternatives:-pip3 install cryptography, python -m pip install cryptography, python3 -m pip install cryptography


def load_key():
    try:
        with open("key.key", "rb") as file:
              # Open the file in binary mode ("rb")
            key = file.read()
             # Read the contents of the file
        return key
    except FileNotFoundError:
        print("Key file not found.")
        return None

master_pwd = input("What is your master password? ")
key = load_key() + master_pwd.encode()
fer = Fernet(key)

def view():
    try:
        with open("password.txt", "r") as f:
            for line in f:
                data = line.rstrip()
                # In Python, rstrip() is a string method used to remove trailing whitespace characters (spaces, tabs, newlines) from the right end of a string.
                user, passw = data.split("|")
                print(f"User: {user.strip()} | Password: {fer.decrypt(passw.strip().encode()).decode()}")
    except FileNotFoundError:
        print("Password file not found.")

def add():
    name = input("Account name: ")
    pwd = input("Password: ")
    with open("password.txt", "a") as f:
        f.write(f"{name.strip()} | {fer.encrypt(pwd.strip().encode()).decode()}\n")

        #     open("password.txt", "a"): This function is used to open a file named "password.txt" in append mode. The "a" mode means that if the file exists, the program will append data to it; if the file doesn't exist, it will be created. The function returns a file object that can be used to read from or write to the file.

# with ... as ...: This is a context manager in Python. It ensures that the file is properly closed after its suite finishes, even if an exception is raised during the execution of the code within the with block. The file object is assigned to the variable f for use within the block.

# So, the line of code opens the file "password.txt" in append mode, and the file object is accessible within the context of the with block using the variable f.
# a(append) mode-opens a file or creates one if it doesn't exist and adds something to the end of the file if it exists
# w(write) mode-completely overwrites a file if it exists
# r(read) mode-you can't write anything in the file but only read it

while True:
    mode = input("Would you like to add a new password or view existing ones (view, add), press q to quit? ").lower()
    if mode == "q":
        break
    elif mode == "view":
        view()
    elif mode == "add":
        add()
    else:
        print("Invalid mode.")




