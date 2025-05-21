#simple access control script using conditional expressions (X if condition else Y) by lanc-kim
def get_users_from_file(username):
    try:
        with open('users.txt') as f:
            for line in f:
                stored_username, role = line.strip().split(',')
                print(f"DEBUG: found username '{stored_username}' with role '{role}'") #DEBUG to check if user.txt is being recognized, can be deleted
                if username == stored_username:
                    return role
    except FileNotFoundError:
        print("Error: users.txt file not found.")
        return None


username = (input("Enter username: "))
role = get_users_from_file(username)

if role is None:
    print("Access denied.")
else:
    try:
            pin = int(input("Enter pin: "))
            pin_status = "correct" if pin==1234 else "incorrect"
            if pin_status == "correct" and role in ["admin","it"] :
                print(f"Welcome back {username}!")
            else:
                print("Access denied.")
    except ValueError:
        print("Invalid PIN input.")

