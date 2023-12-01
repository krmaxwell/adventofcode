def part1(data: list[str]) -> int:
    total = 0
    for s in data:
        value = get_first_number(s) * 10 + get_last_number(s)
        total += value
    return total


def get_first_number(data: str) -> int:
    for c in data:
        if c.isdigit():
            return int(c)
    return -1


def get_last_number(data: str) -> int:
    return get_first_number(data[::-1])


def load_data(path: str) -> list[str]:
    with open(path) as f:
        return [line.strip() for line in f.readlines()]


if __name__ == "__main__":
    data = load_data("input/day1.txt")
    print(part1(data))
