import random
import pygame
pygame.init()

# 窗口大小和方格大小
WINDOW_WIDTH, WINDOW_HEIGHT = 300, 600
BLOCK_SIZE = 30

# 方块类型和颜色
SHAPE_TYPES = ['I', 'J', 'L', 'O', 'S', 'T', 'Z']
SHAPE_COLORS = {
    'I': (0, 255, 255),
    'J': (0, 0, 255),
    'L': (255, 165, 0),
    'O': (255, 255, 0),
    'S': (0, 255, 0),
    'T': (128, 0, 128),
    'Z': (255, 0, 0)
}

class Block:
    def __init__(self):
        self.x, self.y = WINDOW_WIDTH // 2 - BLOCK_SIZE * 2, 0
        self.shape_type = random.choice(SHAPE_TYPES)
        self.color = SHAPE_COLORS[self.shape_type]
        self.shape = self.get_shape(self.shape_type)
    
    # 根据方块类型获取方块形状
    def get_shape(self, shape_type):
        if shape_type == 'I':
            return [(0, -1), (0, 0), (0, 1), (0, 2)]
        elif shape_type == 'J':
            return [(-1, 0), (0, 0), (0, 1), (0, 2)]
        elif shape_type == 'L':
            return [(0, 0), (0, 1), (0, 2), (1, 2)]
        elif shape_type == 'O':
            return [(0, 0), (0, 1), (1, 0), (1, 1)]
        elif shape_type == 'S':
            return [(0, 0), (0, 1), (1, -1), (1, 0)]
        elif shape_type == 'T':
            return [(0, 0), (1, 0), (1, 1), (2, 0)]
        elif shape_type == 'Z':
            return [(0, -1), (0, 0), (1, 0), (1, 1)]
    
    # 向下移动方块
    def move_down(self):
        self.y += BLOCK_SIZE
    
    # 向左移动方块
    def move_left(self):
        self.x -= BLOCK_SIZE
    
    # 向右移动方块
    def move_right(self):
        self.x += BLOCK_SIZE
    
    # 旋转方块
    def rotate(self):
        new_shape = []
        for i in range(len(self.shape)):
            x, y = self.shape[i]
            new_shape.append((y, -x))
        self.shape = new_shape
    
    # 获取方块当前在网格中的位置
    def get_grid_position(self):
        grid_x = (self.x + BLOCK_SIZE // 2) // BLOCK_SIZE
        grid_y = (self.y + BLOCK_SIZE // 2) // BLOCK_SIZE
        return grid_x, grid_y
    
    # 获取方块下落时的预期位置
    def get_fall_position(self):
        new_block = Block()
        new_block.x, new_block.y = self.x, self.y
        new_block.shape = self.shape.copy()
        new_block.move_down()
        return new_block
    
    # 绘制方块
    def draw(self, screen):
        for i in range(len(self.shape)):
            x, y = self.shape[i]
            rect = pygame.Rect(self.x + x * BLOCK_SIZE, self.y + y * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE)
            pygame.draw.rect(screen, self.color, rect)
            pygame.draw.rect(screen, (0, 0, 0), rect, 1)

class Game:
    def __init__(self):
        self.screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption('Tetris')
        self.clock = pygame.time.Clock()
        self.grid = [[None] * (WINDOW_WIDTH // BLOCK_SIZE) for _ in range(WINDOW_HEIGHT // BLOCK_SIZE)]
        self.block = Block()
        self.score = 0
        self.game_over = False
    
    # 处理键盘事件
    def handle_event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                self.block.rotate()
                if self.check_collision():
                    self.block.rotate()
            elif event.key == pygame.K_DOWN:
                self.move_down()
            elif event.key == pygame.K_LEFT:
                self.block.move_left()
                if self.check_collision():
                    self.block.move_right()
            elif event.key == pygame.K_RIGHT:
                self.block.move_right()
                if self.check_collision():
                    self.block.move_left()
    
    # 检查方块是否与其他方块碰撞
    def check_collision(self):
        for i in range(len(self.block.shape)):
            x, y = self.block.shape[i]
            grid_x, grid_y = self.block.get_grid_position()
            if grid_x + x < 0 or grid_x + x >= WINDOW_WIDTH // BLOCK_SIZE or \
                grid_y + y >= WINDOW_HEIGHT // BLOCK_SIZE or self.grid[grid_y+y][grid_x+x]:
                return True
        return False
    
    # 将方块固定在网格中
    def fix_block(self):
        for i in range(len(self.block.shape)):
            x, y = self.block.shape[i]
            grid_x, grid_y = self.block.get_grid_position()
            self.grid[grid_y+y][grid_x+x] = self.block.color
    
    # 消除满行的方块
    def clear_lines(self):
        num_lines_cleared = 0
        for y in range(WINDOW_HEIGHT // BLOCK_SIZE):
            if all(self.grid[y]):
                self.grid.pop(y)
                self.grid.insert(0, [None] * (WINDOW_WIDTH // BLOCK_SIZE))
                num_lines_cleared += 1
        self.score += num_lines_cleared ** 2 * 10
    
    # 检查游戏是否结束
    def check_game_over(self):
        for i in range(len(self.block.shape)):
            x, y = self.block.shape[i]
            grid_x, grid_y = self.block.get_grid_position()
            if grid_y + y < 0 or self.grid[grid_y+y][grid_x+x]:
                self.game_over = True
    
    # 将方块下落到最低位置
    def drop_block_to_bottom(self):
        while not self.check_collision():
            self.block.move_down()
        self.block.move_up()
    
    # 向下移动方块
    def move_down(self):
        self.block.move_down()
        if self.check_collision():
            self.block.move_up()
            self.fix_block()
            self.clear_lines()
            self.check_game_over()
            if not self.game_over:
                self.block = Block()
    
    # 绘制游戏界面
    def draw(self):
        self.screen.fill((255, 255, 255))
        for x in range(WINDOW_WIDTH // BLOCK_SIZE):
            for y in range(WINDOW_HEIGHT // BLOCK_SIZE):
                if self.grid[y][x]:
                    rect = pygame.Rect(x * BLOCK_SIZE, y * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE)
                    pygame.draw.rect(self.screen, self.grid[y][x], rect)
                    pygame.draw.rect(self.screen, (0, 0, 0), rect, 1)
        self.block.draw(self.screen)
        font = pygame.font.Font(None, 30)
        text = font.render('Score: ' + str(self.score), True, (0, 0, 0))
        self.screen.blit(text, (10, 10))
        if self.game_over:
            text = font.render('Game Over', True, (255, 0, 0))
            self.screen.blit(text, (WINDOW_WIDTH // 2 - text.get_width() // 2, WINDOW_HEIGHT // 2 - text.get_height() // 2))
        pygame.display.update()
    
    # 运行游戏主循环
    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return
                self.handle_event(event)
            
            self.move_down()
            self.draw()
            self.clock.tick(30)

if __name__ == '__main__':
    game = Game()
    game.run()
