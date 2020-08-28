# Adventure Scenario
# adventure game using while loop
available_exits = ["north", "south", "east", "west"]

chosen_exit = ""
while chosen_exit not in available_exits:
    chosen_exit = input("Choose a direction: ")
    if chosen_exit.casefold() in available_exits:
        print("You made it out!")
        break
    if chosen_exit.casefold() == "quit":    # fixes case sensitive input to work
        print("Game over")
        break
    else:
        print("Nope, {} not the way.".format(chosen_exit))

