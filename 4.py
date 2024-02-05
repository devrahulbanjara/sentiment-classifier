def guess_car():
    car_list = ['Toyota', 'Honda', 'Ford', 'Chevrolet', 'BMW', 'Mercedes']
    try:
        guess = input("Guess the car model: ")
        if guess not in car_list:
            raise ValueError("Invalid guess. Please choose a car from the list.")
        if guess == 'Mercedes':
            print("Congratulations! You guessed correctly.")
        else:
            print("Incorrect guess. Try again!")
    except ValueError as ve:
        print(f"Error: {ve}")
guess_car()
