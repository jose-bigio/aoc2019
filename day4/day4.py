
# adjacent_duplicate takes an array
# and checks if there are any adjacent elements which are duplicates
def adjacent_duplicate(x):
    for i in range(len(x)-1):
        if x[i] == x[i+1]:
            return True
    return False

def adjacent_duplicate_part2(x):
    duplicates = {}
    count = 1
    for i in range(len(x)-1):
        if x[i] == x[i+1]:
            count += 1
        else:
            duplicates[x[i]] = count
            count = 1

    if count != 1:
        duplicates[x[len(x)-1]] = count

    #print(duplicates)
    for _, v in duplicates.items():
        if v == 2:
            return True
    return False

def non_decreasing(x):
    for i in range(len(x)-1):
        if x[i] > x[i+1]:
            return False
    return True

def is_valid_part2(x):
    array = convert_to_array(x)
    return adjacent_duplicate_part2(array) and non_decreasing(array)

def is_valid(x):
    array = convert_to_array(x)
    return adjacent_duplicate(array) and non_decreasing(array)

def convert_to_array(x):
    return [int(x) for x in str(x)]


if __name__ == "__main__":
    #print(adjacent_duplicate_part2([1, 1, 1]))

    count = 0
    for x in range(236491, 713787):
        if is_valid_part2(x):
            count += 1

    print(count)
