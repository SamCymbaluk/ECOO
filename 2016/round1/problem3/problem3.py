file = open("DATA31.txt")


# The trick with this one is determining what number to sort first
# What we do is loop though the numbers in descending order and check their indexes
# When there is a number the appears to the RIGHT of a larger number we know that needs to be sorted first
def first_sort_num(n, trains):
    index = n - 1
    # Loop in descending order
    for train in range(n, 0, -1):
        current_index = trains.index(train)
        if current_index > index:
            return train
        else:
            index = current_index
    return 1


def test_case():
    n = int(file.readline())
    # There is some weirdness with loading the trains from the data file because there is a trailing space
    trains = list(map(int, file.readline().rstrip(" \n").split(" ")))
    cost = 0

    # Once we determine the number to start sorting on we continue sorting in descending order from that number
    for train in range(first_sort_num(n, trains), 0, -1):
        index = trains.index(train)

        # Move the train car to the back of the train
        trains.pop(index)
        trains.insert(0, train)

        # Add the change in position to cost
        cost += index

    print(cost)


for case in range(10):
    test_case()
