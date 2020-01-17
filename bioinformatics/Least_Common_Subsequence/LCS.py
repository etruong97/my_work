def lcs(s1, s2):
    matrix = []
    backtrack = []
    for i in range(len(s1) + 1):
        row = []
        backtrack_row = []
        for j in range(len(s2) + 1):
            row.append(0)
            backtrack_row.append(0)
        matrix.append(row)
        backtrack.append(backtrack_row)

    for i in range(1, len(s1) + 1):
        for j in range(1, len(s2) + 1):
            diagonal = matrix[i - 1][j - 1]
            if s1[i-1] == s2[j-1]:
                diagonal = diagonal + 1
            matrix[i][j] = max(matrix[i - 1][j], matrix[i][j - 1], diagonal)

            if max(matrix[i - 1][j], matrix[i][j - 1], diagonal) == matrix[i - 1][j]:
                backtrack[i][j] = 1  # vertical
            elif max(matrix[i - 1][j], matrix[i][j - 1], diagonal) == matrix[i][j - 1]:
                backtrack[i][j] = 2  # horizontal
            elif max(matrix[i - 1][j], matrix[i][j - 1], diagonal) == diagonal:
                backtrack[i][j] = 3

    # return backtrack
    # printer(backtrack)
    # print(s1)
    # print(s2)
    output_lcs(backtrack, s1, s2)


def printer(matrix):
    for i in matrix:
        print(i)


# def output_lcs(backtrack, v, i, j, output):
# #     if i == 0 or j == 0:
# #         return
# #     if backtrack[i][j] == 1:
# #         output_lcs(backtrack, v, i - 1, j, output)
# #     elif backtrack[i][j] == 2:
# #         output_lcs(backtrack, v, i, j - 1, output)
# #     elif backtrack[i][j] == 3:
# #         output_lcs(backtrack, v, i - 1, j - 1, output)
# #         print(v[i])

def output_lcs(backtrack, v, w):
    i = len(v)
    j = len(w)
    out = ""
    while i != 0 and j != 0:
        if backtrack[i][j] == 1:
            i = i -1
        elif backtrack[i][j] == 2:
            j = j - 1
        else:
            i = i - 1
            j = j -1
            out = v[i] + out
    print(out)


if __name__ == '__main__':
    lcs('CCGTTTGAGTAGCATTAGTTAGCGAACGGGACCGCTCTAGCAAACATAGCCCGCTATGTAGGGTAATGTCTTGCAGTGTCCGGTACCTAACGTTCTCGCCTTATAGGAACCCGGGTAAAACGTTGTGAACTTACGTTAATCAGAGAGTGCCAGCTAAGGGGCTGTCTTGTTGGATCGCAGCATCGGCACATCGGTGGAAACGACTGAAATTACCGAGGATTCTGCCGGAACGAAGTTTGGTTTACCTTGAACTCCTGGCGTAAGATCTAACCGCGGACCTTTATAGCGGATAAATATCTGCGTATTTAATGAGGCAGTGGATCGGTGATAGCTGTAATGAGAATCTAAGAGAAGGGACTGTAGAGTGAGGACAGGAACGACGATTCCTCGGGGCAACAGAATCGGGCGAGATGGTCTTACGAAGACAATGGCTGCTAGTAATTAGCGGCTTCTAGTGATTGAATTCGCGTTGGCCTCAGAGTGCGCTCGCTGATCCTCGGCGCTCCTTACTTTTCACGAACATACGATAATTATTACAAGTTAAAAGATCCCATGTAAGAAGGGTCAGTCTTACGTGGGCTGGTCACCGAAATCGCTTCGTCTCAGCTTGATAGCGAGGATCGGCGGAAGAGCGGATGACTTGGCAGATGCGGCTAACAGGGCTATCCTATCCGAACCCATGAGGGCGGAGTCGGCTCATAACTTCAACCAGATATTATTTCCAGCCGAGTCCTTCATCTATTCGGTCAAATACGATCCTAAGTTGCCGTCGGATGAACTCCCCCCAGGTAGATGATTCTAGGACGGCGGGACGGAATCCTGCTCAAATAGGCTAGGTCTGGCGAGCGGTAC',
        'TGGTTTAACAGCTTATCAGACGCACGATTTCATTATTGGGGGGTCAGTGAATGGGCTTGCAGGCACTCTGGCGTTCGACTCCACAGTCTGGCGATAGCAGAACTGGAGTACAGTCCCAAGCCGACTCCGTTCACAGTGACAAATCCCTTTAGCCTTTGGTACGAGGATCGCAATAAAACCGTAGAAGGAATAGGCGTCTTTACGAACACGCTCAGTCCGCGTGTTGATTGGGATACGGACAGGTTTAGTGATGGTACAACGTGAAATATCCAACTCCAGATGAGTGCGCAGTAACGGTCCAGGTAAGCATCGTTATTGCCGGACAAGGTAGGTACAGCGGCTATTGTCAATGTTGGTGTCAGCAAATGTCGAGAGCCTCTAACTTTAAGCGCTGTCCGTAGTGGGAATCACTCACCGTCTCCGTGAGACGCAATGGAATTGAGCAGGCCCGCATGTCTCAGTACGATCCCTGTCGGGCCCTAAGGAAAGGTGTTGGGTCCTCGTCTGGGACTAGTATAAATCATACTTTTACGGATTTAGGATCATCTTCGTGCATTTCCATCCCAGTTCATATAGACGGCGAATGCTGTTTAGTGTAGAGAAGGCTAAAGTCATGACCAGCGCATCTTCCGAACTGGGTCAAAAAGTCAGCCCGGGCCCGCGATAAAGATAGGCTGGGACAGCAGCCCTGGAAATGGTCCCGGAAGTCACCGTCGTGGTATATCCGTGAGAAAGGTAACAGGGTCGACTTTGTGATCTAAAGGGCGAACTTACAGCCTGTTGGGGGAAGGGCATATTAGCTTTAGCCGGGATCTGAGAGCGTGCAGACACTACACGGTCGAGACGTAATGGTAGAAAGCAACCAAGGATATGTCTAGGAAAAGAGCCGTGGGAAGAGTTTGGTCCTATCCGACCAATTTATATCGATATTAGGCTGCCGG')