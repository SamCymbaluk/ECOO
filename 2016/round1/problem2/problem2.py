file = open("DATA21.txt")


# This solution is completely brute-force and has a complexity of O(n^3)
# There is almost certainly a quicker solution but with n <= 5000 and simplification allowing n <= 100, this works
def calc_output(result, spinner_nums):
    for num1 in spinner_nums:
        for num2 in spinner_nums:
            for num3 in spinner_nums:
                if num1 + num2 + num3 == result \
                        or (num1 + num2) * num3 == result \
                        or num1 * num2 * num3 == result \
                        or (num1 * num2) + num3 == result:
                    return "T"

    return "F"


def test_case():
    # Consume spinner amount
    file.readline()

    # Spinner values can only be 1 <= s <= 100 so we can simplify the list greatly
    spinner_vals = [False] * 101
    spinner_nums = []
    for num in map(int, file.readline().split(" ")):
        spinner_vals[num] = True

    for i in range(0, 101):
        if spinner_vals[i]:
            spinner_nums.append(i)

    output = ""

    # We are checking to see if certain results are possible
    for result in map(int, file.readline().split(" ")):
        output += calc_output(result, spinner_nums)

    print(output)

for case in range(10):
    test_case()

