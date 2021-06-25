import copy
import random
import time


class c4 :
    board = []
    winner=0
    pause=True
    xs=-10
    ys=-10
    xe=-10
    ye=-10    

    def __init__(self) :
        for y in range(6):
            self.board.append([])
            for x in range(7):
                self.board[y].append(0)
    def reset(self):
        for y in range(6):
            for x in range(7):
                self.board[y][x]=0
        self.winner=0
        self.pause=True       

    def add(self, x, player):
        for y in range(6):
            if self.board[y][x] == 0:
                self.board[y][x] = player
                break
        
    def check_win(self, player):
        flag = 0
    

        for y in range(3):
            for x in range(7):
                if (self.board[y][x] == player and self.board[y + 1][x] == player and self.board[y + 2][x] == player and self.board[y + 3][x] == player):
                    self.winner=player
                    self.xs=x
                    self.ys=y
                    self.xe=x
                    self.ye=y+3
                    break
            for y in range(6):
                for x in range(4):
                    if (self.board[y][x] == player and self.board[y][x + 1] == player and self.board[y][x + 2] == player and self.board[y][x + 3] == player):
                        self.winner=player
                        self.xs=x
                        self.ys=y
                        self.xe=x+3
                        self.ye=y
                        break
            for y in range(3):
                for x in range(4):
                    if (self.board[y][x] == player and self.board[y + 1][x + 1] == player and self.board[y + 2][x + 2] == player and self.board[y + 3][x + 3] == player):
                        self.winner=player
                        self.xs=x
                        self.ys=y
                        self.xe=x+3
                        self.ye=y+3
                        break
            for y in range(3):
                for x in range(3, 7):
                    if (self.board[y][x] == player and self.board[y + 1][x - 1] == player and self.board[y + 2][x - 2] == player and self.board[y + 3][x - 3] == player):
                        self.winner=player
                        self.xs=x
                        self.ys=y
                        self.xe=x-3
                        self.ye=y+3
                        break
                    
            if self.winner==0:
                for x in range(7):
                    flag += int(abs(self.board[5][x]))
                if flag == 7:
                    self.winner=-999
                    
                    
        
        return self.winner
            
    def draw_board(self):
        background(120)        
        noStroke()
        strokeWeight(1)
        for x in range(7):
            #line(width / 7 * x, 0, width / 7 * x, height)
            for y in range(6):
                if self.board[y][x] == 1:
                    fill(255)
                elif self.board[y][x] == -1:
                    fill(0)
                else:
                    fill(130)
                    noStroke()
                ellipse(width / 7 * (x + 0.5), height - height /6 * (y + 0.5), width / 7, height / 6) 
        if self.winner !=0 and self.winner !=-999  :
            stroke(100)
            strokeWeight(10)
            line(width/7*(self.xs+0.5), (height-height/6*(self.ys+0.5)),width/7*(self.xe+0.5), height-height/6*(self.ye+0.5))
                
    def random_AI(self, player):
        board_org = copy.deepcopy(self.board)
        flag=True    
        for x in range(7):
            if self.board[5][x] == 0:
                self.add(x, player)
                if(self.check_win(player)== player):
                    flag=False
                    break
                else:
                    self.board = copy.deepcopy(board_org)
        if flag :
            for x in range(7):
                if self.board[5][x] == 0:
                    self.add(x, -1*player)
                    if(self.check_win(-1*player)== -1*player):
                        self.board = copy.deepcopy(board_org)
                        self.add(x, player)
                        self.winner=0
                        flag=False
                        break
                    else:
                        self.board = copy.deepcopy(board_org)        
            
        
        if flag:
            possible=range(7)
            for x in range(7) :
                if self.board[5][x] != 0 :
                     possible.remove(x)
                else:
                    for x2 in range(7) :
                        self.add(x, player)
                        self.add(x2, -1*player)
                        if(self.check_win(-1*player)== -1*player):
                            possible.remove(x)
                            self.winner==0
                            self.board = copy.deepcopy(board_org)
                            break
                        self.board = copy.deepcopy(board_org)
            self.board = copy.deepcopy(board_org)
            
            
            if len(possible)==0 :
                possible=range(7)

        while flag :
            print(possible)
            
            x = random.choice(possible)
            if self.board[5][x] == 0:
                self.add(x, player)
                break

Game=c4()
mode = 0
#mode = 1

player=1



def mouseReleased():
    global Game
    if Game.winner !=0 :
        print(Game.winner)
        exit()
    else :
        if Game.pause:
            x=int(mouseX / (width / 7.))
            if Game.board[5][x]==0:
                Game.add(x, player)
                Game.pause=False        
                loop()
                return False
        return True
    
def setup():
    size(350, 300)
   #frameRate(2)

def draw():
    noStroke()
    global Game
    global player
    if player == 1:
        Game.random_AI(player)
    elif player == -1:
        if mode==0 :
            Game.random_AI(player)
        elif mode==1  :
            mouseReleased() 
            Game.pause=True

    Game.winner=0
    Game.check_win(player)         
    print(Game.board,Game.winner)
    if Game.winner !=0:
        Game.draw_board()
        noLoop()
    elif player == 1 :
        player = -1
        if mode==1 :
            noLoop()
    elif player==-1:
        player=1
    Game.draw_board()
