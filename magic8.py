# magic 8 ball
import random, time

answers = [
    "It is certain",
    "It is decidedly so",
    "Without a doubt",
    "Yes, definitely",
    "You may rely on it",
    "As I see it, yes",
    "Most likely",
    "Outlook good",
    "Yes",
    "Signs point to yes",
    "Reply hazy try again",
    "Ask again later",
    "Better not tell you now",
    "Cannot predict now",
    "Concentrate and ask again",
    "Don't count on it",
    "My reply is no",
    "My sources say no",
    "Outlook not so good",
    "Very doubtful",
]

exit_condition = 'q'

question = str(input("What is your question? \n"))

while question != exit_condition.lower():
    print("Thinking...")
    # 5 second delay with dots
    for i in range(6):
        if i != 0:
            print("." * i)
            time.sleep(1)

    print(random.choice(answers))
    question = str(input("What is your question? (enter 'q' to exit program) \n"))
