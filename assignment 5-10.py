attempts = 3

for i in range(attempts):
    username = input("Enter your username: ")
    password = int(input("Enter your password: "))

    if username == "admin" and password == 1234:
        print("✅ Login successful!")
        n = int(input("Enter a number: "))
        print(f"Prime numbers between 2 and {n} are:")
        for num in range(2, n + 1):
            for j in range(2, int(num ** 0.5) + 1):
                if num % j == 0:
                    break
            else:
                print(num)
        break  

    else:
        remaining = attempts - (i + 1)
        if remaining > 0:
            print(f"Incorrect credentials. Attempts left: {remaining}\n")
        else:
            print("Account locked! Too many failed attempts.")