import getpass


def main():

    user_info = {"trey": "warehouse"}

    input_ = str(input("Enter your username: "))
    if input_ in user_info:
        password_ = str(input("Enter your password: "))
        if password_ == user_info[input_]:
            print("User Verified")
        else:
            print("Incorrect password!")
    else:
        print("Invalid username!")

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
