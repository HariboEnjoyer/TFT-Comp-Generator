import collections
import random

from Database import all_units, trait_breakpoints, unique_traits_units

def calculate_points(team, bonus_traits=None, included_traits=None, BD = False):
    trait_counter = collections.defaultdict(int)
    for unit in team:
        for trait in unit.traits:
            if trait not in unique_traits_units:  # ignore unique traits
                trait_counter[trait] += 1

    if bonus_traits:  # apply bonus traits
        for trait, bonus in bonus_traits.items():
            if trait not in unique_traits_units:  # ignore unique traits
                trait_counter[trait] += bonus

    if included_traits:  # must include certain traits
        for trait, min_count in included_traits.items():
            if trait_counter[trait] < min_count:
                if BD:
                    return float('inf')
                else:
                    return -1  # return a very low score if the team doesn't satisfy the conditions
    points = 0
    for trait, count in trait_counter.items():
        if trait in trait_breakpoints:  # don't attempt to score unique traits
            for breakpoint in sorted(trait_breakpoints[trait]):
                if count >= breakpoint:
                    points += 1
                else:
                    break
    return points

def generate_random_team(size, included_traits=None, included_units = None, bonus_traits=None, max_cost=None, BD=False):
    available_units = [unit for unit in all_units if unit.cost <= max_cost] if max_cost else all_units.copy()
    if BD:  # exclude units with unique traits if BD is True
        available_units = [unit for unit in available_units if not any(trait in unit.traits for trait in unique_traits_units)]
    team = []

    if included_units:
        for unit_name in included_units:
            for unit in available_units:
                if unit.name == unit_name:
                    team.append(unit)
                    available_units.remove(unit)
                    break

    if included_traits:
        for trait, count in included_traits.items():
            if bonus_traits and trait in bonus_traits:
                count -= bonus_traits[trait]
            if trait in unique_traits_units:  # check for unique traits
                for unit in available_units:
                    if trait in unit.traits:
                        team.append(unit)
                        available_units.remove(unit)
                        break
            else:  # handle normal traits as before
                # Count the traits on the team before adding units
                current_count = sum(trait in unit.traits for unit in team)
                count -= current_count  # Subtract the current count from the required count
                possible_units = [unit for unit in available_units if trait in unit.traits]
                if len(possible_units) < count:
                    raise ValueError(f"Not enough units to satisfy the requirements for trait: {trait}")
                sampled_units = random.sample(possible_units, count)
                team += sampled_units
                for unit in sampled_units:
                    available_units.remove(unit)

    while len(team) < size:
        new_unit = random.choice(available_units)
        team.append(new_unit)
        available_units.remove(new_unit)

    return team

def crossover(team1, team2, max_cost=None, BD=False):
    set1 = set(team1)
    set2 = set(team2)
    common = set1 & set2
    only1 = list(set1 - common)
    only2 = list(set2 - common)
    new_team = list(common)
    all_unique_units = list(set(all_units) - set(new_team))  # all units not already in new_team
    if max_cost is not None:
        all_unique_units = [unit for unit in all_unique_units if unit.cost <= max_cost]
    if BD:  # exclude units with unique traits if BD is True
        all_unique_units = [unit for unit in all_unique_units if not any(trait in unit.traits for trait in unique_traits_units)]
    while len(new_team) < len(team1):
        if len(only1) > 0 and (len(new_team) == len(team1) - 1 or random.random() < 0.5):
            new_unit = only1.pop(random.randrange(len(only1)))
            all_unique_units.remove(new_unit)  # remove unit from all_unique_units
            new_team.append(new_unit)
        elif len(only2) > 0:
            new_unit = only2.pop(random.randrange(len(only2)))
            all_unique_units.remove(new_unit)  # remove unit from all_unique_units
            new_team.append(new_unit)
    return new_team

def mutate(team, included_units = None, max_cost=None, BD=False):
    if included_units:
        for unit in team.copy():
            if unit.name in included_units:
                team.remove(unit)

    if team:
        if random.random() < 0.1:  # mutation rate
            all_unique_units = [unit for unit in all_units if unit not in team and (not included_units or unit.name not in included_units)]
            if max_cost is not None:
                all_unique_units = [unit for unit in all_unique_units if unit.cost <= max_cost]
            if BD:  # exclude units with unique traits if BD is True
                all_unique_units = [unit for unit in all_unique_units if not any(trait in unit.traits for trait in unique_traits_units)]
            if all_unique_units:
                team[random.randrange(len(team))] = random.choice(all_unique_units)

    if included_units:
        for unit_name in included_units:
            for unit in all_units:
                if unit.name == unit_name:
                    team.append(unit)
                    break
    return team


def print_team_info(team, bonus_traits=None):
    trait_counter = collections.defaultdict(int)
    for unit in team:
        for trait in unit.traits:
            trait_counter[trait] += 1

    if bonus_traits:
        for trait, bonus in bonus_traits.items():
            trait_counter[trait] += bonus

    print("Traits:")
    for trait, count in sorted(trait_counter.items(), key=lambda item: item[1], reverse=True):
        if trait not in unique_traits_units and count >= min(
                trait_breakpoints[trait]):  # check if the trait is not a unique trait and a breakpoint is hit
            print(f"- {trait}: {count}")
        elif trait in unique_traits_units:  # if it's a unique trait, print without breakpoints
            print(f"- {trait}: {count}")




def find_team(size, generations=1000, population_size=500, bonus_traits=None, included_traits=None, included_units=None, max_cost=None, BD=False):
    print('\nGenerating...\n')
    try:
        population = [generate_random_team(size, included_traits, included_units, bonus_traits, max_cost, BD) for _ in
                      range(population_size)]
    except ValueError as ve:
        print(f"Error occurred during team generation: {ve}")
        return
    for _ in range(generations):
        population.sort(key=lambda team: calculate_points(team, bonus_traits, included_traits, BD), reverse=not BD)  # change sorting order if BD is True
        population = population[:population_size // 2]  # keep the best half or the worst half depending on BD
        # breed new solutions
        while len(population) < population_size:
            team1, team2 = random.sample(population, 2)
            new_team = crossover(team1, team2, max_cost, BD)
            population.append(mutate(new_team, included_units, max_cost, BD))

    best_team = sorted(population[0], key=lambda unit: unit.cost)
    best_points = calculate_points(best_team, bonus_traits, included_traits, BD)

    print(f"Best team: {[unit.name for unit in best_team]}, points: {best_points}")
    print_team_info(best_team, bonus_traits)

    return best_team, best_points



