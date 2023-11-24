import os
from pathlib import Path

path = Path(__file__).resolve().parent
file_path = os.path.join(path, 'example.txt')
print(file_path)

# print(int('547.856366'))

sign_ind = {
    'PRIORITY_ROAD': 0,
    'PASS_EITHER_SIDE': 1,
    'PASS_RIGHT_SIDE': 2,
    'GIVE_WAY': 3,
    '70_SIGN': 4,
    '90_SIGN': 5,
    'OTHER': 6,
    '80_SIGN': 7,
    '50_SIGN': 8,
    'PEDESTRIAN_CROSSING': 9,
    '60_SIGN': 10,
    '30_SIGN': 11,
    'NO_PARKING': 12,
    'PASS_LEFT_SIDE': 13,
    '110_SIGN': 14,
    'STOP': 15,
    '100_SIGN': 16,
    'NO_STOPPING_NO_STANDING': 17,
    'URDBL': 18,
    '120_SIGN': 19,
}
to_print = list(sign_ind.keys())
to_print.sort()

for item in to_print:
    print('\'' + item + '\'')
