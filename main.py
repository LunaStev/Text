import pygame

pygame.init()

width = 1920
height = 1080

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("이상한 프로그램")

background_color = (0, 0, 0)
screen.fill(background_color)

custom_font = pygame.font.Font("SCDream3.otf", 280)
custom_font.set_bold(True)
bold_text = custom_font.render("자리비움", True, (255, 255, 255))

text_rect = bold_text.get_rect(center=(width // 2, height // 2))

screen.blit(bold_text, text_rect)

pygame.display.flip()

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
pygame.quit()