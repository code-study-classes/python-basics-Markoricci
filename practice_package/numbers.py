def calculate_distance(x1, x2):
    return abs(x1 - x2)

def calculate_segments(length_a, length_b):
    if length_a <= length_b:
        raise ValueError
    return length_a // length_b

def calculate_digit_sum(number):
    return sum(int(digit) for digit in str(abs(number)))

def calculate_rect_area(x1, y1, x2, y2):
    width = abs(x2 - x1)
    height = abs(y2 - y1)
    return width * height

def round_to_multiple(number, multiple):
    return round(number / multiple) * multiple
