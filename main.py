class Player:
    x = 0
    def getPos(self):
        return self.x
    def setPos(self,newPos):
        self.x = newPos

class Board:
    xDim = 20
    yDim = 6
    board = ['.'*xDim for x in range(yDim)]
    def getY(self):
        return self.yDim
    def getX(self):
        return self.xDim
    def clearBall(self):
        self.board[0:-1] = ['.'*(self.xDim-1) for x in range(self.yDim)]
    def printBoard(self):
        for i in self.board:
            print i
    def updatePlayer(self,playerPos):
        lastLine = ['.']*(self.xDim-1)
        lastLine[playerPos] = 'x'
        lastLine = ''.join(lastLine)
        self.board[-1]=lastLine
    def updateBall(self,ballPos):
        ballx = ballPos[0]
        bally = ballPos[1]
        line = ['.']*(self.xDim-1)
        line[ballx] = 'o'
        line = ''.join(line)
        self.board[bally]=line

class Ball:
    ballx = 1
    bally = 1
    ballDx = 1
    ballDy = 1
    def getPos(self):
        return (self.ballx,self.bally)
    def setPos(self,x,y):
        self.ballx = x
        self.bally = y
    def move(self):
        self.setPos(self.ballx+self.ballDx,self.bally+self.ballDy)
    def setDir(self,dx,dy):
        self.ballDx = dx
        self.ballDy = dy
    def checkWalls(self,board):
        if self.ballx ==0 or self.ballx == board.getX()-2:
            self.setDir(self.ballDx*-1,self.ballDy)
        if self.bally ==0:
            self.setDir(self.ballDx,self.ballDy*-1)
    def checkBottom(self,board,player):
        if self.bally == board.getY() and player.getPos()==(self.ballx):
            self.setDir(self.ballDx,self.ballDy*-1)
            return False
        else:#if the player has failed to hit the ball
            return True
        
player = Player()
board = Board()
ball = Ball()
player.setPos(6)

for i in range(200):
    player.setPos(int(raw_input()))
    ball.checkWalls(board)
    ball.checkBottom(board,player)
    board.clearBall()
    board.updateBall(ball.getPos())
    board.updatePlayer(player.getPos())
    board.printBoard()
    ball.move()
    print "\n"