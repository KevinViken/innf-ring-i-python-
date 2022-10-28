def pluss(x, y):
    return x + y

def minus(x, y):
    return x - y

def gange(x, y):
    return x * y

def dele(x, y):
    return x / y

while True:
    print("Regne metode")
    print("1. pluss")
    print("2. minus")
    print("3. gange")
    print("4. dele")


    choice = input("Velg regne metode(1/2/3/4): ")

    if choice in ("1", "2", "3", "4"):
        num1 = float(input("første nummer: "))
        num2 = float(input("andre nummer: "))

        if choice == "1":
            print(num1, "+", num2, "=", pluss(num1, num2))

        elif choice == "2":
            print(num1, "-", num2, "=", minus(num1, num2))

        elif choice == "3":
            print(num1, "*", num2, "=", gange(num1, num2))
        
        elif choice == "4":
            print(num1, "/", num2, "=", dele(num1, num2))

        
        next_calculation = input("Neste utregning? (yes/no): ")
        if next_calculation == "no":
            break

    else:
        print("Invalid Input")