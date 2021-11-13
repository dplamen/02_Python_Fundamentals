def check_win(m, player):
    won = False
    for i in range(len(m)):
        if m[i] == [player, player, player]:
            won = True
            break
        if m[0][i] == player and m[1][i] == player and m[2][i] == player:
            won = True
            break
    if m[0][0] == player and m[1][1] == player and m[2][2] == player:
        won = True
    if m[0][2] == player and m[1][1] == player and m[2][0] == player:
        won = True
    return won


mat = []
for k in range(3):
    mat.append(input().split())
player1 = check_win(mat, '1')
player2 = check_win(mat, '2')
if player1:
    print('First player won')
elif player2:
    print('Second player won')
else:
    print('Draw!')


