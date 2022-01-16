from wsgiref import validate


def all_possible_board_squares():
    output = []
    NUMBERS = [ 8, 7, 6, 5, 4, 3, 2, 1 ]
    LETTERS = [ "a", "b", "c", "d", "e", "f", "g", "h" ]
    for number in NUMBERS:
        for letter in LETTERS:
            output.append(letter + str(number))
    return output

def convert_to_coords(position):
    if (position in all_possible_board_squares()):
        LETTERS = [ "a", "b", "c", "d", "e", "f", "g", "h" ]
        x = (str(LETTERS.index(position[0]) + 1))
        y = position[1]
        return [int(x), int(y)]
    return False

def convert_to_position(coords):
    LETTERS = { 1: "a", 2: "b", 3: "c", 4: "d", 5: "e", 6: "f", 7: "g", 8: "h" }
    try:
        x = LETTERS[coords[0]]
        y = coords[1]
        positon = x + str(y)
        if positon in all_possible_board_squares():
            return positon    
    except:
        pass

class Player:
    def __init__(self, color):
        self.color = color
        self.pieces = []
        self.captured_pieces = []

class Piece:
    def __init__(self, color, title, x, y):
        self.color = color
        self.title = title
        self.coords = [x, y]
        self.position = convert_to_position([self.coords[0], self.coords[1]])
        self.captured = False
        self.moves = 0

    def validate_path(self, position):
        return position in all_possible_board_squares() and (check_if_square_is_occupied(position) == False or (select_piece(position).color != self.color and select_piece(position).title != "King")) 

    def __str__(self):
        return self.color + " " + self.title

class Rook(Piece):
    def __init__(self, color, title, x, y):
        super().__init__(color, title, x, y)
    
    def possible_moves(self):
        output = []
        for i in range(1, 8):
            north = convert_to_position([self.coords[0], self.coords[1] + i])
            if self.validate_path(north) == True:
                output.append(north)
            else:
                break
        for i in range(1, 8):
            south = convert_to_position([self.coords[0], self.coords[1] - i])
            if self.validate_path(south) == True:
                output.append(south)
            else:
                break
        for i in range(1, 8):
            east = convert_to_position([self.coords[0] + i, self.coords[1]])
            if self.validate_path(east) == True:
                output.append(east)
            else:
                break
        for i in range(1, 8):
            west = convert_to_position([self.coords[0] - i, self.coords[1]])
            if self.validate_path(west) == True:
                output.append(west)
            else:
                break
        return output

class Knight(Piece):
    def __init__(self, color, title, x, y):
        super().__init__(color, title, x, y)

    def possible_moves(self):
        output = []
        ene = convert_to_position([self.coords[0] + 2, self.coords[1] + 1])
        ese = convert_to_position([self.coords[0] + 2, self.coords[1] - 1])
        sse = convert_to_position([self.coords[0] + 1, self.coords[1] - 2])
        ssw = convert_to_position([self.coords[0] - 1, self.coords[1] - 2])
        wsw = convert_to_position([self.coords[0] - 2, self.coords[1] - 1])
        wnw = convert_to_position([self.coords[0] - 2, self.coords[1] + 1])
        nnw = convert_to_position([self.coords[0] - 1, self.coords[1] + 2])
        nne = convert_to_position([self.coords[0] + 1, self.coords[1] + 2])
        if self.validate_path(ene):
            output.append(ene)
        if self.validate_path(ese):
            output.append(ese)
        if self.validate_path(sse):
            output.append(sse)
        if self.validate_path(ssw):
            output.append(ssw)
        if self.validate_path(wsw):
            output.append(wsw)
        if self.validate_path(wnw):
            output.append(wnw)
        if self.validate_path(nnw):
            output.append(nnw)
        if self.validate_path(nne):
            output.append(nne)
        return output

class Bishop(Piece):
    def __init__(self, color, title, x, y):
        super().__init__(color, title, x, y)
    
    def possible_moves(self):
        bishop_possible = []
        for i in range(1, 8):
            north_east = convert_to_position([self.coords[0] + i, self.coords[1] + i])
            if self.validate_path(north_east):
                bishop_possible.append(north_east)
            else:
                break
        for i in range(1, 8):
            south_east = convert_to_position([self.coords[0] + i, self.coords[1] - i])
            if self.validate_path(south_east):
                bishop_possible.append(south_east)
            else:
                break
        for i in range(1, 8):
            south_west = convert_to_position([self.coords[0] - i, self.coords[1] - i])
            if self.validate_path(south_west):
                bishop_possible.append(south_west)
            else:
                break
        for i in range(1, 8):
            north_west = convert_to_position([self.coords[0] - i, self.coords[1] + i])
            if self.validate_path(north_west):
                bishop_possible.append(north_west)
            else:
                break
        return bishop_possible


