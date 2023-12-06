f = open("input.txt", "r")

# Almost got it on the recursion.  Need to find a way to skip the indices contained within a number.

currentnums = []
currentsyms = []
nums = "0123456789"

line = 0


def findnumbers(index, string, numbers):
    currentindex = index
    numbers = numbers

    # while string:
    #     for i in string[currentindex:]:
    #         print("current index is", string.find(i, currentindex))
    #         if i in nums:
    #             startindex = string.find(i, currentindex)
    #             print("startindex is", startindex)
    #             num = ""
    #             for x in string[startindex:]:
    #                 if x in nums:
    #                     num += x
    #                 else:
    #                     endindex = string.find(x, startindex)
    #                     print("endindex is", endindex)
    #                     currentindex = endindex
    #                     break
    #             num = int(num)
    #             print("num is", num)
    #             number = (num, (startindex, endindex))
    #             print("number is", number)
    #             numbers.append(number)
    #             print(numbers)
    #         else:
    #             currentindex = currentindex + 1
    #     findnumbers(index=currentindex, string=string, numbers=numbers)
    # else:
    #     return numbers

    # while currentindex <= len(string) + 1:
    #     print("current index is", currentindex)
    #     if string[currentindex] in nums:
    #         startindex = currentindex
    #         endindex = None
    #         print("startindex is", startindex)
    #         num = ""
    #         for x in string[startindex:]:
    #             if x in nums:
    #                 num += x
    #                 print(num)
    #             else:
    #                 endindex = string.find(x, startindex)
    #                 print("endindex is", endindex)
    #                 currentindex = endindex
    #         num = int(num)
    #         print("num is", num)
    #         number = (num, (startindex, endindex))
    #         print("number is", number)
    #         numbers.append(number)
    #         print(numbers)
    #     else:
    #         currentindex += 1

    # return findnumbers(currentindex, string, numbers)

    if currentindex != len(string) + 1:
        for i in range(currentindex, len(string) + 1):
            print("current index is", currentindex)
            if string[i] in nums:
                startindex = i
                print("startindex is", startindex)
                num = ""
                for x in string[startindex:]:
                    if x in nums:
                        num += x
                    else:
                        endindex = string.find(x, startindex)
                        print("endindex is", endindex)
                        currentindex = endindex
                        break
                num = int(num)
                print("num is", num)
                number = (num, (startindex, endindex))
                print("number is", number)
                numbers.append(number)
                print(numbers)
            else:
                currentindex = i
        findnumbers(index=currentindex, string=string, numbers=numbers)
    else:
        return numbers


print(findnumbers(0, f.readline(), []))


# record number indices: if i is not num and i+1 is num, i+1 is start index.  If i is num and i+1 is not num, i is end index.  Line[start:end] is num (integer).

# dict of num, tuple of start/end indices

# record symbol indices: if i is neither num nor dot, place index in list.
