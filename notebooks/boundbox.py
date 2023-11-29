import matplotlib.pyplot as plt
import matplotlib.patches as patches
from PIL import Image

image_path = 'data/main_road.jpg'
bound_box = [734.514285, 476.071103, 682.706066, 428.440966]  
image = Image.open(image_path)

# Создание объекта "фигуры" для прямоугольной рамки
rect = patches.Rectangle(
    (bound_box[0], bound_box[1]),  # (x, y)
    bound_box[2] - bound_box[0],   # width
    bound_box[3] - bound_box[1],   # height
    linewidth=2, edgecolor='r', facecolor='none'  # Цвет рамки и ее толщина
)

fig, ax = plt.subplots(1)
ax.imshow(image)
ax.add_patch(rect)
plt.show()


def yolo_to_regular(yolo_bound_box, image_width, image_height):
    center_x, center_y, width, height = yolo_bound_box

    x_min = (center_x - width / 2) * image_width
    y_min = (center_y - height / 2) * image_height
    x_max = (center_x + width / 2) * image_width
    y_max = (center_y + height / 2) * image_height

    return [x_min, y_min, x_max, y_max]


image_width = 1280
image_height = 960

yolo_bound_box = [0.553601699609375, 0.4711000359375, 0.040475171093750005, 0.049614726041666654]

bound_box = yolo_to_regular(yolo_bound_box, image_width, image_height)

print("Обычный bound box:", bound_box)


# Пример YOLO-bound box

# Создание объекта "оси" для отображения изображения и YOLO-bound box
image = Image.open(image_path)

# Создание объекта "фигуры" для прямоугольной рамки
rect = patches.Rectangle(
    (bound_box[0], bound_box[1]),  # (x, y)
    bound_box[2] - bound_box[0],   # width
    bound_box[3] - bound_box[1],   # height
    linewidth=2, edgecolor='r', facecolor='none'  # Цвет рамки и ее толщина
)

fig, ax = plt.subplots(1)
ax.imshow(image)
ax.add_patch(rect)
plt.show()
