import asyncio
import pygame
from typing import Tuple

pygame.init()

SCREEN_SIZE: Tuple[int, int] = (1080, 720)
DISPLAY = pygame.display.set_mode(SCREEN_SIZE, pygame.RESIZABLE)
pygame.display.set_caption("test")
CLOCK = pygame.time.Clock()
delta_time: float = 0.1
font = pygame.font.Font(None, 36)

VIRTUAL = pygame.Surface(SCREEN_SIZE)

def blit_virtual(surface: pygame.Surface) -> None:
    """Scale and letterbox the fixed-resolution surface to the actual window."""
    window = pygame.display.get_surface()
    if window is None:
        return
    win_w, win_h = window.get_size()
    surf_w, surf_h = surface.get_size()

    scale = min(win_w / surf_w, win_h / surf_h)
    scaled_w = max(1, int(surf_w * scale))
    scaled_h = max(1, int(surf_h * scale))

    scaled = pygame.transform.smoothscale(surface, (scaled_w, scaled_h))

    x = (win_w - scaled_w) // 2
    y = (win_h - scaled_h) // 2

    window.fill((0, 0, 0))
    window.blit(scaled, (x, y))

async def main() -> None:
    running: bool = True
    hello_world = font.render("Hello World", True, (255, 255, 255))

    while running:
        for event in pygame.event.get():
            match event.type:
                case pygame.QUIT:
                    running = False
                case _:
                    pass

        VIRTUAL.fill((30, 30, 30))
        VIRTUAL.blit(hello_world, (10, 10))

        blit_virtual(VIRTUAL)

        pygame.display.flip()
        delta_time = CLOCK.tick(60) / 1000
        delta_time = max(0.001, min(0.1, delta_time))
        await asyncio.sleep(0)

asyncio.run(main())
