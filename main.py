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
    pass


color_names = get_color_choice()
quantity = get_num_hexagons()

draw_hexagon()
