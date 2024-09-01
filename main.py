import os.path
import os
import zipfile
import itertools

GREEN = '\033[92m'
RED = '\033[91m'
PURPLE = '\033[95m'
RESET = '\033[0m'

print(f"""{RED}

 _______ _____ ______ _______ _     _  ______ _    _ 
(_______|_____|_____ (_______) |   | |/ _____) |  / )
   __      _   _____) )____  | |   | | /     | | / / 
  / /     | | |  ____/  ___) | |   | | |     | |< <  
 / /____ _| |_| |    | |     | |___| | \_____| | \ \ 
(_______|_____)_|    |_|      \______|\______)_|  \_)
                                                     
""")


# apertura zip con psw
def extract_zip(zip_file, password):
    try:
        zip_file.extractall(pwd=password.encode())
        return True
    except Exception:
        return False


# bruteforce sincronizzato con extract_zip
def brute_force(zip_file_path, wordlist_path):
    with zipfile.ZipFile(zip_file_path) as zip_file:
        with open(wordlist_path, 'r', encoding='latin-1') as f:
            passwords = f.readlines()
        print(f"{GREEN}Attempting to bruteforce the zip file{RESET}")

        for password in passwords:
            password = password.strip()
            print(f"Trying Password: {RED}{password}{RESET}")
            if extract_zip(zip_file, password):
                print(f"\n{GREEN}Password found: {PURPLE}{password}{RESET}")
                return
        print("Password not found in wordlist.")

def main():
    print(
        f"{PURPLE}NOTE : {RESET}{GREEN}This Tool only works with {RED}'ZIP Legacy Encryption'{RESET}")
    print(f"{GREEN}Welcome to ZipFuck! {RED}EHF{RESET}")
    print(f"{GREEN}Please provide the path to the zip file and the wordlist.{RESET}")

    while True:
        zip_file_path = input(f"{PURPLE}Enter the path to the zip file: {RESET}")
        print(f"{GREEN}({RED}To Use the default wordlist type:{PURPLE}  rockyou.txt{GREEN})")
        wordlist_path = input(f"{PURPLE}Enter the path to the wordlist: {RESET}")

        if not os.path.exists(zip_file_path) or not os.path.exists(wordlist_path):
            print(f"{PURPLE}Please specify a valid path. {RESET}")
        else:
            break

    print(f"{RED}\nStarting brute force attack...\n{RED}")
    brute_force(zip_file_path, wordlist_path)

if __name__ == "__main__":
    main()
