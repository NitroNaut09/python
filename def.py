import math

def main():
	x = int(input("Enter a number: "))
	print(f"The square of {x} is {square(x)}")

def square(n):
	return pow(n, 2)

main()