char = input("which character: ")
side_length = int(input("length of side: "))
horizontal_spacing = int(input("horizontal spacing: "))
vert_counter = 0
while vert_counter < side_length:
    vert_counter += 1
    horiz_counter = 0
    line = ''
    while horiz_counter < vert_counter:
        horiz_counter += 1
        line += char + (' ' * horizontal_spacing)
    print(line)