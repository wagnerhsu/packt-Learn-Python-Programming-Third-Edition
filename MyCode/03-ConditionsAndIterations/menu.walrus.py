flavors = ["pistachio", "malaga", "vanilla", "chocolate", "strawberry"]
prompt = "What flavor do you want?"
print(flavors)

while (choice := input(prompt)) not in flavors:
    print("That's not a flavor I know.")
print(f"You chose {choice}!")
    