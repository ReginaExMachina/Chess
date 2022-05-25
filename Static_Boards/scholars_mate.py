import chess

board = chess.Board()

board.push_san("e4")
board.push_san("e5")
board.push_san("Qh5")
board.push_san("Nc6")
board.push_san("Bc4")
board.push_san("Nf6")
board.push_san("Qxf7")

print(board)

print("\n" + "Is this checkmate?")
print(board.is_checkmate())
