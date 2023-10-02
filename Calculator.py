

def main():

    while True:
        print("Select operation:")
        print("1. Add\n2. Subtract\n3. Multiply\n4. Divide\n5. Exit")

        option = input("Enter option (1/2/3/4/5): ")

        if option == '5':
            print("Exiting the calculator. Goodbye!")
            break

        if option in ('1', '2', '3', '4'):
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))

            if option == '1':
                print(f"{num1} + {num2} = {num1+ num2}")

            elif option == '2':
                print(f"{num1} - {num2} = {num1-num2}")

            elif option == '3':
                print(f"{num1} * {num2} = {num1*num2}")

            elif option == '4':
                
                print(f"{num1} / {num2} = {num1/num2}")

        else:
            print("Invalid input. Please enter a valid number.")


if __name__ == "__main__":
    main()
    

