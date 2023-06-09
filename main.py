from Teambuilder import find_team
from Database import all_units

def read_traits(saved_value, prompt):
    try:
        raw_traits = input(prompt)
        if raw_traits.lower() == "clear":
            return None
        elif raw_traits.lower() == "back":
            return saved_value
        traits = {}
        for trait in raw_traits.split(','):
            name, value = trait.split(':')
            traits[name.strip()] = int(value.strip())
        return traits

    except Exception as e:
        print(f"Invalid input format or data provided: {e}. Returning to menu.")
        return saved_value  # return saved_value to maintain previous valid input


def read_units(saved_value, prompt):
    try:
        raw_units = input(prompt)
        if raw_units.lower() == "clear":
            return None
        elif raw_units.lower() == "back":
            return saved_value
        units = [unit.strip() for unit in raw_units.split(',')]
        valid_units = [unit.name for unit in all_units]  # get names of all valid units
        for unit in units:
            if unit not in valid_units:
                print(f"Invalid unit: {unit}. Please enter valid unit names.")
                return read_units(saved_value, prompt)  # ask again if any unit is invalid
        return units
    except Exception as e:
        print(f"Invalid input format or data provided: {e}. Returning to menu.")
        return saved_value  # return saved_value to maintain previous valid input

def read_integer(saved_value, prompt, min_value=None, max_value=None):
    try:
        while True:
            value = input(prompt)
            if value.lower() == "clear":
                return None
            elif value.lower() == "back":
                return saved_value
            if value.isdigit():
                value = int(value)
                if min_value is not None and value < min_value:
                    print(f"Value should not be less than {min_value}")
                elif max_value is not None and value > max_value:
                    print(f"Value should not be more than {max_value}")
                else:
                    return value
            else:
                print("Invalid input. Please enter an integer.")
    except Exception as e:
        print(f"Unexpected error occurred: {e}. Returning to menu.")
        return saved_value  # return saved_value to maintain previous valid input


def main():
    print("Welcome to the TFT Set 9 comp generator!")

    team_size = read_integer(None, "Enter the team size (Number from 2 to 59): ", 2, 59)
    bonus_traits = None
    trait_requirements = None
    included_units = None
    max_unit_cost = 5
    BD = False

    while True:
        print("Please enter the corresponding number for what you wish to change:")
        print(f"1. Bonus Traits (Emblems/Hearts). Current: {bonus_traits if bonus_traits else 'None'}")
        print(f"2. Composition Trait Requirements. Current: {trait_requirements if trait_requirements else 'None'}")
        print(f"3. Maximum Unit Cost. Current: {max_unit_cost}")
        print(f"4. Included Units. Current: {', '.join(included_units) if included_units else 'None'}")
        print(f"5. Built Different? Current: {'Yes' if BD else 'No'}")
        print(f"6. Team Size. Current: {team_size}")
        print("7. Generate Composition")
        print("8. Exit")

        option = input()

        if option in ["1","2","3","4","5","6"]:
            print("\nYou can enter 'Clear' to reset to the default value, or enter 'Back' to return to the menu.\n")
        if option == "1":
            print("Warning: Does NOT work with unique traits (Redeemer, Technogenius, etc)")
            bonus_traits = read_traits(bonus_traits, "Enter your trait bonuses, seperated by commas. E.g., 'Sorcerer: 1' for Sorcerer+1. If you have multiple bonuses, you can enter 'Noxus: 2, Demacia: 1' for Noxus +2 and Demacia +1.\n")
        elif option == "2":
            print("Warning: Does NOT work with unique traits (Redeemer, Technogenius, etc)."
                  "If you want champions with unique traits to be included, enter their names under included units.")
            trait_requirements = read_traits(trait_requirements,"Enter your trait requirements, seperated by commas E.g., 'Demacia: 7' for a team with at least 7 Demacia units. 'Yordle: 3, Gunner: 2' for a team with at least 3 Yordles and 2 Gunners.\n")
        elif option == "3":
            max_unit_cost = read_integer(max_unit_cost, "Enter maximum unit cost (1-5)\n", 1, 5)
            if not max_unit_cost:
                max_unit_cost = 5
        elif option == "4":  # handle input for included units
            included_units = read_units(included_units, "Enter the units you want to include in your team, separated by commas. E.g., 'Senna, Malzahar'\n")
            if included_units and len(included_units) > team_size:
                print("\nError: The number of included units cannot exceed the team size.\n")
                included_units = None
        elif option == "5":
            if BD:
                BD = input("Is this a Built Different team? (y/n)\n").lower()
                if BD == 'y' or BD == 'back':
                    BD = True
            else:
                BD = input("Is this a Built Different team? (y/n)\n").lower() == 'y'
        elif option == "6":
            team_size = read_integer(team_size, "Enter team size (2 to 59)\n", 2, 59)
            if not team_size:
                team_size = 8
        elif option == "7":
            find_team(team_size, bonus_traits=bonus_traits, included_traits=trait_requirements, included_units=included_units, max_cost=max_unit_cost, BD=BD)
            while True:
                print("\nWhat do you want to do next?")
                print("1. Try again with the same requirements")
                print("2. Edit requirements")
                print("3. Exit")
                next_option = input()
                if next_option == "1":
                    find_team(team_size, bonus_traits=bonus_traits, included_traits=trait_requirements, included_units=included_units, max_cost=max_unit_cost, BD=BD)
                elif next_option == "2":
                    break
                elif next_option == "3":
                    return
                else:
                    print("Invalid option. Please choose a number from 1 to 3.")
        elif option == "8":
            break
        else:
            print("Invalid option. Please choose a number from 1 to 7.")

if __name__ == "__main__":
    main()