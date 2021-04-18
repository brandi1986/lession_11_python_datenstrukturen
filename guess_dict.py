import random
import json
import datetime
import operator

secret = random.randint(1, 30)
attempts = 0

with open("score_dict.json", "r") as file_handle:
    score_list_dict = json.loads(file_handle.read())

sorted_score = sorted(score_list_dict, key=operator.itemgetter('attempts'))[:3]

for score_dict in sorted_score:
    score_text = "Player {0} had {1} attempts on {2}. The secret number was {3}. The wrong guesses were: {4}"\
        .format(score_dict.get("name"),
                str(score_dict.get("attempts")),
                score_dict.get("date"),
                score_dict.get("secret"),
                score_dict.get("wrong_guesses"))
    print(score_text)


name = input("What´s your name?")
wrong_guesses = []
while True:
    guess = int(input("Guess the secret number (between 1 and 30): "))
    attempts += 1

    if guess == secret:
        print("You've guessed it - congratulations! It's number " + str(secret))
        print("Attempts needed: " + str(attempts))

        dict_entry = {
            "name": name,
            "attempts": attempts,
            "date": str(datetime.datetime.now()),
            "secret": secret,
            "wrong_guesses": wrong_guesses,
        }
        score_list_dict.append(dict_entry)
        with open("score_dict.json", "w") as file_handle:
            file_handle.write(json.dumps(score_list_dict))
        break

    elif guess > secret:
        print("Your guess is not correct... try something smaller")
    elif guess < secret:
        print("Your guess is not correct... try something bigger")
    wrong_guesses.append(guess)
