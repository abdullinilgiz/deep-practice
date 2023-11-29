import os
import re

from pathlib import Path


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


name_ind = {
    '100_SIGN': 0,
    '110_SIGN': 1,
    '120_SIGN': 2,
    '30_SIGN': 3,
    '50_SIGN': 4,
    '60_SIGN': 5,
    '70_SIGN': 6,
    '80_SIGN': 7,
    '90_SIGN': 8,
    'GIVE_WAY': 9,
    'NO_PARKING': 10,
    'NO_STOPPING_NO_STANDING': 11,
    'OTHER': 12,
    'PASS_EITHER_SIDE': 13,
    'PASS_LEFT_SIDE': 14,
    'PASS_RIGHT_SIDE': 15,
    'PEDESTRIAN_CROSSING': 16,
    'PRIORITY_ROAD': 17,
    'STOP': 18,
    'URDBL': 19,
 }

directory_name = Path(__file__).resolve().parent.parent
annotations = ['annot_s1p0.txt', 'annot_s2p0.txt']
for annot in annotations:
    folder_path = os.path.join(directory_name, 'data')
    file = open(os.path.join(folder_path, annot))
    folder_path = os.path.join(folder_path, 'labels')
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
                    class_num = name_ind[sign_name]
                    x, y, w, h = convert_to_yolo(coords[0], coords[1],
                                                 coords[2], coords[3])
                    file.write(f'{class_num} {x} {y} {w} {h}\n')

labels = list(name_ind.keys())
path = os.path.join(folder_path, 'classes.txt')
with open(path, 'w') as file:
    for item in labels:
        file.write(item + '\n')
