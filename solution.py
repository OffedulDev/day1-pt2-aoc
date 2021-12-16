_prepareSumTab = []



def prepareSum(element, index):
    if len(_prepareSumTab) > 3:
        _prepareSumTab.clear()
    
    _prepareSumTab.insert(index, int(element))


def main():
    _tab = open("input.in", "rt").read().split("\n")
    _index = 0
    _tabLen = len(_tab)

    print(_tab)
    while _index != 3:
        _index += 1
        prepareSum(_tab[_index], _index)
    else:
        sumTag()
        _index = 0

def sumTag():
    firstSum = _prepareSumTab[0] + _prepareSumTab[1] + _prepareSumTab[2]
    print(firstSum)

    return int(firstSum)

if __name__ == "__main__":
    main()