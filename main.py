from pprint import pp


def beolvas():
    with open('Nike_shoes_2023-04-16.csv', 'r', encoding='utf-8') as forras:
        bemenet = forras.read().split('\n')

    for index, item in enumerate(bemenet):
        if item == '':
            bemenet.pop(index)

    sorok = []
    for sor in bemenet:
        sor = sor.split(',')
        for index, item in enumerate(sor):
            if item == '':
                sor.pop(index)
        sorok.append(sor)

    kulcsok = sorok.pop(0)

    for item in sorok:
        item.pop(0)

    tulajdonsagok = []
    for sor in sorok:
        cipo = {}
        for index, item in enumerate(sor):
            cipo[kulcsok[index]] = item
        tulajdonsagok.append(cipo)

    with open('Nike_shoes_2023-04-17.csv', 'r', encoding='utf-8') as forras:
        bemenet = forras.read().split('\n')

    for index, item in enumerate(bemenet):
        if item == '':
            bemenet.pop(index)

    sorok = []
    for sor in bemenet:
        sor = sor.split(',')
        for index, item in enumerate(sor):
            if item == '':
                sor.pop(index)
        sorok.append(sor)

    kulcsok = sorok.pop(0)

    for item in sorok:
        item.pop(0)

    for sor in sorok:
        cipo = {}
        for index, item in enumerate(sor):
            cipo[kulcsok[index]] = item
        tulajdonsagok.append(cipo)
    return tulajdonsagok


def beker():
    return int(input('Melyik kategóriában akarsz szortírozni?  '))


def main():
    print('1 - title')
    print('2 - color')
    print('3 - full price')
    print('4 - current price')
    print('5 - publish date')
    valasz = beker()
    if valasz == 1:
        kulcs = 'title'
    elif valasz == 2:
        kulcs = 'color_breif'
    elif valasz == 3:
        kulcs = 'fullPrice'
    elif valasz == 4:
        kulcs = 'currentPrice'
    elif valasz == 5:
        kulcs = 'publish_date'

    pp(sorted(beolvas(), key=lambda cipo: cipo[kulcs]))


main()