import sys

def main() :
	try :
		args = sys.argv[1:]
		if len(args) == 0 :
			return
		assert len(args) == 1, "more than one argument is provided"
		number = int(args[0])
		if number % 2 == 0 :
			print("I'm Even.")
		else :
			print("I'm Odd.")
	except ValueError :
		print(f"AssertionError: argument is not an integer")
	except AssertionError as error :
		print(f"AssertionError: {error}")

if __name__ == "__main__" :
	main()
