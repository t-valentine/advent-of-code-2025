def dialOverflow(dial):
    i = dial
    if dial in range(0, 99):
        return dial
    while i not in range(0, 99):
        if i > 99:
            i -= 100
        elif i < 0:
            i += 100
        else:
            break
    return i


def day1():
    rotations = []
    dial = 50
    zeroes = 0
    # with open('test_input.txt', 'r') as file:
    with open('input.txt', 'r') as file:
        rotations = [line.rstrip('\n') for line in file]
    # print(rotations)
    for r in rotations:
        if r[0] == "R":
            dial += int(r[1:])
            dial = dialOverflow(dial)
        elif r[0] == "L":
            dial -= int(r[1:])
            dial = dialOverflow(dial)
        if dial == 0:
            zeroes += 1
        # print(dial)
    return print(f"Final Dial: {dial}\nZeroes: {zeroes}")


day1()
# answer is between 5500 and 3400... not very helpful lol
# pt 1 answer is 995

print(266 % 100)
