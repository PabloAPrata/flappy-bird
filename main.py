import pygame
from sys import exit

# Inicializando o game
pygame.init()
clock = pygame.time.Clock()  # Permite controlar o framerate do jogo

# Define o tamanho da janela
win_height = 720
win_width = 550
window = pygame.display.set_mode((win_width, win_height))

# Importando as imagens
bird_images = [pygame.image.load("assets/bird_down.png"),
               pygame.image.load("assets/bird_mid.png"),
               pygame.image.load("assets/bird_up.png")]
skyline_image = pygame.image.load("assets/background.png")
ground_image = pygame.image.load("assets/ground.png")
top_pipe_image = pygame.image.load("assets/pipe_top.png")
bottom_pipe_image = pygame.image.load("assets/pipe_bottom.png")
game_over_image = pygame.image.load("assets/game_over.png")
start_image = pygame.image.load("assets/start.png")

# Game
# Indica a velocidade que o chão rolará
scroll_speed = 2
bird_start_position = (100, 250)

class Bird(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = bird_images[0]
        self.rect = self.image.get_rect()
        self.rect.center = bird_start_position
        self.image_index = 0
        self.vel = 0
        self.flap = False
        self.alive = True

    def update(self, user_input):
        # Animar o pássaro
        self.image_index += 1
        if self.image_index >= 30:
            self.image_index = 0
        self.image = bird_images[self.image_index // 10]

class Ground(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = ground_image
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = x, y

    def update(self):
        # Move o chão
        self.rect.x -= scroll_speed
        if self.rect.x <= -win_width:
            self.kill()

# Sair do Jogo
def quit_game():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()


# Função main do jogo
# Função main do jogo
def main():

    # Instancia o pássaro
    bird = pygame.sprite.GroupSingle()
    bird_sprite = Bird()  # Crie uma instância do Bird
    bird.add(bird_sprite)

    # Instancia o chão inicial
    x_pos_ground, y_pos_ground = 0, 520
    ground = pygame.sprite.Group()
    ground.add(Ground(x_pos_ground, y_pos_ground))

    run = True
    while run:
        quit_game()

        # Define a tela base preta com os padrões RGB 0, 0, 0 = preto
        window.fill((0, 0, 0))

        # Desenha o plano de fundo
        window.blit(skyline_image, (0, 0))  # (0, 0) é a posição da imagem

        # Cria o Chão
        if len(ground) <= 2:
            ground.add(Ground(win_width, y_pos_ground))

        # Desenha - tubos, pássaro e o chão
        ground.draw(window)
        bird.draw(window)

        # Atualiza - tubos, pássaro e o chão
        ground.update()
        bird_sprite.update(None)  # Passe None como o argumento user_input para bird.update()

        clock.tick(60)  # Define o framerate para 60.
        pygame.display.update()

main()