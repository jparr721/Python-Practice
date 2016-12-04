class BasicCalculator:
    # define functions
    def add(x, y):
        """This function adds two numbers"""
        return x + y

    def subtract(x, y):
        """This function subtracts two numbers"""
        return x - y

    def multiply(x, y):
        """This function multiplies two numbers"""
        return x * y

    def divide(x, y):
        """This function divides two numbers"""
        return x / y

    def power(x, y):
        """This function does a power of two numbers"""
        return x ** y

if __name__ == '__main__':

    print("Select an operator")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Power")

    left = int(input("Enter your left number: "))
    choice = int(input("Select your operator(1, 2, 3, 4): "))
    right = int(input("Select your right number: "))

    if choice == '1':
        #Error is here, it says "Unresolved reference 'add'"
        print(add(left, right))
    else:
        print("Invalid input")














