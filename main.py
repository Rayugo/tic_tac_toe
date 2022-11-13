import sys, pygame
from settings import Settings

class TicTacToe():
    def __init__(self):
        pygame.init()
        self.settings = Settings()
        self.width = self.settings.width
        self.height = self.settings.height
        self.one_third_width = self.width // 3
        self.one_third_height = self.height // 3
        self.screen = pygame.display.set_mode(self.settings.size)
        self.screen.fill(self.settings.background_color)
        self.player = True #true represent 'x' and false represent 'o'
        self.positions_taken = []
        self.board = [[0]*3 for i in range(3)]
        self.font = pygame.font.SysFont(self.settings.font, self.settings.font_size)


    def start_game(self):
        self._draw_lines()
        player_x_won, player_o_won = False, False
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONUP:
                    pos = pygame.mouse.get_pos()
                    x = pos[0] - (pos[0] % self.one_third_width)
                    y = pos[1] - (pos[1] % self.one_third_height)
                    if self.player and (x,y) not in self.positions_taken:
                        self._draw_x(x, y)
                        self.positions_taken.append((x,y))
                        self.board[x//self.one_third_width][y//self.one_third_height] = 'x'
                        self.player = False
                        if self.check_win(x//self.one_third_width, y//self.one_third_height, 'x'):
                            player_x_won = True
                        
                    elif (x,y) not in self.positions_taken:
                        self._draw_o(x, y)
                        self.positions_taken.append((x,y))
                        self.board[x//self.one_third_width][y//self.one_third_height] = 'o'
                        self.player = True
                        if self.check_win(x//self.one_third_width, y//self.one_third_height, 'o'):
                            player_o_won = True
                            
            pygame.display.flip()
            if player_x_won or player_o_won or len(self.positions_taken) == 9:
                break

        if player_x_won:
            self._display_endscreen('X')
        elif player_o_won:
            self._display_endscreen('O')
        else:
            self._display_endscreen('REMIS')

    def _draw_lines(self):
        pygame.draw.line(self.screen, (0,0,0), (self.one_third_width, 0), (self.one_third_width, self.height), 4)
        pygame.draw.line(self.screen, (0,0,0), (self.one_third_width * 2, 0), (self.one_third_width * 2, self.height), 4)
        pygame.draw.line(self.screen, (0,0,0), (0, self.one_third_height), (self.width, self.one_third_height), 4)
        pygame.draw.line(self.screen, (0,0,0), (0, self.one_third_height * 2), (self.width, self.one_third_height * 2), 4)
    
    def _draw_x(self, x, y):
        pygame.draw.line(self.screen, self.settings.x_color, (x,y), (x + self.one_third_width, y + self.one_third_height), 5)
        pygame.draw.line(self.screen, self.settings.x_color, (x + self.one_third_width, y), (x, y + self.one_third_height), 5)
    
    def _draw_o(self, x, y):
        pygame.draw.circle(self.screen, self.settings.o_color, (x + self.one_third_width // 2, y + self.one_third_height // 2), self.one_third_width // 2, 4)

    def check_win(self, x, y, player):
        win = False
        for col in range(3):
            if self.board[x][col] == player:
                win = True
            else:
                win = False
                break
        if not win:
            for row in range(3):
                if self.board[row][y] == player:
                    win = True
                else:
                    win = False
                    break
        if not win:
            for diag1 in range(3):
                if self.board[diag1][diag1] == player:
                    win = True
                else:
                    win = False
                    break
        if not win:
            for diag2 in range(3):
                if self.board[diag2][2-diag2] == player:
                    win = True
                else:
                    win = False
                    break
        return win

    def _draw_buttons(self):
        pygame.draw.rect(self.screen, (0,0,0), (100,120,250,100), 2)
        pygame.draw.rect(self.screen, (0,0,0), (100,230,250,100), 2)
        self.screen.blit(self.font.render('PLAY AGAIN', True, (50,205,50)), (110,150))
        self.screen.blit(self.font.render('EXIT', True, (220,20,60)), (180,260))
    
    def _display_endscreen(self, player):
        self.screen.fill((192,192,192))
        self._draw_buttons()
        if player == 'REMIS':
            self.screen.blit(self.font.render(f"DRAW !", True, (255,165,0)), (140,40))
        else:
            self.screen.blit(self.font.render(f"'{player}' WON !", True, (255,165,0)), (140,40))
        pygame.display.flip()
        

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT: 
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONUP:
                    pos = pygame.mouse.get_pos()
                    if pos[0] < 350 and pos[0] > 100 and pos[1] > 120 and pos[1] < 220:
                        self.restart_game()
                    elif pos[0] < 350 and pos[0] > 100 and pos[1] > 230 and pos[1] < 330:
                        sys.exit()
        
    def restart_game(self):
        self.screen.fill(self.settings.background_color)
        self.board = [[0]*3 for i in range(3)]
        self.positions_taken = []
        self.player = True
        self.start_game()


if __name__ == "__main__":
    ttt = TicTacToe()
    ttt.start_game()