class Queen(Piece):
    def __init__(self, color, title, x, y):
        super().__init__(color, title, x, y)

    def possible_moves(self):
        output = []
        for i in range(1, 8):
            north = convert_to_position([self.coords[0], self.coords[1] + i])
            if self.validate_path(north) == True:
                output.append(north)
            else:
                break
        for i in range(1, 8):            
            south = convert_to_position([self.coords[0], self.coords[1] - i])
            if self.validate_path(south) == True:
                output.append(south)
            else:
                break
        for i in range(1, 8):
            east = convert_to_position([self.coords[0] + i, self.coords[1]])
            if self.validate_path(east) == True:
                output.append(east)
            else:
                break
        for i in range(1, 8): 
            west = convert_to_position([self.coords[0] - i, self.coords[1]])
            if self.validate_path(west) == True:
                output.append(west)
            else:
                break        
        for i in range(1, 8):
            north_east = convert_to_position([self.coords[0] + i, self.coords[1] + i])
            if self.validate_path(north_east) == True:
                output.append(north_east)
            else:
                break
        for i in range(1, 8):
            south_east = convert_to_position([self.coords[0] + i, self.coords[1] - i])
            if self.validate_path(south_east) == True:
                output.append(south_east)
            else:
                break
        for i in range(1, 8):
            south_west = convert_to_position([self.coords[0] - i, self.coords[1] - i])
            if self.validate_path(south_west) == True:
                output.append(south_west)
            else:
                break
        for i in range(1, 8):
            north_west = convert_to_position([self.coords[0] - i, self.coords[1] + i])
            if self.validate_path(north_west) == True:
                output.append(north_west)
            else:
                break
        return output

class King(Piece):
    def __init__(self, color, title, x, y):
        super().__init__(color, title, x, y)

    def possible_moves(self):
        output = []
        north = convert_to_position([self.coords[0], self.coords[1] + 1])
        south = convert_to_position([self.coords[0], self.coords[1] - 1])
        east = convert_to_position([self.coords[0] + 1, self.coords[1]])
        west = convert_to_position([self.coords[0] - 1, self.coords[1]])
        north_east = convert_to_position([self.coords[0] + 1, self.coords[1] + 1])
        south_east = convert_to_position([self.coords[0] + 1, self.coords[1] - 1])
        south_west = convert_to_position([self.coords[0] - 1, self.coords[1] - 1])
        north_west = convert_to_position([self.coords[0] - 1, self.coords[1] + 1])
        if self.validate_path(north):
            output.append(north)
        if self.validate_path(south):
            output.append(south)
        if self.validate_path(east):
            output.append(east)
        if self.validate_path(west):
            output.append(west)
        if self.validate_path(north_east):
            output.append(north_east)
        if self.validate_path(south_east):
            output.append(south_east)
        if self.validate_path(south_west):
            output.append(south_west)
        if self.validate_path(north_west):
            output.append(north_west)
        return output

class WhitePawn(Piece):
    def __init__(self, color, title, x, y):
        super().__init__(color, title, x, y)

    def possible_moves(self):
        output = []
        north = convert_to_position([self.coords[0], self.coords[1] + 1])
        ne = convert_to_position([self.coords[0] + 1, self.coords[1] + 1])
        nw = convert_to_position([self.coords[0] - 1, self.coords[1] + 1])
        if self.moves == 0:
            nn = convert_to_position([self.coords[0], self.coords[1] + 2])
            if nn in all_possible_board_squares() and check_if_square_is_occupied(north) == False and check_if_square_is_occupied(nn) == False:
                output.append(nn)
        if north in all_possible_board_squares() and check_if_square_is_occupied(north) == False:
            output.append(north)
        if ne in all_possible_board_squares() and check_if_square_is_occupied(ne) == True and select_piece(ne).color != "White":
            output.append(ne)
        if nw in all_possible_board_squares() and check_if_square_is_occupied(nw) == True and select_piece(nw).color != "White":
            output.append(nw)
        return output

