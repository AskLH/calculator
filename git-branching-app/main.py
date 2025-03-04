import calculator

def main():
    while True:
        print("\nSimple Calculator")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Exit")
        
        choice = input("Enter choice (1/2/3/4/5): ")
        
        if choice == "5":
            print("Goodbye!")
            break

        if choice not in ("1", "2", "3", "4"):
            print("Invalid choice, please try again.")
            continue

        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            
            if choice == "1":
                result = calculator.add(num1, num2)
            elif choice == "2":
                result = calculator.subtract(num1, num2)
            elif choice == "3":
                result = calculator.multiply(num1, num2)
            elif choice == "4":
                result = calculator.divide(num1, num2)

            print(f"Result: {result}")

        except ValueError:
            print("Invalid input! Please enter numbers only.")

if __name__ == "__main__":
    main()
