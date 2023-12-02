f = open("input.txt", "r")

total = 0

for i in f:
    gid = int(i.split(":")[0].split()[1])
    games = i.strip().split(": ")[1].split("; ")

    nums = i.strip().split(": ")[1].replace(";", ",").split(", ")

    mins = {"red": 0, "blue": 0, "green": 0}

    for num in nums:
        if int(num.split(" ")[0]) > mins[num.split(" ")[1]]:
            mins[num.split(" ")[1]] = int(num.split(" ")[0])

    power = mins["blue"] * mins["green"] * mins["red"]

    total += power

    print(gid, ":", mins, "Power:", power)

print(total)
