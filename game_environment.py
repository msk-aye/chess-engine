from abc import ABC, abstractmethod

# Constants
PAWN = "P"
KNIGHT = "N"
BISHOP = "B"
ROOK = "R"
QUEEN = "Q"
KING = "K"

class Piece(ABC):
    def __init__(self, position: tuple, white: bool, board):
        self.position = position
        self.rank = 8 - position[0]
        self.file = position[1] + 1
        self.white = white
        self.update_moves = False
        self.moves = []
        self.board = board

    @abstractmethod
    def __repr__(self):
        pass

    @abstractmethod
    def __str__(self):
        pass

    def get_position(self) -> tuple:
        return self.position

    def set_position(self, position: tuple):
        self.position = position
        self.rank = position[0]
        self.file = position[1]
        self.update_moves = True

    def is_white(self) -> bool:
        return self.white

    @abstractmethod
    def get_moves(self) -> list:
        pass

class Pawn(Piece):
    def __init__(self, position: tuple, white: bool):
        super().__init__(position, white)
        self.update_moves = True

    def __repr__(self):
        return PAWN

    def __str__(self):
        return PAWN

    def get_moves(self):
        if self.update_moves:
            self.moves = []

            if self.white:
                if self.rank == 1:
                    self.moves.append((self.rank + 2, self.file))
                self.moves.append((self.rank + 1, self.file))
                if self.board.get_piece_at((self.rank + 1, self.file + 1)) and not self.board.get_piece_at((self.rank + 1, self.file + 1)).is_white():
                    self.moves.append((self.rank + 1, self.file + 1))
                if self.board.get_piece_at((self.rank + 1, self.file - 1)) and not self.board.get_piece_at((self.rank + 1, self.file - 1)).is_white():
                    self.moves.append((self.rank + 1, self.file - 1))

            else:
                if self.rank == 6:
                    self.moves.append((self.rank - 2, self.file))
                self.moves.append((self.position[0] - 1, self.position[1]))

            self.update_moves = False

        return self.moves

class Knight(Piece):
    pass

class Bishop(Piece):
    pass

class Rook(Piece):
    pass

class Queen(Piece):
    pass

class King(Piece):
    pass

class Board:
    def __init__(self):
        self.board = [[None for i in range(8)] for j in range(8)]

    def get_piece_at(self, position: tuple) -> Piece:
        if position[0] < 0 or position[0] > 7 or position[1] < 0 or position[1] > 7:
            return None

        return self.board[position[0]][position[1]]

    def set_piece_at(self, position: tuple, piece: Piece):
        self.board[position[0]][position[1]] = piece

    def get_board(self) -> list:
        return self.board

    def print_board(self) -> None:
        for i in range(8):
            for j in range(8):
                if self.board[i][j] is None:
                    print(" ", end=" ")
                else:
                    print(self.board[i][j], end=" ")
            print()

    def chess_notation(self, position: tuple) -> str:
        return chr(position[1] + 97) + str(8 - position[0])

    def algebraic_notation(self, position: str) -> tuple:
        return (8 - int(position[1]), ord(position[0]) - 97)

class GameEnvironment:
    def __init__(self):
        self.board = Board()

    def get_board(self):
        return self.board

    def get_pieces(self):
        return self.pieces

    def get_moves(self, piece):
        return piece.moves()

    def get_piece_at(self, position):
        return self.board.get_piece_at(position)
