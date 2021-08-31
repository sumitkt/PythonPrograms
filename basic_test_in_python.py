################Recursion 1########

# q: print decreasing value from n to 1

def printDecreasing(n):
    if n == 0:
        return
    print(n)
    printDecreasing(n - 1)


def printIncreasing(n):
    if n == 0:
        return

    printIncreasing(n - 1)
    print(n)


def printDecreasingIncreasing(n):
    if (n == 0):
        return
    print(n)
    printDecreasingIncreasing(n - 1)
    print(n)


def printFactorial(n):
    if n == 0:
        return

    printFactorial(n - 1)
    print('*' + str(n), end='') if n != 1 else print(str(n), end='')


def powerLinear(x, n):
    if n == 0:
        return 1

    return x * powerLinear(x, n - 1)


def powerLogarithmic(x, n):
    if n == 0:
        return 1

    x1 = powerLogarithmic(x, n // 2)
    # x2=powerLogarithmic(x,n//2) #why to call this!!!! this is redundant
    # return x1*x2
    ans = x1 * x1
    if n % 2 == 1:  # n is not even
        ans = ans * x
    return ans


def TowerOfHanoi(n, source, destination, intermediate):
    if n == 1:
        print(str(n) + source + '-->' + destination)
        return

    TowerOfHanoi(n - 1, source, intermediate, destination)
    print(str(n) + source + '-->' + destination)
    TowerOfHanoi(n - 1, intermediate, destination, source)


def displayArray(array, size):
    if size < 0:
        return

    displayArray(array, size - 1)
    print(array[size])


def displayArrayinReverse(array, size):
    if size < 0:
        return
    print(array[size])
    displayArrayinReverse(array, size - 1)


def max_in_Array(array, size):
    if size == 0:
        return array[size]

    return max(max_in_Array(array, size - 1), array[size])


def first_index_of_Occurence(array, idx, num):
    if len(array) == idx:
        return -1

    if array[idx] == num:
        return idx

    out_index = first_index_of_Occurence(array, idx + 1, num)
    '''
    if array[idx] == array[out_index]:
        return idx
    else:
        return out_index
    '''
    return out_index


def last_index_of_Occurence(array, idx, num):
    if len(array) == idx:
        return -1

    out_index = last_index_of_Occurence(array, idx + 1, num)

    if out_index != -1:
        return out_index
    else:
        if array[idx] == num:
            return idx
        else:
            return out_index


def all_occurences(array, idx, num):
    result = []
    if len(array) == idx:
        return -1
    if array[idx] == num:
        result.append(idx)

    res = all_occurences(array, idx + 1, num)
    # result.extend(res) if res != -1:
    if res == -1 and len(result) == 0:
        return -1
        # Do something
    elif res != -1:
        result.extend(res)
        return result
        # DO something
    else:
        return result


def getSSQ(string):
    if len(string) == 0:
        l = ['']
        return l



    x = getSSQ(string[:-1])
    ch = string[-1]
    new_result = []
    for stri in x:
        new_result.append(stri + '')
    for stri in x:
        new_result.append(stri + ch)
    return new_result





if __name__ == '__main__':
    # printDecreasing(5)
    # printDecreasingIncreasing(5)
    # y=powerLogarithmic(4,4)
    # print(y)
    # TowerOfHanoi(3,'A','B','C')
    array = [2, 3, 6, 9, 8, 3, 2, 3, 2, 4]
    # displayArray(array,4)
    # displayArrayinReverse(array,4)
    # print(max_in_Array(array, ))
    #print(all_occurences(array, 0, 3))
    print(getSSQ('sumitkumarthakur'))