class BlackPawn(Piece):
    def __init__(self, color, title, x, y):
        super().__init__(color, title, x, y)

    def possible_moves(self):
        output = []
        south = convert_to_position([self.coords[0], self.coords[1] - 1])
        se = convert_to_position([self.coords[0] + 1, self.coords[1] - 1])
        sw = convert_to_position([self.coords[0] - 1, self.coords[1] - 1])
        if self.moves == 0:
            ss = convert_to_position([self.coords[0], self.coords[1] - 2])
            if ss in all_possible_board_squares() and check_if_square_is_occupied(south) == False and check_if_square_is_occupied(ss) == False:
                output.append(ss)
        if south in all_possible_board_squares() and check_if_square_is_occupied(south) == False:
            output.append(south)
        if se in all_possible_board_squares() and check_if_square_is_occupied(se) == True and select_piece(se).color != "Black":
            output.append(se)
        if sw in all_possible_board_squares() and check_if_square_is_occupied(se) == True and select_piece(sw).color != "Black":
            output.append(sw)
        return output

class Game:
    def __init__(self): 
        self.board = {}
        for square in all_possible_board_squares():
            self.board[square] = None
        self.moves = 0
        self.player1 = Player("White")
        self.player2 = Player("Black")

def add_black_ranks():
    BLACK_TITLES = [
        0,
        Rook("Black", "Rook", 1, 8),
        Knight("Black", "Knight", 2, 8,),
        Bishop("Black", "Bishop", 3, 8,),
        Queen("Black", "Queen", 4, 8),
        King("Black", "King", 5, 8,),
        Bishop("Black", "Bishop", 6, 8,),
        Knight("Black", "Knight", 7, 8,),
        Rook("Black", "Rook", 8, 8,)
    ]
    for i in range(1, 9):
        POSITIONS = [0, "a8", "b8", "c8", "d8", "e8", "f8", "g8", "h8"]
        GAME.board[POSITIONS[i]] = BLACK_TITLES[i]
        GAME.player2.pieces.append(BLACK_TITLES[i])

def add_black_pawns():
    for i in range(1, 9):
        POSITIONS = [0, "a7", "b7", "c7", "d7", "e7", "f7", "g7", "h7"]
        pawn = BlackPawn("Black", "Pawn", i, 7)
        GAME.board[POSITIONS[i]] = pawn
        GAME.player2.pieces.append(pawn)

def add_white_ranks():
    WHITE_TITLES = [
        0,
        Rook("White", "Rook", 1, 1),
        Knight("White", "Knight", 2, 1),
        Bishop("White", "Bishop", 3, 1),
        Queen("White", "Queen", 4, 1),
        King("White", "King", 5, 1),
        Bishop("White", "Bishop", 6, 1),
        Knight("White", "Knight", 7, 1),
        Rook("White", "Rook", 8, 1)
    ]
    for i in range(1, 9):
        POSITIONS = [0, "a1", "b1", "c1", "d1", "e1", "f1", "g1", "h1"]
        GAME.board[POSITIONS[i]] = WHITE_TITLES[i]
        GAME.player1.pieces.append(WHITE_TITLES[i])

def add_white_pawns():
    for i in range(1, 9):
        POSITIONS = [0, "a2", "b2", "c2", "d2", "e2", "f2", "g2", "h2"]
        pawn = WhitePawn("White", "Pawn", i, 2)
        GAME.board[POSITIONS[i]] = pawn
        GAME.player1.pieces.append(pawn)

def put_pieces_on_board():
    add_black_pawns()
    add_black_ranks()
    add_white_pawns()
    add_white_ranks()
    
def select_piece(position):
    if position in all_possible_board_squares():
        return GAME.board[position]
    else:
        return "Something went wrong"

def check_if_square_is_occupied(check):
    if check in all_possible_board_squares():
        if select_piece(check) != None: 
            return True
        return False
    else:
        return "Something went wrong"

def get_all_positions_by_color(color):
    output = []
    for square in all_possible_board_squares():
        piece = select_piece(square)
        if piece != None and piece.color == color:
            output.append(square)
    return output

def general_check_all_moves_by_piece():
    for position in all_possible_board_squares():
        if check_if_square_is_occupied(position) == True:
            piece = select_piece(position)
            print(piece, piece.possible_moves())

def get_pieces_that_have_moves():
    output = []
    for position in all_possible_board_squares():
        if check_if_square_is_occupied(position) == True and len(select_piece(position).possible_moves()) != 0:
            output.append({position: len(select_piece(position).possible_moves())})
    return output
            
"""take the board out of the box and place it on the table"""
GAME = Game()

"""take the pieces out of the bags and place them 
    at their initial positions on the board"""
put_pieces_on_board()

"""APPLICATION"""

# Idea to use possible moves to generate a menu and then use text descriptions of what happened
# For example, "Black Rook captures White Queen" or "Black Rook moves to d5"
