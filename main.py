class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

def intersection_exist(a, b):
    xo, ox, yo, oy = False, False, False, False
    ab = axis_intersection(a, b)

    if min(a.x, b.x) <= ab.x <= max(a.x, b.x):
        if ab.x >= 0:
            ox = True
        if ab.x <= 0:
            xo = True

    if min(a.y, b.y) <= ab.y <= max(a.y, b.y):
        if ab.y >= 0:
            oy = True
        if ab.y <= 0:
            yo = True
    return xo, ox, yo, oy


def axis_intersection(a, b):
    return Point((a.x + b.x) / 2, (a.y + b.y) / 2)


def read_point_from_file(file_path):
    with open(file_path, 'r') as file:
        x, y = map(float, file.readline().split())
    return Point(x, y)

def task_3_12_solution():
    # Чтение данных о вершинах треугольника из файлов
    file_paths = ['vertex_1.txt', 'vertex_2.txt', 'vertex_3.txt', 'vertex_4.txt', 'vertex_5.txt']
    vertices = [read_point_from_file(file_path) for file_path in file_paths]
    xo, ox, yo, oy = False, False, False, False
    # Проверка пересечений и вывод информации
    for i in range(len(vertices)):
        for j in range(i + 1, len(vertices)):
            xo, ox, yo, oy = intersection_exist(vertices[i], vertices[j])

        if xo and ox and yo and oy:
            print(f"Треугольник {i + 1} лежит в четырех четвертях")
        else:
            print(f"Треугольник {i + 1} не лежит в четырех четвертях")
if __name__=='__main__':
    task_3_12_solution()