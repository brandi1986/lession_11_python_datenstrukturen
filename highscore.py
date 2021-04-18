import random
import json

secret = random.randint(1, 30)
attempts = 0

with open("score.json", "r") as score_file:
    score_list = json.loads(score_file.read())
    score_list.sort()
    out_list = ""
    for x in range(len(score_list)):
        out_list = out_list + str(score_list[x])
        if x != len(score_list) - 1:
            out_list += ", "
print("Guesses so far: {0}".format(out_list))

while True:
    guess = int(input("Guess the secret number (between 1 and 30): "))
    attempts += 1

    if guess == secret:
        print("You've guessed it - congratulations! It's number " + str(secret))
        print("Attempts needed: " + str(attempts))
        score_list.append(attempts)
        with open("score.json", "w") as score_file:
            score_file.write(json.dumps(score_list))
        break

    elif guess > secret:
        print("Your guess is not correct... try something smaller")
    elif guess < secret:
        print("Your guess is not correct... try something bigger")
