def main():
    game = [[0, 1, 2],
            [1, 1, 2],
            [2, 1, 1]]
    isWinner = False
    # check every col and every row
    for i in range(3):
        if check_col(i, game):
            print(str(game[0][i]) + " won the game")
            isWinner = True
            break
        if check_row(i, game):
            print(str(game[i][0]) + " won the game")
            isWinner = True
            break
    if check_diags(game) != False:
        print(str(check_diags(game)) + " is the winner of the game")
        isWinner = True
    if isWinner == False:
        print("Its a tie!")
    pass


# check one row by index
def check_row(rowNum, mat):
    row = mat[rowNum]
    first = row[0]

    for col in row:
        if first != col:
            return False
    return True
    pass


# check one col by index
def check_col(colNum, mat):
    first = mat[0][colNum]

    for row in range(3):
        if first != mat[row][colNum]:
            return False
    return True
    pass


# check both diagonals
def check_diags(mat):
    firstDiag1 = mat[0][2]
    winner = firstDiag1
    for i in range(3):
        if firstDiag1 != mat[i][2 - i]:
            winner = False
            break
    if winner != False:
        return winner

    firstDiag2 = mat[0][0]
    winner = firstDiag2
    for i in range(3):
        if firstDiag2 != mat[i][i]:
            winner = False
            break
    return winner
    pass


if __name__ == '__main__':
    main()
