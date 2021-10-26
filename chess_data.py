# This data contains the board and string data

class ChessBoard:
    def __init__(self):
        # 8 by 8 board that will be used to store the coordinates of the pieces
        #              A  B  C  D  E  F  G  H
        self.board = [[0, 0, 0, 0, 0, 0, 0, 0],  # 8
                      [0, 0, 0, 0, 0, 0, 0, 0],  # 7
                      [0, 0, 0, 0, 0, 0, 0, 0],  # 6
                      [0, 0, 0, 0, 0, 0, 0, 0],  # 5
                      [0, 0, 0, 0, 0, 0, 0, 0],  # 4
                      [0, 0, 0, 0, 0, 0, 0, 0],  # 3
                      [0, 0, 0, 0, 0, 0, 0, 0],  # 2
                      [0, 0, 0, 0, 0, 0, 0, 0]]  # 1

        #  Used for converting the coordinates of the board
        self.board_letters = {'A': 0, 'B': 1, 'C': 2, 'D': 3,
                              'E': 4, 'F': 5, 'G': 6, 'H': 7}

        self.piece_list = []

    def __str__(self):
        board_state = []
        for row in self.board:
            board_state.append(str(row) + "\n")
        return ''.join(board_state)

    # This function takes in a string like "A1" and converts it into
    # coordinates to be used by the array
    def location_conversion(self, location: str) -> list:
        value = []
        if len(location) == 2:
            for spot in location:
                value.append(spot)
            hor = self.board_letters[value[0]]
            vert = 8 - int(value[1])
            return [vert, hor]

    def board_input(self, location: list, obj=None):
        vert = location[0]
        hor = location[1]
        if self.board[vert][hor]:
            self.piece_list.append(self[vert][hor])
        self.board[location[0]][location[1]] = obj
        return self.board[vert][hor]

    def board_get_postion(self, piece: str) -> tuple:
        for vert, data in enumerate(self.board):
            if data.index(piece) == '':
                return vert, data.index(piece)


"""
The goal of this should be too ensure that every piece has an individual id
This makes it so that it is easier to locate the peice within the array and
then manipulate its postion from within the class
"""


class GamePiece:
    def __init__(self, side, identification):
        self.side = side
        self.id = identification


class Pawn(GamePiece):
    id_number = 0

    def __init__(self, side, identification):
        super().__init__(side, identification)
        self.name = 'pawn_'
        Pawn.id_number += 1

    def __str__(self):
        return self.name + str(Pawn.id_number)

    def movement(self):
        if self.side is True:
            initial_position = list(ChessBoard().board_get_position(Pawn.id_number))
            final_position = [initial_position[0] + 1, initial_position[1]]
            ChessBoard().board_input(final_position, Pawn.id_number)

        elif self.side is False:

            initial_position = list(ChessBoard().board_get_position(Pawn.id_number))
            final_position = [initial_position[0] - 1, initial_position[1]]
            ChessBoard().board_input(final_position, Pawn.id_number)


if __name__ == '__main__':
    pass
