#Basic Structure of a python program

#Imports

#Global variables

#Functions

#Main classes


def main():

    while True:
        print("Select operation:")
        print("1. Add\n2. Subtract\n3. Multiply\n4. Divide\n5. square number\n6. Floor division \n7. Factorial\n8. Exit")

        option = input("Enter option (1/2/3/4/5/6/7/8): ")

        if option == '8':
            print("Exiting the calculator")
            break

        if option in ('1', '2', '3', '4','5','6','7','8'):
            num1 = float(input("Enter first number: "))
            if option !='5'and option !='7':
                num2 = float(input("Enter second number: "))

            if option == '1':
                print(f"{num1} + {num2} = {num1+ num2}")

            elif option == '2':
                print(f"{num1} - {num2} = {num1-num2}")

            elif option == '3':
                print(f"{num1} * {num2} = {num1*num2}")

            elif option == '4':    
                print(f"{num1} / {num2} = {num1/num2}")

            elif option =='5':
                print(f'{num1}  ** 2 = {num1*num1}')

            elif option =='6':
                print(f'{num1} // {num2} = {num1//num2}')

            elif option == '7':
                result = 1
                res = 1
                for i in range(1, int(num1) + 1):
                    result *= i
                for i in range(int(num1), 1, -1):
                    res *=i
                print(f"{res}")
                print(f"{num1}! = {result}")

        else:
            print("Invalid input. Please enter a valid number.")


if __name__ == "__main__":
    main()
    

