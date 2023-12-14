chess = [1, 1, 2, 2, 2, 8]
donghyun_piece = list(input().split())
need_piece = []
for i in range(len(donghyun_piece)):
    donghyun_piece[i] = int(donghyun_piece[i])

    need_piece.append(str(chess[i] - donghyun_piece[i]))
print(' '.join(need_piece))