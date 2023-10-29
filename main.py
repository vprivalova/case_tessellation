import turtle as t
import ru_local as ru


def get_num_hexagons():
    hex_number = int(input('\n' + ru.HEX_NUMBER))
    while (hex_number < 4) or (hex_number > 20):
        hex_number = int(input(ru.HEX_NUMBER_AGAIN))

    return hex_number


def get_color_choice():
    available_colors = [ru.RED, ru.YELLOW, ru.GREEN, ru.BLUE, ru.BLACK, ru.VIOLET, ru.ORANGE]

    print(ru.ACCEPTABLE_COLORS)
    for element in available_colors:
        print(element)

    color_name1 = input('\n' + ru.COLOR1_INPUT)
    while color_name1 not in available_colors:
        color_name1 = input(ru.COLOR1_INPUT_AGAIN)

    color_name2 = input('\n' + ru.COLOR2_INPUT)
    while color_name2 not in available_colors:
        color_name2 = input(ru)

    colors = [color_name1, color_name2]

    return colors


def draw_hexagon(x, y, side_len, color):
    t.pencolor(color)
    t.fillcolor(color)
    t.pu()
    t.goto(x, y)
    t.pd()
    t.begin_fill()
    t.setheading(30)
    for i in range(6):
        t.forward(side_len)
        t.left(300)
    t.end_fill()
    t.setheading(0)


color_names = get_color_choice()
quantity = get_num_hexagons()

t.speed(5000)
d = 500 // quantity
side_len = d // (3 ** 0.5)
number_rows = int(500 // (2 * side_len))

for number in range(number_rows+1):
    y_1 = 250 - 0.5 * side_len - (1.5 * side_len) * number
    for hexagon in range(quantity+1):
        if number == 0:
            x_1 = -250 + (3 ** 0.5) * side_len * 0.5 + (3 ** 0.5) * side_len * hexagon
            draw_hexagon(x_1, y_1, side_len, 'green')
        elif number % 2 == 0:
            x_1 = -250 + (3 ** 0.5) * side_len * 0.5 + (3 ** 0.5) * side_len * hexagon
            draw_hexagon(x_1, y_1, side_len, 'green')
        else:
            x_1 = -250 + (3 ** 0.5) * side_len * hexagon
            draw_hexagon(x_1, y_1, side_len, 'green')
t.mainloop()
