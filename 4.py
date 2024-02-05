def guess_car():
    car_list = ['Toyota', 'Honda', 'Ford', 'Chevrolet', 'BMW', 'Mercedes']
    try:
        guess = input("Guess the car model: ")
        if guess in car_list:
            print("Congratulations! You guessed correctly.")
        else:
            raise ValueError("Invalid guess. Please choose a car from the list.")
    except ValueError as ve:
        print(f"Error: {ve}")
guess_car()
