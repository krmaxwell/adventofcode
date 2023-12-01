from day1 import part1, get_first_number, get_last_number

test_data = ["1abc2", "pqr3stu8vwx", "a1b2c3d4e5f", "treb7uchet"]


def test_day1_part1():
    assert part1(test_data) == 142


def test_get_first_number():
    test_str = test_data[0]
    assert get_first_number(test_str) == 1


def test_get_last_number():
    test_str = test_data[0]
    assert get_last_number(test_str) == 2
