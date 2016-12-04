class BasicCalculator:
    # define functions
    def add(self, x, y):
        """This function adds two numbers"""
        return x + y

    def subtract(self, x, y):
        """This function subtracts two numbers"""
        return x - y

    def multiply(self, x, y):
        """This function multiplies two numbers"""
        return x * y

    def divide(self, x, y):
        """This function divides two numbers"""
        return x / y

    def power(self, x, y):
        """This function does a power of two numbers"""
        return x ** y

if __name__ == '__main__':

    calc = BasicCalculator()

    print("Select an operator")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Power")

    left = int(input("Enter your left number: "))
    choice = int(input("Select your operator(1, 2, 3, 4): "))
    right = int(input("Select your right number: "))

    if choice == 1:
        print(calc.add(left, right))

    elif choice == 2:
        print(calc.subtract(left, right))

    elif choice == 3:
        print(calc.multiply(left, right))

    elif choice == 4:
        print(calc.divide(left, right))

    elif choice == 5:
        print(calc.power(left, right))

    else:
        print("Invalid input")














