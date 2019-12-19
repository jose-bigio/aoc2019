

def parse_input():
    with open("input.txt") as f:
        orbits = {}
        reverse_orbits = {}
        for line in f:
            split = line.rstrip().split(")")
            orbits[split[1]] = split[0]
            reverse_orbits[split[0]] = split[1]

    return orbits, reverse_orbits


def indirect_orbits(orbit, orbits):
    # count indirect orbits
        count = 0
        found = True
        while found:
            if orbit not in orbits:
                found = False
            else:
                orbit = orbits[orbit]
                count += 1
        return count

def count_orbits(orbits):
    count = 0
    for orbit in orbits:
        # direct orbit
        #count += 1
        # count indirect orbits
        count += indirect_orbits(orbit, orbits)

    return count


def find_shortest_path(orbits, reverse_orbits):
    start = orbits["YOU"]


if __name__ == "__main__":
    orbits, reverse_orbits = parse_input()
    print(count_orbits(orbits))
    #print(indirect_orbits("L", orbits))
