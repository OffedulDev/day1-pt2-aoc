sums = []

def sumAndAddToList(_3rd, _2nd, _1st):


    res = _3rd + _2nd + _1st
    sums.append(_3rd + _2nd + _1st)


    return "Added to list 'sums' number: " + str(res)


def main():
    _file = open("input.in", "rt")
    _fileContent = (_file.read()).split("\n")
    _numbers = len(_fileContent)
    _increments = 0
    # _index = 0
    
    for i in _fileContent:

        if _fileContent.index(i) == (len(_fileContent) + 1):
             sums.append(i)
             sums.append(_fileContent[_fileContent.index(i) - 1])
             break

        thirdNum = _fileContent[_fileContent.index(i)]
        secondNum = _fileContent[_fileContent.index(i) - 1]
        firstNum = _fileContent[_fileContent.index(i) - 2]

        
        
        sumAndAddToList(int(thirdNum), int(secondNum), int(firstNum))
    
    for i in sums:

        if sums.index(i) == (len(sums) - 1): break

        if int(i) < int(sums[sums.index(i) + 1]):
            _increments += 1
        else:
            continue
    
    print(_increments) # _index





if __name__ == "__main__":
    main()
