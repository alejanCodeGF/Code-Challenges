# * Crea una función que dibuje una espiral como la del ejemplo.
# * - Únicamente se indica de forma dinámica el tamaño del lado.
# * - Símbolos permitidos: ═ ║ ╗ ╔ ╝ ╚
# *
# * Ejemplo espiral de lado 5 (5 filas y 5 columnas):
# * ════╗
# * ╔══╗║
# * ║╔╗║║
# * ║╚═╝║
# * ╚═══╝ 

# ESTE CODIGO NO LO HE HECHO YO, no sabia ni por donde empezar

def draw_spiral(side_length):
    # Calculate the number of rows and columns needed for the spiral
    rows = side_length
    cols = side_length

    # Create an empty grid
    grid = [[' ' for _ in range(cols)] for _ in range(rows)]

    # Initialize the starting position and direction
    row = 0
    col = 0
    direction = 'right'

    # Define the symbols for each direction
    symbols = {
        'right': ['═', '╗', '╝', '╔'],
        'down': ['║', '╝', '╚', '╗'],
        'left': ['═', '╔', '╚', '╝'],
        'up': ['║', '╗', '╔', '╚']
    }

    # Function to update the direction
    def update_direction():
        nonlocal direction
        if direction == 'right':
            direction = 'down'
        elif direction == 'down':
            direction = 'left'
        elif direction == 'left':
            direction = 'up'
        elif direction == 'up':
            direction = 'right'

    # Function to check if a given position is valid
    def is_valid_position(row, col):
        return 0 <= row < rows and 0 <= col < cols and grid[row][col] == ' '

    # Function to check if a corner needs to be added
    def needs_corner(row, col):
        if direction == 'right' and (col + 1 == cols or grid[row][col + 1] != ' '):
            return True
        elif direction == 'down' and (row + 1 == rows or grid[row + 1][col] != ' '):
            return True
        elif direction == 'left' and (col == 0 or grid[row][col - 1] != ' '):
            return True
        elif direction == 'up' and (row == 0 or grid[row - 1][col] != ' '):
            return True
        return False

    # Main loop to fill the grid
    for num in range(1, side_length ** 2 + 1):
        grid[row][col] = symbols[direction][0]

        if needs_corner(row, col):
            update_direction()
            grid[row][col] = symbols[direction][3]

        if direction == 'right':
            col += 1
        elif direction == 'down':
            row += 1
        elif direction == 'left':
            col -= 1
        elif direction == 'up':
            row -= 1

    # Convert the grid to the string representation
    output = ''
    for row in grid:
        for symbol in row:
            output += symbol
        output += '\n'

    return output

# Test the function
side_length = 5
spiral = draw_spiral(side_length)
print(spiral)
