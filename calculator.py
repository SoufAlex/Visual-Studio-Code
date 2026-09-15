def calculator():
	first = float(input("Enter the first number: "))
	operator = input("Enter an operator (+, -, *, /): ")
	second = float(input("Enter the second number: "))

	if operator == "+":
		result = first + second
	elif operator == "-":
		result = first - second
	elif operator == "*":
		result = first * second
	elif operator == "/":
		if second == 0:
			print("Cannot divide by zero.")
			return
		result = first / second
	else:
		print("Invalid operator.")
		return

	print(f"Result: {result}")


if __name__ == "__main__":
	calculator()