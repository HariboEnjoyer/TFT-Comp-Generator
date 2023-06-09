class Unit:
    def __init__(self, name, traits, cost):
        self.name = name
        self.traits = traits
        self.cost = cost

# Define traits, their breakpoints, and units associated with each trait
traits_breakpoints_units = {
    "Demacia": ([3, 5, 7, 9], ["Kayle", "Poppy", "Galio", "Garen", "Sona", "Jarvan", "Lux"]),
    "Freljord": ([2, 3, 4], ["Ashe", "Lissandra", "Sejuani"]),
    "Ionia": ([3, 6, 9], ["Irelia", "Jhin", "Sett", "Zed", "Karma", "Shen", "Yasuo", "Ahri"]),
    "Noxus": ([3, 6, 9], ["Cassiopeia", "Samira", "Kled", "Swain", "Darius", "Katarina", "Sion"]),
    "Piltover": ([3, 6], ["Orianna", "Vi", "Ekko", "Jayce", "Heimerdinger"]),
    "Shadow Isles": ([2, 4, 6], ["Maokai", "Viego", "Kalista", "Gwen", "Senna"]),
    "Shurima": ([3, 5, 7, 9], ["Cassiopeia", "Renekton", "Taliyah", "Akshan", "Azir", "Nasus", "Ksante"]),
    "Targon": ([2, 3, 4], ["Soraka", "Taric", "Aphelios"]),
    "Void": ([3, 6, 8], ["Chogath", "Malzahar", "Kassadin", "Reksai", "Velkoz", "Kaisa", "Belveth"]),
    "Yordle": ([3, 5], ["Poppy", "Tristana", "Teemo", "Kled", "Heimerdinger"]),
    "Zaun": ([2, 4, 6], ["Jinx", "Warwick", "Ekko", "Urgot", "Zeri"]),
    "Bastion": ([2, 4, 6, 8], ["Maokai", "Poppy", "Kassadin", "Taric", "Shen", "Ksante"]),
    "Bruiser": ([2, 4, 6], ["Chogath", "Renekton", "Vi", "Reksai", "Sejuani", "Sion"]),
    "Challenger": ([2, 4, 6, 8], ["Irelia", "Samira", "Warwick", "Kalista", "Kaisa", "Yasuo"]),
    "Deadeye": ([2, 4, 6], ["Jhin", "Ashe", "Akshan", "Aphelios", "Urgot"]),
    "Gunner": ([2, 4, 6], ["Tristana", "Jinx", "Jayce", "Zeri", "Senna"]),
    "Invoker": ([2, 4, 6], ["Cassiopeia", "Galio", "Soraka", "Karma", "Lissandra", "Shen", "Ryze"]),
    "Juggernaut": ([2, 4, 6], ["Sett", "Warwick", "Darius", "Garen", "Nasus", "Aatrox"]),
    "Multicaster": ([2, 4], ["Taliyah", "Teemo", "Sona", "Velkoz"]),
    "Rogue": ([2, 4], ["Viego", "Zed", "Ekko", "Katarina"]),
    "Slayer": ([2, 3, 4, 5, 6], ["Kayle", "Kled", "Zed", "Gwen", "Aatrox"]),
    "Sorcerer": ([2, 4, 6, 8], ["Malzahar", "Orianna", "Swain", "Taric", "Velkoz", "Lux", "Ahri"]),
    "Strategist": ([2, 3, 4, 5], ["Swain", "Teemo", "Azir", "Jarvan"])
}

unit_costs = {
    1: ["Cassiopeia", "Chogath", "Irelia", "Jhin", "Kayle", "Malzahar", "Maokai", "Orianna", "Poppy", "Renekton", "Samira", "Tristana", "Viego"],
    2: ["Ashe", "Galio", "Jinx", "Kassadin", "Kled", "Sett", "Soraka", "Swain", "Taliyah", "Teemo", "Vi", "Warwick", "Zed"],
    3: ["Akshan", "Darius", "Ekko", "Garen", "Jayce", "Kalista", "Karma", "Katarina", "Lissandra", "Reksai", "Sona", "Taric", "Velkoz"],
    4: ["Aphelios", "Azir", "Gwen", "Jarvan", "Kaisa", "Lux", "Nasus", "Sejuani", "Shen", "Urgot", "Yasuo", "Zeri"],
    5: ["Aatrox", "Ahri", "Belveth", "Heimerdinger", "Ksante", "Ryze", "Senna", "Sion"]
}


trait_breakpoints = {
    "Demacia": [3, 5, 7, 9],
    "Freljord": [2, 3, 4],
    "Ionia": [3, 6, 9],
    "Noxus": [3, 6, 9],
    "Piltover": [3, 6],
    "Shadow Isles": [2, 4, 6],
    "Shurima": [3, 5, 7, 9],
    "Targon": [2, 3, 4],
    "Void": [3, 6, 8],
    "Yordle": [3, 5],
    "Zaun": [2, 4, 6],
    "Bastion": [2, 4, 6, 8],
    "Bruiser": [2, 4, 6],
    "Challenger": [2, 4, 6, 8],
    "Deadeye": [2, 4, 6],
    "Gunner": [2, 4, 6],
    "Invoker": [2, 4, 6],
    "Juggernaut": [2, 4, 6],
    "Multicaster": [2, 4],
    "Rogue": [2, 4],
    "Slayer": [2, 3, 4, 5, 6],
    "Sorcerer": [2, 4, 6, 8],
    "Strategist": [2, 3, 4, 5]
}

unique_traits_units = {
    "Darkin": "Aatrox",
    "Empress": "Belveth",
    "Technogenius": "Heimerdinger",
    "Wanderer": "Ryze",
    "Redeemer": "Senna"
}

# Creating a list of all units
all_units = []

unit_name_to_cost = {unit: cost for cost, units in unit_costs.items() for unit in units}

for trait, (breakpoints, units) in traits_breakpoints_units.items():
    for unit in units:
        if not any(unit == x.name for x in all_units):
            cost = unit_name_to_cost[unit]
            all_units.append(Unit(unit, [trait], cost))
        else:
            for x in all_units:
                if x.name == unit:
                    x.traits.append(trait)

for trait, unit_name in unique_traits_units.items():
    for unit in all_units:
        if unit.name == unit_name:
            unit.traits.append(trait)