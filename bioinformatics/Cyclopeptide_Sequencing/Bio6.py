import itertools
from itertools import cycle


def cyclopeptide_sequencing(spectrum):
    output = []
    peptides = [[]]
    while len(peptides) > 0:
        peptides = expand(peptides)
        for pep in peptides:
            if mass(pep) == parent_mass(spectrum):
                if cyclospectrum(pep) == spectrum:
                    output.append(pep)
                peptides.remove(pep)
            elif not is_consistent(pep, spectrum):
                peptides.remove(pep)
    return output


def cyclopeptide_sequencing2(spectrum):
    output = []
    peptides = [[]]

    while len(peptides) != 0:
        peptides = expand(peptides)
        i = 0
        while i < len(peptides):
            peptide = peptides[i]
            if mass(peptide) == parent_mass(spectrum):
                # print(cyclospectrum2(peptide))
                # print(spectrum)
                # print()
                if cyclospectrum2(peptide).sort() == spectrum.sort():
                    output.append(peptide)
                peptides.remove(peptide)
                i = i - 1
            elif not is_consistent(peptide, spectrum):
                peptides.remove(peptide)
                i = i - 1
            i = i + 1
    return output


def mass(peptide):
    s = 0
    for i in peptide:
        s = s + i
    return s


def parent_mass(spectrum):
    return max(spectrum)


def expand(peptides):
    aa = [57, 71, 87, 97, 99, 101, 103, 113, 114, 115,
          128, 129, 131, 137, 147, 156, 163, 186]

    expanded = []
    for mass in aa:
        for p in peptides:
            c = p.copy()
            c.append(mass)
            expanded.append(c)
    return expanded


def cyclospectrum(peptide):
    spectrum = [0]
    for i in range(0, len(peptide)):
        for j in range(len(peptide)):
            if j + i < len(peptide):
                spectrum.append(mass(peptide[j: j+i]))
            else:
                first = peptide[j:]
                other = peptide[:(j + i) % len(peptide)]
                spectrum.append(mass(first) + mass(other))

    spectrum.sort()
    return spectrum


def cyclospectrum2(peptide):
    spectrum = [0]
    for i in range(1, len(peptide)):
        for start in range(len(peptide)):
            sliced = itertools.islice(cycle(peptide), start, start + i)
            spectrum.append(mass(sliced))
    spectrum.append(mass(peptide))

    return spectrum


def linspectrum(peptide):
    spectrum = [0]
    for i in range(1, len(peptide)):
        for j in range(len(peptide)):
            if i + j > len(peptide):
                continue
            else:
                spectrum.append(mass(peptide[j: j + i]))
                # print(peptide[j:j + i])


    if len(peptide) == 1:
        spectrum.append(peptide[0])
    return spectrum


def is_consistent(peptide, spectrum):
    lin = linspectrum(peptide)
    return set(lin).issubset(set(spectrum))


def file_reader(txt):
    with open(txt, "r") as file:
        data = file.read().split(" ")
        ls = []
        for i in data:
            ls.append(int(i))
    return ls


def printer(peptides):
    for ls in peptides:
        s = ""
        for i in range(len(ls)):
            if i == len(ls) - 1:
                s = s + str(ls[i])
            else:
                s = s + str(ls[i]) + "-"
        print(s)


if __name__ == '__main__':
    # ls = [0, 113, 128, 186, 241, 299, 314, 427]
    # ls2 = [0, 99, 128, 163]

    # print(sum(ls2))
    # print(linspectrum(ls2))
    # print(cyclopeptide_sequencing2(ls))
    printer(cyclopeptide_sequencing2(file_reader('pep.txt')))









