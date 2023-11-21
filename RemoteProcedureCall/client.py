import xmlrpc.client
proxy = xmlrpc.client.ServerProxy("http://localhost:6789")
print("Connected to localhost")
while True:
    print(""" Operations 
          1. Add
          2. Subtract
          3. Multiply
          4. Divide
          5. Exit """)

    ch = int(input("Enter Choice: "))
    if ch == 1:
        a = int(input("Enter a: "))
        b = int(input("Enter b: "))
        ans = proxy.add(a, b)
        print(f"Addition : {ans}")

    elif ch == 2:
        a = int(input("Enter a: "))
        b = int(input("Enter b: "))
        ans = proxy.sub(a, b)
        print(f"Subtraction : {ans}")

    elif ch == 3:
        a = int(input("Enter a: "))
        b = int(input("Enter b: "))
        ans = proxy.mul(a, b)
        print(f"Multiplication : {ans}")

    elif ch == 4:
        a = int(input("Enter a: "))
        b = int(input("Enter b: "))
        if b != 0:
            ans = proxy.div(a, b)
            print(f"Division : {ans}")
        else:
            print("Cannot divide by 0")

    elif ch == 5:
        break

    else:
        print("Enter Correct Choice")
