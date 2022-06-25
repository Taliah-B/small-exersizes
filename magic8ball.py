# Magic 8 Ball program
import random


def magic8ball():
    response = input(
        "(Type your question and press enter to get an answer or type quit to exit)\nWhat is your question?\n")
    answers = [
        "It is certain",
        "It is decidedly so",
        "Without a doubt",
        "Yes definitely",
        "You may rely on it",
        "As I see it, yes",
        "Most likely",
        "Outlook good",
        "Yes",
        "Signs point to yes",
        "Reply hazy, try again",
        "Ask again later",
        "Better not to tell you now",
        "Cannot predict now",
        "Concentrate and ask again",
        "Don't count on it",
        "My reply is no",
        "My sources say no",
        "Outlook not so good",
        "Very doubtfull",
    ]

    if response == "quit":
        print("Goodbye!")
    else:
        print(random.choice(answers), "\n")
        magic8ball()


magic8ball()
