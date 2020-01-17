def greedy_sorting(ls):
    output = []
    identity = []
    for i in range(1, len(ls)+1):
        identity.append(i)

    while True:
        if ls == identity:
            return output

        start = 0
        x = 0
        for i in range(len(ls)):
            if ls[i] != identity[i]:
                start = i
                break
            else:
                x += 1

        stop = 0
        for i in range(start, len(ls)):
            if ls[i] == identity[x] or ls[i] == -identity[x]:
                stop = i+1

        ls = flip(start, stop, ls)
        printer(ls)


def printer(ls):
    s = "("
    for i in range(len(ls)):
        if i == len(ls)-1:
            if ls[i] < 0:
                s = s + str(ls[i]) + ")"
            elif ls[i] == 0:
                s = s + str(ls[i]) + ")"
            else:
                s = s + "+" + str(ls[i]) + ")"
        else:
            if ls[i] < 0:
                s = s + str(ls[i]) + " "
            elif ls[i] == 0:
                s = s + str(ls[i]) + " "
            else:
                s = s + "+" + str(ls[i]) + " "
    print(s)


def flip(start, stop, ls):
    reversed = ls[start:stop]
    reversed.reverse()
    counter = 0
    for i in range(start, stop):
        ls[i] = -reversed[counter]
        counter += 1
    return ls


def file_reader(txt):
    with open(txt, "r") as file:
        data = file.read().split(" ")
        ls = []
        data[0] = data[0].replace('(', '')
        data[len(data)-1] = data[len(data)-1].replace(')', '')
        for i in data:
            ls.append(int(i))
    return ls


if __name__ == '__main__':
    l = file_reader('input2.txt')
    # l = [-3, +4, +1, +5, -2]
    greedy_sorting(l)


