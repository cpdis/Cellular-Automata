import pygame
import random

# Define some colors and other constants
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (25, 25, 25)
WIN_SIZE = 500
CELL_SIZE = 20
# Window height and width must be a multiple of the cell size
assert WIN_SIZE % CELL_SIZE == 0

# def blank():
#     grid = {}
#     for y in range (CELL_SIZE):
#         for x in range(CELL_SIZE):
#             grid[x, y] = 0


def grid():
    for x in range(0, WIN_SIZE, CELL_SIZE):  # draw vertical lines
        pygame.draw.line(screen, GRAY, (x, 0), (x, WIN_SIZE))
    for y in range(0, WIN_SIZE, CELL_SIZE):  # draw horizontal lines
        pygame.draw.line(screen, GRAY, (0, y), (WIN_SIZE, y))


def main():
    pygame.init()

    # Set the width and height of the screen [width, height]
    size = (WIN_SIZE, WIN_SIZE)
    global screen
    screen = pygame.display.set_mode(size)

    # Add a title
    pygame.display.set_caption("Conway's Game of Life")

    # Loop until the user clicks the close button.
    done = False

    # Used to manage how fast the screen updates
    clock = pygame.time.Clock()

    # -------- Main Program Loop -----------
    while not done:
        # --- Main event loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

        # --- Game logic should go here

        # 1. Any live cell with fewer than two live neighbours dies, as if by underpopulation.
        # 2. Any live cell with two or three live neighbours lives on to the next generation.
        # 3. Any live cell with more than three live neighbours dies, as if by overpopulation.
        # 4. Any dead cell with exactly three live neighbours becomes a live cell, as if by reproduction.

        # TODO: 3. Work on rules that i) look at all neighbors, ii) save new state in future_state

        # --- Screen-clearing code goes here

        # Here, we clear the screen to gray. Don't put other drawing commands
        # above this, or they will be erased with this command.
        screen.fill(WHITE)

        # Draw the grid
        grid()

        # --- Go ahead and update the screen with what we've drawn.
        pygame.display.flip()

        # --- Limit to 5 frames per second
        clock.tick(5)

    # Close the window and quit.
    pygame.quit()


if __name__ == "__main__":
    main()
