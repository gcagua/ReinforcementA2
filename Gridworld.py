class Gridworld:

    def __init__(self, dimensions = 10):
        self.dimensions = dimensions
        self.board = [['' for i in range (0, dimensions)] for j in range(0, dimensions)]
        self.current_state = (0,0)

        ## en qué momento se llenan las casillas con *, 0, 1, -1
        self.board[2][1] = '*'
        self.board[2][2] = '*'
        self.board[2][3] = '*'
        self.board[2][4] = '*'
        self.board[2][6] = '*'
        self.board[2][7] = '*'
        self.board[2][8] = '*'
        self.board[3][4] = '*'
        self.board[4][4] = '*'
        self.board[5][4] = '*'
        self.board[6][4] = '*'
        self.board[7][4] = '*'

        self.board[4][5] = -1
        self.board[7][5] = -1
        self.board[7][6] = -1
        self.board[5][5] = 1

    def get_current_state(self):
        return self.current_state

    def get_posible_actions(self, i, j):

        states = []
        if i != 0 and self.board[i-1][j] != '*':
            states.append('up')
        if i != self.dimensions and self.board[i+1][j] != '*':
            states.append('down')
        if j != 0 and self.board[i][j-1] != '*':
            states.append('left')
        if j != self.dimensions and self.board[i][j+1] != '*':
            states.append('right')
        
        return states

    def do_action(self, action):

        if action == 'up':
            self.current_state = (self.current_state[0]-1, self.current_state[1])
        elif action == 'down':
            self.current_state = (self.current_state[0]+1, self.current_state[1])
        elif action == 'left':
            self.current_state = (self.current_state[0], self.current_state[1]-1)
        elif action == 'right':
            self.current_state = (self.current_state[0], self.current_state[1]+1)

        self.board[self.current_state[0]][self.current_state[1]] = 'x'
        return (self.board[self.current_state[0]][self.current_state[1]], (self.current_state[0], self.current_state[1]))

    def reset(self):
        self.current_state = (0,0)
    
    def is_terminal(self):
        return True if self.board[self.current_state[0], self.current_state[1]] == 1 else False
    
grid = Gridworld()
print(grid.get_posible_actions(grid.get_current_state()[0],grid.get_current_state()[1]))
print(grid.do_action('down'))
print(grid.get_posible_actions(grid.get_current_state()[0],grid.get_current_state()[1]))
print(grid.do_action('right'))
print(grid.get_posible_actions(grid.get_current_state()[0],grid.get_current_state()[1]))
print(grid.do_action('right'))

