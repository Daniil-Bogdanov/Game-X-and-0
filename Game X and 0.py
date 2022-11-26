def table():
    print('—————————')
    print(f" | 0 | 1 | 2 |")
    for i in range(3):
        print('—————————')
        print(f"{i}| {game_field[i][0]} | {game_field[i][1]} | {game_field[i][2]} | ")

def take_input():
    while True:
        coords = input("  Введите координаты: ").split()
        if len(coords) != 2:
            print(" Введите две координаты ")
            continue
        x, y = coords
        if not (x.isdigit()) or not (y.isdigit()):
            print(" Введите числа ")
            continue
        x, y = int(x), int(y)
        if 0 > x or x > 2 or 0 > y or y > 2:
            print(" Координаты вне диапозона （>﹏<）")
            continue
        if game_field[x][y] != " ":
            print(" Игровая клетка уже занята (⋟﹏⋞)")
            continue
        return x, y

def victory():
    vick = (((0, 0), (0, 1), (0, 2)), ((1, 0), (1, 1), (1, 2)), ((2, 0), (2, 1), (2, 2)),
                ((0, 2), (1, 1), (2, 0)), ((0, 0), (1, 1), (2, 2)), ((0, 0), (1, 0), (2, 0)),
                ((0, 1), (1, 1), (2, 1)), ((0, 2), (1, 2), (2, 2)))
    for i in vick:
        a = i[0]
        b = i[1]
        c = i[2]
        if table[a[0]][a[1]] == table[b[0]][b[1]] == table[c[0]][c[1]] != " ":
            print(f"Победил {table[a[0]][a[1]]}")
            return True
    return False


game_field = [[" ", " ", " "] for i in range(3)]
count = 0
while True:
    count += 1
    table()
    print('—————————')
    if count % 2 == 1:
        print(" Ход крестика: ")
    else:
        print(" Ход нолика: ")
    x, y = take_input()
    if count % 2 == 1:
        game_field[x][y] = "X"
    else:
        game_field[x][y] = "0"
    if count == 9:
        print(" Ничья")
        break
