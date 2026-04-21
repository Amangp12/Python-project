import requests
import random
import time
import webbrowser

emoticon = "૮(˶ㅠ︿ㅠ)ა"

def main():
    global emoticon
    say("Hello! How can I assist you today?")
    
    while True:
        choice = input("Please type what you'd like to do (e.g., calculate, game, weather, visit site, set timer, exit, etc.): ").strip().lower()

        if "calculate" in choice:
            get_cal()
        elif "game" in choice:
            say("I have two games: Snake, Water, and Gun, and a Number Guessing Game.")
            ask = input("Which game do you want to play? ").strip().title()
            if "snake" in ask or "1" in ask:
                get_snake_game()
            elif "guess" in ask or "2" in ask:
                get_guess_game()
        elif "weather" in choice:
            say("Here is the weather report:")
            get_weather()
        elif "visit" in choice:
            visit_site()
        elif "set timer" in choice:
            set_timer()
        elif "exit" in choice:
            print(f"Goodbye {emoticon}")
            break
        else:
            say("Sorry, I didn't understand that. Please try again.")

def say(phrase, sep=" "):
    print(phrase + sep + emoticon)

def get_weather():
    api_key = "cfdffd11a852c95e68abb69f606bcb87"
    lat = 26.922069
    lon = 75.778885
    url = f"http://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}&units=metric"

    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        temp = data['main']['temp']
        description = data['weather'][0]['description'].capitalize()
        print(f"The current temperature in Jaipur is {temp}°C with {description}.")
    else:
        print("Sorry, I couldn't retrieve the weather information.")

def get_snake_game():
    win, lost, draw = 0, 0, 0

    while True:
        print("Enter 'R' for Rock, 'P' for Paper, and 'S' for Scissor")
        player_input = input("Enter your input: ").title()

        if player_input == 'R':
            input_code = -1
        elif player_input == 'P':
            input_code = 0
        elif player_input == 'S':
            input_code = 1
        else:
            print('Invalid input. Please read the instructions before inputting.')
            continue
        
        computer_input = random.choice([-1, 0, 1])
        result = game(input_code, computer_input)
        
        print(f"Your choice: {to_choice(input_code)}")
        print(f"Computer's choice: {to_choice(computer_input)}")

        if result == -1:
            print('Computer WON')
            lost += 1
        elif result == 0:
            print('It is a DRAW')
            draw += 1
        elif result == 1:
            print('CONGRATULATIONS! You won')
            win += 1

        play_again = input("Do you want to continue playing? (Y/N): ").title()
        if play_again != 'Y':
            break

    print(f"\nTotal games played: {win + lost + draw}")
    print(f"Total wins: {win}")
    print(f"Total losses: {lost}")
    print(f"Total draws: {draw}")

def game(player, computer):
    if player == computer:
        return 0
    elif (player == -1 and computer == 0) or (player == 0 and computer == 1) or (player == 1 and computer == -1):
        return -1
    else:
        return 1

def to_choice(code):
    return {-1: 'Rock', 0: 'Paper', 1: 'Scissors'}.get(code)

def get_guess_game():
    number_to_guess = random.randint(1, 15)
    attempts = 0

    while True:
        try:
            player_guess = int(input("Guess the number (Between 1 and 15): "))
            attempts += 1

            if player_guess < number_to_guess:
                print("Too low! Try again.")
            elif player_guess > number_to_guess:
                print("Too high! Try again.")
            else:
                print(f"Congratulations! You've guessed the number in {attempts} attempts.")
                break

        except ValueError:
            print("Invalid input! Please enter a number between 1 and 15.")

def get_cal():
    expression = input("Enter a mathematical expression: ").strip()
    components = expression.split()

    if len(components) % 2 == 0:
        print("Invalid input format. Please enter in the correct format 'number operator number ...'.")
        return

    try:
        result = float(components[0])

        for i in range(1, len(components) - 1, 2):
            operator = components[i]
            next_number = float(components[i + 1])

            if operator == "+":
                result += next_number
            elif operator == "-":
                result -= next_number
            elif operator == "*":
                result *= next_number
            elif operator == "/":
                if next_number != 0:
                    result /= next_number
                else:
                    print("Error: Division by zero is not allowed.")
                    return
            else:
                print(f"Invalid operator '{operator}'. Please use one of +, -, *, /.")
                return

        print(f"The result of {expression} is: {result}")

    except ValueError:
        print("Invalid numbers. Please enter valid numerical values.")

def visit_site():
    url = input("Enter the website URL you want to visit: ").strip()
    if url:
        webbrowser.open(url)
        say(f"Opening {url}")
    else:
        say("Invalid URL.")

def set_timer():
    try:
        seconds = int(input("Enter the number of seconds for the timer: ").strip())
        say(f"Timer set for {seconds} seconds.")
        time.sleep(seconds)
        say("Time's up!")
    except ValueError:
        say("Invalid input. Please enter a number.")

main()
