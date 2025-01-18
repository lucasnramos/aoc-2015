
mock_input = ")))"
input_file = open("./input.txt", "r")

def part_one():
    count = 0
    for line in input_file:
        for char in line:
            if char == '(':
                count += 1
            else:
                count -= 1;
    print(count)


def part_two():
    count = 0
    text = input_file.readline()
    for i, char in enumerate(text):
        if char == '(':
            count += 1
        else:
            count -= 1
        if (count == -1):
            print(i + 1)
    print(count)


part_two()
