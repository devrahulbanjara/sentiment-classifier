def guess_car():
    car_list = ['Toyota', 'Honda', 'Ford', 'Chevrolet', 'BMW', 'Mercedes']

    try:
        # User input for guessing the car
        guess = input("Guess the car model: ")

        # Validate the user input
        if guess not in car_list:
            raise ValueError("Invalid guess. Please choose a car from the list.")

        # Check if the guess is correct
        if guess == 'Mercedes':
            print("Congratulations! You guessed correctly.")
        else:
            print("Incorrect guess. Try again!")

    except ValueError as ve:
        print(f"Error: {ve}")

guess_car()
