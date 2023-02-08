class Game_status():
    def __init__(self):
        #plansza szachowa 8x8, litery "b" i "w" odpowiadają odpowiednio kolorowi czarnemu i białemu. Duże litery symbolizują figury, a litera "p" pionka. Puste pola oznaczone są "__"
        self.board = [
            ["bR","bN","bB","bQ","bK","bB","bN","bR"],
            ["bp","bp","bp","bp","bp","bp","bp","bp"],
            ["__","__","__","__","__","__","__","__"],
            ["__","__","__","__","__","__","__","__"],
            ["__","__","__","__","__","__","__","__"],
            ["__","__","__","__","__","__","__","__"],
            ["wp","wp","wp","wp","wp","wp","wp","wp"],
            ["wR","wN","wB","wQ","wK","wB","wN","wR"]
        ]
        self.white_To_Move = True
        self.move_Log = []

    class Move():
        ranks_to_rows = {"1":7,"2":6,"3":5,"4":4,"5":3,"6":2,"7":1,"8":0}
        rows_to_ranks = {v: k for k, v in ranks_to_rows.items()}

        files_to_cols = {"a":7,"b":6,"c":5,"d":4,"e":3,"f":2,"g":1,"h":0}
        cols_to_files = {v: k for k, v in files_to_cols.items()}


        def __init__(self,start_squere, stop_squere, board):
            self.start_row = start_squere[0]
            self.start_col = start_squere[1]
            self.stop_row = stop_squere[0]
            self.stop_col  = stop_squere[1]
            self.piece_moved = board[self.start_row][self.start_col]
            self.piece_selected = board[self.stop_row][self.stop_col]

        def Chess_notation(self):
            return self.get_rank_file(self.start_row, self.start_col) + self.get_rank_file(self.start_row, self.stop_col)

        def get_rank_file(self, row, column):
            return self.cols_to_files[column] +self.rows_to_ranks[row]
            