"""
This function declares the ChessBoard class
This class is meant to hold the positions of all the pieces on the board
This board has methods for multiple things:
        - returning the state of the board
        - inputting the selected piece into the proper spot
        - returning the spot of a particular piece
        - storing overwritten pieces into a list of taken pieces
"""


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

        # Used for storing the pieces that are overridden by move commands
        self.piece_list = []

    def __str__(self):
        board_state = []
        for row in self.board:
            board_state.append(str(row) + "\n")
        return ''.join(board_state)

    def board_input(self, location: list, obj):
        if len(location) == 2:
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

    # The following 2 functions are staticmethods
    # This is because they should serve as standalone functions that come
    # with the class during the import rather than relying on the class
    @staticmethod
    def location_letter_conversion(location: str) -> list:
        value = []
        conversion_symbols = {'A': 0, 'B': 1, 'C': 2, 'D': 3,
                              'E': 4, 'F': 5, 'G': 6, 'H': 7}
        if len(location) == 2:
            for spot in location:
                value.append(spot)
            hor = conversion_symbols[value[0]]
            vert = 8 - int(value[1])
            return [vert, hor]

    @staticmethod
    def location_array_conversion(location: list) -> str:
        value = []
        conversion_symbols = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
        if len(location) == 2:
            for spot in location:
                value.append(spot)
            hor = conversion_symbols[value[0]]
            ver = 8 - value[1]
            return hor + str(ver)


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
    # This is used for the creation of a unique ID for the pieces
    id_number = 0

    def __init__(self, side, identification):
        super().__init__(side, identification)

        # These lines are used for creating a unique ID for each piece
        # upon every intialization of the class
        piece_name = 'pawn_'
        Pawn.id_number += 1
        self.name = piece_name + str(Pawn.id_number)

    def __str__(self):
        return self.name

        # double move and diagonal move need to be implemented
    def forward_movement(self):
        if self.side is True:
            ipos = list(ChessBoard().board_get_position(self.name))
            fpos = [ipos[0] + 1, ipos[1]]
            ChessBoard().board_input(fpos, self.name)
            return f'{self.name} was inserted at {fpos}'

        elif self.side is False:
            ipos = list(ChessBoard().board_get_position(self.name))
            fpos = [ipos[0] - 1, ipos[1]]
            ChessBoard().board_input(fpos, self.name)

    def diagonal_movement(self):
        pass


if __name__ == '__main__':
    pass
