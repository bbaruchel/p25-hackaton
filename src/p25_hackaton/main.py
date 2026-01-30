from .display import Display
from .platform import Platform
from .goo import Goo


def main() -> None:
    start : Platform = Platform(x=0.05, y=0.4, width=0.1, height=0.02, start=True, end=False)
    end : Platform = Platform(x=0.65, y=0.1, width=0.1, height=0.02, start=False, end=True)
    platforms : list[Platform] = [start, end]

    goos : list[Goo] = []
    
    display = Display(width=0.8, height=0.6, start=start, end=end, platforms=platforms, goos=goos)

    running = True

    while running:
        running = display.handle_events()
        display.update()

    display.close()
