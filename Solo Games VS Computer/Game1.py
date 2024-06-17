import random as ran

choices = ["rock", "paper", "scissors"]
uninspirational_quotes = [
    "You miss 100 percent of the shots you don't take. And probably about 80 percent of the ones you do.",
    "Dream big, achieve little.",
    "Success is relative. The more successful your friends are, the less successful you feel.",
    "Aim low. You won't be disappointed.",
    "Opportunity knocks. Usually when you're not home.",
    "If at first you don't succeed, maybe it's time to lower your expectations.",
    "Believe in yourself. But not too much. Others find it annoying.",
    "Procrastination: because someday is not a day of the week.",
    "Failure is the key to limited success."
]

while True:
    user = input("Choose Rock, Paper, Scissors (or type 'exit' to quit): ").lower()
    if user == "exit":
        break
    
    computer = ran.choice(choices)
    print("You chose:", user)
    print("Computer chose:", computer)
    
    if user == computer:
        print("TIE")
    elif (user == "rock" and computer == "scissors") or \
         (user == "paper" and computer == "rock") or \
         (user == "scissors" and computer == "paper"):
        print("You Win!!!")
    else:
        print("Dang you lost :(")
        random_quote = ran.choice(uninspirational_quotes)
        print(random_quote)
