#Access Control System

print("ACCESS CONTROL SYSTEM")

u = "srijan"
p = "xan@192"

count = 0

while count < 3:

    name = input("Enter username: ")
    password = input("Enter password: ")

    if name == u:
        if password == p:

            print("Login Successful")
            print("Access Granted")

            print("1. View Data")
            print("2. Exit")

            option = input("Enter choice: ")

            if option == "1":
                print("You can see the secret data.")
            elif option == "2":
                print("Exit Program")
            else:
                print("Wrong Choice")

            break

        else:
            print("Wrong Password")

    else:
        print("Wrong Username")

    count = count + 1
    print("Attempts left:", 3 - count)

if count == 3:
    print("Access Denied")
