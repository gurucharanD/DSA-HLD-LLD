class TicTacToe:

    def __init__(self, n: int):
        
        self.rows = [0]*n
        self.cols = [0]*n
        self.lr = 0
        self.rl = 0
        self.n = n
        

    def move(self, row: int, col: int, player: int) -> int:
        
        if player == 1:
            if row - col == 0:
                self.lr+=1
            if row+col == self.n - 1:
                self.rl+=1
            
            self.rows[row]+=1
            self.cols[col]+=1
            
            if self.rows[row] == self.n or self.cols[col] == self.n or self.rl == self.n or self.lr == self.n:
                return 1
            
        else:
            
            if row - col == 0:
                self.lr-=1
            if row+col == self.n - 1:
                self.rl-=1
            
            self.rows[row]-=1
            self.cols[col]-=1
            
            if self.rows[row] == -self.n or self.cols[col] == -self.n or self.rl == -self.n or self.lr == -self.n:
                return 2
        
        
        return 0
        

# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)