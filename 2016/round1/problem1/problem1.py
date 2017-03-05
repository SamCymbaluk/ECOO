file = open("DATA12.txt")


def test_case():
    # Read weights from file and map to ints
    weights = list(map(float, file.readline().split(" ")))
    # Number of students
    n = int(file.readline())
    # How many students passed. We will output this in the end
    passed = 0

    for student in range(n):
        score = 0.0
        marks = list(map(float, file.readline().split(" ")))
        # Loop though weights and marks
        for i in range(0, 4):
            # Calculate the score from the formula sumOf(weight*mark)
            score += (weights[i]/100) * marks[i]

        if score >= 50:
            # Student has a passing score, add one to num of passed students
            passed += 1

    print(passed)

for case in range(10):
    test_case()

