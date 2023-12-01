f = open("code1.txt", "r")

l = []

for i in f:
    l.append(i.strip("\n"))

print(l)

sums = []

for i in l:
    nums = []
    for a in i:
        try:
            nums.append(int(a))
        except:
            pass
    # print(nums)
    num = str(nums[0]) + str(nums[-1])
    sums.append(int(num))

# print(sums)
total = sum(sums)
# print(total)

digits = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
}

nums = []
for i in l:
    numdict = {}
    for key, value in digits.items():
        if key in i:
            res = [x for x in range(len(i)) if i.startswith(key, x)]
            for r in res:
                numdict.update({r: key})
        if value in i:
            res = [x for x in range(len(i)) if i.startswith(value, x)]
            for r in res:
                numdict.update({r: value})
    numdict = dict(sorted(numdict.items()))
    print(numdict)
    num = ""
    first = numdict[min(numdict.keys())]
    last = numdict[max(numdict.keys())]

    if first in digits.keys():
        num = num + digits[first]
    else:
        num = num + first

    if last in digits.keys():
        num = num + digits[last]
    else:
        num = num + last

    nums.append(int(num))

print(nums)
print(sum(nums))
