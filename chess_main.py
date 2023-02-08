import pygame as pg
import engine

width = height = 512
dimension = 8
squere_size = height//dimension
fps = 60
images = {}

def Load_Images(): #ładowanie grafik figur i pionków
    pieces = ["bR","bN","bB","bQ","bK","bB","bN","bR","bp","wp","wR","wN","wB","wQ","wK","wB","wN","wR"]
    for piece in pieces:
        images[piece] = pg.transform.scale(pg.image.load("images/"+piece+".png"),(squere_size, squere_size))

def Main(): # odpalanie gry
    pg.init()
    window = pg.display.set_mode((width,height))
    clock = pg.time.Clock()
    window.fill(pg.Color("white"))
    gs = engine.Game_status()
    Load_Images()
    squere_selected = () #wybór pola
    player_clicks = [] #zapisywanie wyborów gracza
    run = True
    while run:
        for _ in pg.event.get():
            if _.type == pg.QUIT:
                run = False
            elif _.type == pg.MOUSEBUTTONDOWN:
                location = pg.mouse.get_pos()
                mouse_col = [0]// squere_size
                mouse_row = [1]// squere_size
                if squere_selected == (mouse_row, mouse_col): #sprawdzanie czy gracz nie kliknął drugi raz tego samego pola
                    squere_selected = () #odkliknięcie 
                    player_clicks = []
                else:
                    squere_selected = (mouse_row, mouse_col)
                    player_clicks.append(squere_selected)

                if len(player_clicks) == 2:
                    move = engine.Move(player_clicks[0], player_clicks[1], gs.board)

        Draw_board(window,gs)
        clock.tick(fps)
        pg.display.flip()

def Draw_board(window,gs):
    Draw_squeres(window)
    Draw_pieces(window, gs.board)

def Draw_squeres(window):
    colors = [pg.Color("white"), pg.Color("dark gray")]
    for row in range(dimension):
        for column in range(dimension):
            color = colors[((row + column) % 2)]
            pg.draw.rect(window, color, pg.Rect(column*squere_size, row*squere_size, squere_size,squere_size))

def Draw_pieces(window, board):
    for row in range(dimension):
        for column in range(dimension):
            piece = board[row][column]
            if piece != "__":
                window.blit(images[piece],pg.Rect(column*squere_size, row*squere_size, squere_size,squere_size))




Main()