f = open("input.txt", "r")

possible_games = []
impossible_games = []
possible_total = 0

for i in f:
    gid = int(i.split(":")[0].split()[1])
    games = i.strip().split(": ")[1].split("; ")

    possible = True

    nums = i.strip().split(": ")[1].replace(";", ",").split(", ")

    for num in nums:
        if int(num.split(" ")[0]) > 14:
            possible = False
            print("Game ", gid, " Exceeds blue max")
            break
        elif int(num.split(" ")[0]) == 14:
            if num.split(" ")[1] not in ["blue"]:
                possible = False
                print("Game ", gid, " Exceeds red/green max")
                break
            else:
                print(gid, ": ", num)
        elif int(num.split(" ")[0]) == 13:
            if num.split(" ")[1] not in ["blue", "green"]:
                possible = False
                print("Game ", gid, " Exceeds red max")
                break
            else:
                print(gid, ": ", num)
        else:
            print(gid, ": ", num)

    if possible:
        possible_games.append(gid)
        possible_total += gid
    else:
        impossible_games.append(gid)

print(possible_games)
print(impossible_games)
print(possible_total)
