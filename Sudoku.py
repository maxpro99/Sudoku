import ast
import time


def no_problem(num, val):
    answer = True
    for control_field in control_fields:
        if answer and (num in control_field):
            for control_el in control_field:
                if answer and num != control_el and val == field[control_el]:
                    answer = False
    return answer


def load_task(filename):
    global field_pos
    global start_field
    global control_fields
    global current_field
    global el

    try:
        with open(filename, "r") as file:
            for line in file:
                if line.startswith("field_pos = "):
                    field_pos = ast.literal_eval(line.split('=')[1].strip())
                if line.startswith("field = "):
                    start_field = ast.literal_eval(line.split('=')[1].strip())
                if line.startswith("control_fields = "):
                    control_fields = ast.literal_eval(line.split('=')[1].strip())
                if line.startswith("current_field = "):
                    current_field = ast.literal_eval(line.split('=')[1].strip())
                if line.startswith("el = "):
                    el = ast.literal_eval(line.split('=')[1].strip())
    except FileNotFoundError:
        print(f"Файл {filename} не найден.")
    except IOError as e:
        print(f"Ошибка при чтении файла '{filename}': {e}")


def save_field(field, filename):
    print('Solve:')
    # Надо печать сделать поуниверсальнее для любых полей
    print(' ',
          '  '.join([str(el[1]) + '\n' if (el[0] + 1) % 9 == 0 else str(el[1]) for el in enumerate(field)]))

    with open(filename, 'a') as file:
        file.write('Решение:\n')
        file.write('  ')
        file.write('  '.join([str(el[1]) + '\n' if (el[0] + 1) % 9 == 0 else str(el[1]) for el in enumerate(field)]))
        file.write('\n\n')


if __name__ == '__main__':

    load_task('init.sudk')

    field = current_field
    solve = []

    firsteltoprogress = field.index(0)
    eltoprogress = field.index(0, firsteltoprogress + 1)
    progress = 0

    start_time = time.time()

    while 0 <= el < 81:
        while el < 81 and field[el] < 10:
            if start_field[el] != 0:
                el += 1
            else:
                if el == eltoprogress:
                    progress = field[firsteltoprogress] * 10 + field[el]
                    print(f'Progress approximately is : {progress}%; ')
                field[el] += 1
                if field[el] < 10 and no_problem(el, field[el]):
                    el += 1
        if el < 81:
            if start_field[el] == 0:
                field[el] = 0
                el -= 1
            while start_field[el] != 0:
                el -= 1
        else:
            solve.append(field)
            save_field(field, "solve.sudk")
            if len(solve) < 2:
                el = 80
                while start_field[el] != 0:
                    el -= 1
            else:
                print('The Solving more then one...')

    print(f'Вермя выполнения {time.time() - start_time} сек.')
    if len(solve) == 0:
        print('The Solving does not exist.')
    else:
        print('The Solving in "solve.sudk".')
