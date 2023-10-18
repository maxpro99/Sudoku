# MakeSudoku.py

def saveinit(filename):
    try:
        with open(filename, "w") as file:
            file.write('#Кол-во ячеек поля /необязательный\n')
            file.write(f'field_size = 81\n')

            file.write('#Расположение ячеек поля [[x, y]]\n')
            file.write(f'field_pos = {field_pos}\n')

            file.write('#само поле [значение элемента]\n')
            file.write(f'field = {start_field}\n')

            file.write('#Кол-во контрольных полей /необязательный\n')
            file.write(f'control_fields_size = 27\n')

            file.write('#контрольные поля [[номера элементов], '  # номера элементов из поля
                       'условие/необязательный, '  # варианты - none, 'sum', 'substract', 'div', 'mult'
                       'значение/необязательный]\n')  # значение результата условия для поля
            file.write(f'control_fields = {control_fields}\n')

            file.write('#текущее поле\n')
            file.write(f'current_field = {start_field}\n')

            file.write('#текущий элемент\n')
            file.write(f'el = 0\n')

    except FileNotFoundError:
        print(f"Файл {filename} не найден.")
    except configparser.Error as e:
        print(f"Ошибка при чтении файла '{filename}': {e}")

def makeSudoku():
    global field_pos
    global start_field
    global control_fields

    field_pos = []
    for y in range(9):
        for x in range(9):
            field_pos.append([x, y])

    # "самая сложная" от финна Arto Inkala
    # start_field = [8, 0, 0,  0, 0, 0,  0, 0, 0,
    #                0, 0, 3,  6, 0, 0,  0, 0, 0,
    #                0, 7, 0,  0, 9, 0,  2, 0, 0,
    #
    #                0, 5, 0,  0, 0, 7,  0, 0, 0,
    #                0, 0, 0,  0, 4, 5,  7, 0, 0,
    #                0, 0, 0,  1, 0, 0,  0, 3, 0,
    #
    #                0, 0, 1,  0, 0, 0,  0, 6, 8,
    #                0, 0, 8,  5, 0, 0,  0, 1, 0,
    #                0, 9, 0,  0, 0, 0,  4, 0, 0]

    # Одна из задач с 17 стартовыми элементами от 01/01/2012 от
    # GaryMcGuire∗. "There is no 16-Clue Sudoku: Solving the Sudoku Minimum Number of Clues Problem"
    # ∗School of Mathematical Sciences, University College Dublin,Ireland.
    # E-mail: gary.mcguire@ucd.ie

    start_field = [0, 0, 0,  8, 0, 1,  0, 0, 0,
                   0, 0, 0,  0, 0, 0,  4, 3, 0,
                   5, 0, 0,  0, 0, 0,  0, 0, 0,

                   0, 0, 0,  0, 7, 0,  8, 0, 0,
                   0, 0, 0,  0, 0, 0,  1, 0, 0,
                   0, 2, 0,  0, 3, 0,  0, 0, 0,

                   6, 0, 0,  0, 0, 0,  0, 7, 5,
                   0, 0, 3,  4, 0, 0,  0, 0, 0,
                   0, 0, 0,  2, 0, 0,  6, 0, 0]

    control_fields = []
    for i in range(9):
        control_field_x = [x for x in range(81) if x // 9 == i]
        control_field_y = [y for y in range(81) if y % 9 == i % 9]
        control_fields.append(control_field_x)
        control_fields.append(control_field_y)
    for i1 in range(3):
        for i2 in range(3):
            control_field_z = []
            for i3 in range(3):
                for i4 in range(3):
                    control_field_z.append(i1 * 27 + i2 * 3 + i3 * 9 + i4)
            control_fields.append(control_field_z)

    saveinit('init.sudk')

makeSudoku()

