def load_file(filename: str = "level3/level3_1.in") -> list:
    with open(filename, "r") as file:
        return [line.strip() for line in file.readlines()]


def check_winner(styles: str) -> str:
    if "R" in styles and "P" in styles:
        return "P"
    elif "R" in styles and "S" in styles:
        return "R"
    elif "P" in styles and "S" in styles:
        return "S"
    elif styles[0] == styles[1]:
        return styles[0]


def tournament_round(fighters: str) -> str:
    pairs = []
    left = ""
    while fighters:
        pairs.append(fighters[:2])
        fighters = fighters[2:]

    for pair in pairs:
        round_winner = check_winner(pair)
        left = left + round_winner
    return left


def check_tournament_winners(fighters: str) -> str:
    fighters_for_second = tournament_round(fighters)
    return tournament_round(fighters_for_second)


def write_to_file(data: list, filename: str = "level3/level3_1.out") -> None:
    with open(filename, "w") as file:
        for line in data:
            file.write(line + "\n")


def tournament(data: list) -> list:
    rounds = []
    for tourn in data[1:]:
        tourn = tourn.split(" ")
        rocks = "R"*tourn[0][::-1]
        papers = "P"*tourn[1][::-1]
        scissors = "S"*tourn[2][::-1]
        if rnd := gen_round(rocks, papers, scissors):
            rounds.append(rnd)
    return rounds


if __name__ == '__main__':
    """comp = tournament(load_file("level3/level3_example.in"))
    print(comp)
    write_to_file(comp, "level3/level3_example_our.out")
    exit()"""
    for i in range(1, 5 + 1):
        comp = tournament(load_file(f"level3/level3_{i}.in"))
        write_to_file(comp, f"level3/level3_{i}.out")
