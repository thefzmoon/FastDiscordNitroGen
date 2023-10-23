import random
import string

def generate_code():
    code = ''.join(random.choices(string.ascii_letters + string.digits, k=16))
    return f"https://discord.gift/{code}"

print("""
  _______ _    _ ______ ______ ________  __  ____   ____  _   _ 
 |__   __| |  | |  ____|  ____|___  /  \/  |/ __ \ / __ \| \ | |
    | |  | |__| | |__  | |__     / /| \  / | |  | | |  | |  \| |
    | |  |  __  |  __| |  __|   / / | |\/| | |  | | |  | | . ` |
    | |  | |  | | |____| |     / /__| |  | | |__| | |__| | |\  |
    |_|  |_|  |_|______|_|    /_____|_|  |_|\____/ \____/|_| \_|
                                                                                                                      
""")

quantity = int(input("Input number of Nitro Codes you would like to gen: "))

with open("output.txt", "w") as f:
    for i in range(quantity):
        code = generate_code()
        f.write(f"{code}\n")

print(f"{quantity} Discord Nitro codes have been generated and saved to output.txt")
