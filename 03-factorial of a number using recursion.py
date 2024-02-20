while True:
    try:
        n = int(input("Enter a positive integer: "))
        if n <= 0:
            raise ValueError("Please enter a positive integer.")
        
        def fact(n):
            if n == 1:
                return 1
            else:
                return n * fact(n - 1)

        res = fact(n)
        print("The factorial of the given number:", res)

    except ValueError as ve:
        print(f"Error: {ve}")
        continue

    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        continue

    ch = input("Do you want to continue? (y/n) ")
    if ch.lower() != 'y':
        break
