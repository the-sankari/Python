# row = []
# for i in range(8):
#     row.append(WHITE_PAWN)
# squares = [x ** 2 for x in range(10)]

# twos = [2 ** i for i in range(8)]

# odds = [x for x in squares if x % 2 != 0 ]

# print(squares)
# print(twos)
# print(odds)

# board = []
EMPTY = "K"
# for i in range(8):
#     row = [EMPTY for i in range(8)]
#     board.append(row)
board = [[EMPTY for i in range(8)] for j in range(8)]
print(board)