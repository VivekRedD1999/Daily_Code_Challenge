#    Run-length encoding is a fast and simple method of encoding strings. 
#    The basic idea is to represent repeated successive characters as a single count and character
#    For example, the string "AAAABBBCCDAA" would be encoded as "4A3B2C1D2A".
#=====================================================================================================
def Run_Length_Coding(x):
    result, final = [], ""
    count = 1
    for i in range(len(x)):
        if i == len(x) - 1:
            result.append(count)
            result.append(x[i])
        elif x[i] == x[i + 1]:
            count += 1
        else:
            result.append(count)
            result.append(x[i])
            count = 1
    for val in result:
        val = str(val)
        final += val
    return final
print(Run_Length_Coding(input()))
