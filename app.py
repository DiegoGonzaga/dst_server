from worlds import worlds
from script_dst import start_server
import os
from dotenv import load_dotenv


def show_options():
    i = 0
    quantity_worlds = len(worlds)

    if os.name == "posix":
        _ = os.system("clear")
    else:
        _ = os.system("cls")
    print("*** DON'T STARVE TOGETHER DEDDICATED SERVER STARTER ***\n\n")
    while quantity_worlds > i:
        world = worlds[i]
        name = world.get("name")
        description = world.get("description")
        public_name = world.get("public_name")

        description_text = ""
        quantity_descriptions = len(description)
        j = 0
        while j < quantity_descriptions:
            description_text = (
                description_text + "\t" + f"{j+1})" + description[j] + "\n"
            )
            j = j + 1

        print(
            f"[{i+1}] {name}\nPUBLIC NAME:\n\t{public_name}\nDESCRIPTION:\n{description_text}\n"
        )
        i = i + 1
    print("[0] EXIT")


def choose_world(limit):
    if limit < 0:
        raise ValueError("Must be greater than zero.")
    choice = None
    options = []
    i = 0
    while i <= limit:
        options.append(str(i))
        i = i + 1
    while choice not in options:
        print("Choose world:")
        choice = input()
        if choice not in options:
            print("Invalid number! Please choose between options!")
    return choice


def main():
    load_dotenv()
    show_options()
    choice = choose_world(len(worlds))
    choice = int(choice)
    if choice != 0:
        start_server(worlds[choice - 1]["name"])


main()
