import os
import re

from pathlib import Path

from pprint import pprint


def convert_to_yolo(x1, y1, x2, y2, image_width=1280, image_height=960):
    x = (x1 + x2) / (2 * image_width)
    y = (y1 + y2) / (2 * image_height)
    w = (x1 - x2) / image_width
    h = (y1 - y2) / image_height
    return x, y, w, h


def extract_name_and_coords(sign):
    print('*', sign, '*')
    coords = list(map(float, re.findall(r'\d*\.\d+|\d+', sign)))
    print(coords)
    sign_name = sign.split(', ')[-1]
    print(sign_name)
    return sign_name, coords


ind = 0
name_ind = dict() # {
#     'PRIORITY_ROAD': 0,
#     'PASS_EITHER_SIDE': 1,
#     'PASS_RIGHT_SIDE': 2,
#     'GIVE_WAY': 3,
#     '70_SIGN': 4,
#     '90_SIGN': 5,
#     'OTHER': 6,
#     '80_SIGN': 7,
#     '50_SIGN': 8,
#     'PEDESTRIAN_CROSSING': 9,
#     '60_SIGN': 10,
#     '30_SIGN': 11,
#     'NO_PARKING': 12,
#     'PASS_LEFT_SIDE': 13,
#     '110_SIGN': 14,
#     'STOP': 15,
#     '100_SIGN': 16,
#     'NO_STOPPING_NO_STANDING': 17,
#     'URDBL': 18,
#     '120_SIGN': 19,
#  }

file = open(
    '/home/ilgiz/dev/deep-practice/notebooks/const_data/sweden_labelling.txt')

directory_name = Path(__file__).resolve().parent.parent
folder_path = os.path.join(directory_name, 'labels')

for line in file:
    name_other = line.split(':')
    file_name = name_other[0].split('.')[0] + '.txt'
    path = os.path.join(folder_path, file_name)
    with open(path, 'w') as file:
        second_part = name_other[1].strip()
        signs = second_part.split(';')
        for sign in signs[0:len(signs) - 1]:
            if sign != 'MISC_SIGNS':
                sign_name, coords = extract_name_and_coords(sign)
                if sign_name not in name_ind:
                    name_ind[sign_name] = ind
                    ind += 1
                class_num = name_ind[sign_name]
                x, y, w, h = convert_to_yolo(coords[0], coords[1],
                                             coords[2], coords[3])
                file.write(f'{class_num} {x} {y} {w} {h}\n')

pprint(name_ind)

labels = []
for key, val in name_ind.items():
    labels.append((val, key))

labels.sort()

path = os.path.join(folder_path, 'classes.txt')
with open(path, 'w') as file:
    for item in labels:
        file.write(str(item[0]) + ' ' + str(item[1]) + '\n')
