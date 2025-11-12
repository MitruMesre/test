import asyncio
import pygame
from typing import Tuple

pygame.init()

SCREEN_SIZE: Tuple[int, int] = (1080, 720)
SCREEN = pygame.display.set_mode(SCREEN_SIZE, pygame.SCALED | pygame.NOFRAME)
pygame.display.set_caption("test")
CLOCK = pygame.time.Clock()
delta_time: float = 0.1
font = pygame.font.Font(None, 36)

async def main() -> None:
    running: bool = True
    hello_world = font.render("Hello World", True, (255, 255, 255))
    while running:
        for event in pygame.event.get():
            match event.type:
                case pygame.QUIT:
                    running = False

        SCREEN.fill((30, 30, 30))
        SCREEN.blit(hello_world, (10, 10))

        pygame.display.flip()
        delta_time = CLOCK.tick(60) / 1000
        delta_time = max(0.001, min(0.1, delta_time))
        await asyncio.sleep(0)

asyncio.run(main())
