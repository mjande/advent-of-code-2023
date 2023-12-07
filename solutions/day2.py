class Cubes:
    def __init__(self, string):
        count, color = string.split(" ")
        self.count = int(count)
        self.color = color

def is_possible(game_rounds):
    for round in game_rounds:
        for cube_string in round.split(","):
            cubes = Cubes(cube_string.strip())
            if ((cubes.color == 'red' and cubes.count > 12)
                or (cubes.color == 'green' and cubes.count > 13)
                or (cubes.color == 'blue' and cubes.count > 14)
            ):
                return False
    return True

def get_power_of_set(game_rounds):
    min_red, min_green, min_blue = 0, 0, 0

    for round in game_rounds:
        for cube_string in round.split(","):
            cubes = Cubes(cube_string.strip())
            if cubes.color == 'red' and cubes.count > min_red:
                min_red = cubes.count
            elif cubes.color == 'green' and cubes.count > min_green:
                min_green = cubes.count
            elif cubes.color == 'blue' and cubes.count > min_blue:
                min_blue = cubes.count

    return min_red * min_green * min_blue
    

if __name__ == '__main__':
    # Part 1
    with open("./inputs/day2.txt") as input:
        res = 0

        for game in input: 
            name, rounds = game.split(":")
            if is_possible(rounds.split(";")):
                res += int(name.split(" ")[1])

    print("Part One:", res)

    # Part 2
    with open("./inputs/day2.txt") as input:
        res = 0

        for game in input:
            rounds = game.split(":")[1]
            res += get_power_of_set(rounds.split(";"))

    print("Part Two:", res)
