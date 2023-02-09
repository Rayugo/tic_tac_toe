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
        self.screen = pygame.display.set_mode(self.settings.initial_size, pygame.RESIZABLE)
        self.player = True #true represent 'x' and false represent 'o'
        self.field_taken = 0
        self.board = [[0]*3 for i in range(3)]
        self.font = pygame.font.SysFont(self.settings.font, self.settings.font_size)


    def start_game(self):
        self.screen.fill(self.settings.background_color)
        self._draw_lines()
        player_x_won, player_o_won = False, False
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.VIDEORESIZE:
                    #old_screen = self.screen
                    self.screen = pygame.display.set_mode((event.w, event.h), pygame.RESIZABLE)
                    self._update_game_screen()
                    #self.screen.blit(old_screen, (0,0))
                    #del old_screen

                elif event.type == pygame.MOUSEBUTTONUP:
                    pos = pygame.mouse.get_pos()
                    #x = pos[0] - (pos[0] % (self.screen.get_width()//3))
                    #y = pos[1] - (pos[1] % (self.screen.get_height()//3))

                    if pos[0] < self.screen.get_width()//3:
                        y = 0
                    elif pos[0] < (self.screen.get_width()//3) * 2:
                        y = 1
                    else:
                        y = 2
                    
                    if pos[1] < self.screen.get_height()//3:
                        x = 0
                    elif pos[1] < (self.screen.get_height()//3) * 2:
                        x = 1
                    else:
                        x = 2

                    print(x, y)
                    if self.player and not self.board[x][y]:
                        self._draw_x(y, x)
                        #self.positions_taken.append((x,y))
                        self.field_taken = self.field_taken + 1
                        self.board[x][y] = 'x'
                        self.player = False
                        if self.check_win(x, y, 'x'):
                            player_x_won = True
                        
                    elif not self.board[x][y]:
                        self._draw_o(y, x)
                        #self.positions_taken.append((x,y))
                        self.field_taken = self.field_taken + 1
                        self.board[x][y] = 'o'
                        self.player = True
                        if self.check_win(x, y, 'o'):
                            player_o_won = True
                            
            pygame.display.flip()
            
            if player_x_won or player_o_won or self.field_taken == 9:
                break

        if player_x_won:
            self._endscreen('X')
        elif player_o_won:
            self._endscreen('O')
        else:
            self._endscreen('DRAW')

    def _draw_lines(self):
        pygame.draw.line(self.screen, (0,0,0), (self.screen.get_width()//3, 0), (self.screen.get_width()//3, self.screen.get_height()), 4)
        pygame.draw.line(self.screen, (0,0,0), (self.screen.get_width()//3 * 2, 0), (self.screen.get_width()//3 * 2, self.screen.get_height()), 4)
        pygame.draw.line(self.screen, (0,0,0), (0, self.screen.get_height()//3), (self.screen.get_width(), self.screen.get_height()//3), 4)
        pygame.draw.line(self.screen, (0,0,0), (0, (self.screen.get_height()//3) * 2), (self.screen.get_width(), (self.screen.get_height()//3) * 2), 4)
    
    def _draw_x(self, x, y):
        print("X: ", x, y)
        pygame.draw.line(self.screen, self.settings.x_color, (x * self.one_third_width, y * self.one_third_height), ((x + 1) * self.one_third_width, (y + 1) * self.one_third_height), 5)
        pygame.draw.line(self.screen, self.settings.x_color, ((x + 1) * self.one_third_width, y * self.one_third_height), (x * self.one_third_width, (y + 1) * self.one_third_height), 5)
    
    def _draw_o(self, x, y):
        pygame.draw.ellipse(self.screen, self.settings.o_color, (x * self.one_third_width, y * self.one_third_height, self.one_third_width, self.one_third_height), 5)

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

    def _update_game_screen(self):
        #print("DZIALA")
        
        self.one_third_width = self.screen.get_width() // 3
        self.one_third_height = self.screen.get_height() // 3
        self.screen.fill(self.settings.background_color)
        self._draw_lines()
        for x,i in enumerate(self.board):
            for y,j in enumerate(i):
                if j == 'x':
                    self._draw_x(y, x)
                elif j == 'o':
                    self._draw_o(y, x)


    def _display_buttons(self):
        #pygame.draw.rect(self.screen, (0,0,0), (100,120,250,100), 2)
        #pygame.draw.rect(self.screen, (0,0,0), (100,230,250,100), 2)
        pygame.draw.rect(self.screen, (0,0,0), (self.one_third_width//2, self.one_third_height//2, self.one_third_width*2, self.one_third_height), 2)
        pygame.draw.rect(self.screen, (0,0,0), (self.one_third_width//2, self.one_third_height*1.5 + 20, self.one_third_width*2, self.one_third_height), 2)
        play_again_text = self.font.render('PLAY AGAIN', True, (50,205,50))
        play_again_rect = play_again_text.get_rect(center=(1.5*self.one_third_width, self.one_third_height))
        self.screen.blit(play_again_text, play_again_rect)
        exit_text = self.font.render('EXIT', True, (220,20,60))
        exit_rect = exit_text.get_rect(center=(1.5*self.one_third_width, 2*self.one_third_height+20))
        self.screen.blit(exit_text, exit_rect)
    
    def _display_result(self, result):
        if result == 'DRAW':
            draw_text = self.font.render(f"DRAW !", True, (255,165,0))
            draw_rect = draw_text.get_rext(center=(1.5*self.one_third_width, self.one_third_height//2 - 30))
            self.screen.blit(draw_text, draw_rect)
        else:
            winner_text = self.font.render(f"'{result}' WON !", True, (255,165,0))
            winner_rect = winner_text.get_rect(center=(1.5*self.one_third_width, self.one_third_height//2 - 30))
            self.screen.blit(winner_text, winner_rect)

    def _display_endscreen(self, result):
        self.one_third_width = self.screen.get_width() // 3
        self.one_third_height = self.screen.get_height() // 3
        self.screen.fill(self.settings.background_color)
        self._display_buttons()
        self._display_result(result)
        pygame.display.flip()
    
    def _endscreen(self, result):
        self._display_endscreen(result)
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT: 
                    sys.exit()
                elif event.type == pygame.VIDEORESIZE:
                    #old_screen = self.screen
                    self.screen = pygame.display.set_mode((event.w, event.h), pygame.RESIZABLE)
                    self._display_endscreen(result)
                    #self.screen.blit(old_screen, (0,0))
                    #del old_screen
                elif event.type == pygame.MOUSEBUTTONUP:
                    pos = pygame.mouse.get_pos()
                    if (pos[0] < self.one_third_width//2 + self.one_third_width*2) and (pos[0] > self.one_third_width//2) and (pos[1] > self.one_third_height//2) and (pos[1] < self.one_third_height//2 + self.one_third_height):
                        self.restart_game()
                    elif (pos[0] < self.one_third_width//2 + self.one_third_width*2) and (pos[0] > self.one_third_width//2) and (pos[1] > self.one_third_height*1.5 + 20) and (pos[1] < self.one_third_height*1.5 + 20 + self.one_third_height):
                        sys.exit()
        
    def restart_game(self):
        self.screen.fill(self.settings.background_color)
        self.board = [[0]*3 for i in range(3)]
        self.field_taken = 0
        self.player = True
        self.start_game()


if __name__ == "__main__":
    ttt = TicTacToe()
    ttt.start_game()