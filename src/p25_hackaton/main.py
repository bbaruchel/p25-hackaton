from .display import Display
from .platform import Platform
from .goo import Goo


def main() -> None:
    start : Platform = Platform(x=50, y=400, width=100, height=20, start=True, end=False)
    end : Platform = Platform(x=650, y=100, width=100, height=20, start=False, end=True)
    platforms : list[Platform] = [start, end]

    goos : list[Goo] = []
    
    display = Display(width=800, height=600, start=start, end=end, platforms=platforms, goos=goos)

    running = True

    while running:
        running = display.handle_events()
        display.update()
    display.close()

