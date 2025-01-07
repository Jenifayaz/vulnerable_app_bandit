import subprocess
import os

# Example of a command injection vulnerability
def run_command(user_input):
    command = f"echo {user_input}"
    subprocess.run(command, shell=True)

# Example of a hardcoded secret
SECRET_KEY = "12345"

if __name__ == "__main__":
    user_input = input("Enter something: ")
    run_command(user_input)
