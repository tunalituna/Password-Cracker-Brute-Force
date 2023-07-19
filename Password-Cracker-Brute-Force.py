import itertools

def password_cracker(target_password, charset, max_length):
    for length in range(1, max_length + 1):
        for combination in itertools.product(charset, repeat=length):
            password_attempt = ''.join(combination)
            if password_attempt == target_password:
                return password_attempt

    return None

def main():
    print("Password Cracker - Brute Force")
    print("------------------------------")
    target_password = input("Enter the target password: ")
    charset = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    max_password_length = 4  # You can adjust this to increase the maximum password length to check

    cracked_password = password_cracker(target_password, charset, max_password_length)

    if cracked_password:
        print(f"Password cracked: {cracked_password}")
    else:
        print("Password not found.")

if __name__ == "__main__":
    main()
