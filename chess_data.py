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

        self.board_letters = {'A': 0, 'B': 1, 'C': 2, 'D': 3,
                              'E': 4, 'F': 5, 'G': 6, 'H': 7}

        self.piece_list = []

    # This function takes in a string like "A1" and converts it into
    # coordinates to be used by the array
    def location_conversion(self, location: str) -> list:
        value = []
        if len(location) == 2:
            for spot in location:
                value.append(spot)
            hor_location = self.board_letters[value[0]]
            vert_location = 8 - int(value[1])
            return [vert_location, hor_location]

    def board_input(self, location: list, obj=None):
        vert = location[0]
        hor = location[1]
        if self.board[vert][hor]:
            self.piece_list.append(self[vert][hor])
        self.board[location[0]][location[1]] = obj

    def board_output(self, location: str):
        vert = location[0]
        hor = location[1]
        return self.board[vert][hor]


if __name__ == '__main__':
    pass
