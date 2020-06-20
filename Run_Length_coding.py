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
