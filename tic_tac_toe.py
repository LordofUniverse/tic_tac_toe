class Board:
    def __init__(self):
        self._board = True
        self.player = 'x'
        self.posx = []
        self.poso = []
        self.bw = ' | '
        self.two_bw = '\n--- --- ---\n'
        self.all_bw = '\n' + '-'*100
        print('It is a two player game..')
        print('player1 is "x" ')

    def start(self):
        pass

    def update(self):
        print('updating... \n')
        if self.player == 'x':
            while True: 
                inp = input('type x pos and y pos(as numbers - for example, 2 3 ) relative to top of board to enter: ').split(' ')
                if (inp in self.posx) or (inp in self.poso):
                    print('cant replace number, try again..')
                elif int(inp[0]) > 3 or int(inp[0]) < 1 or int(inp[1]) < 1 or int(inp[1]) > 3:
                    print('number out of range limit, try again between 1 and 3..')
                else:
                    self.posx.append(inp)
                    break
            self.player = 'y'
        else:
            while True: 
                inp = input('type x pos and y pos(as numbers - for example, 2 3 ) relative to top of board to enter: ').split(' ')
                if (inp in self.posx) or (inp in self.poso):
                    print('cant replace number, try again..')
                elif int(inp[0]) > 3 or int(inp[0]) < 1 or int(inp[1]) < 1 or int(inp[1]) > 3:
                    print('number out of range limit, try again between 1 and 3..')
                else:
                    self.poso.append(inp)
                    break
            self.player = 'x'
        self.print(self.posx, self.poso)

    def win(self, pos):
        if (['1', '1'] in pos and ['1', '2'] in pos and ['1', '3'] in pos) or (['2', '1'] in pos and ['2', '2'] in pos and ['2', '3'] in pos) or (['3', '1'] in pos and ['3', '2'] in pos and ['3', '3'] in pos) or (['1', '1'] in pos and ['2', '1'] in pos and ['3', '1'] in pos) or (['1', '2'] in pos and ['2', '2'] in pos and ['3', '2'] in pos) or (['1', '3'] in pos and ['2', '3'] in pos and ['3', '3'] in pos) or (['1', '1'] in pos and ['2', '2'] in pos and ['3', '3'] in pos) or (['3', '1'] in pos and ['2', '2'] in pos and ['1', '3'] in pos):
            return 'win'
        else: 
            return '.'
        
    def print(self, posx, poso):
        final = ''
        for i in range(1, 4):
            for j in range(1, 4):
                if [str(j), str(i)] in posx:
                    final += 'x' + self.bw
                elif [str(j), str(i)] in poso:
                    final += 'o' + self.bw
                else:
                    final += ' ' + self.bw
            final += self.two_bw
        final += self.all_bw
        print(final)

        wino = self.win(poso)
        winx = self.win(posx)

        if wino == 'win':
            print('\n \n \n "o" has won the game \n \n \n ')
            self._board = False

        elif winx == 'win':
            print('\n \n \n "x" has won the game \n \n \n ')
            self._board = False

board = Board()
board.start()

while (board._board):
    board.update()
