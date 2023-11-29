# Глубокое обучение на практике
## Что было сделано?
### Задача
Создать прототип помощника для водителей, который будет оповещать их о дорожных знаках.
### Данные 
Не предоставлены данные для обучения модели. Соответственно их необходимо было найти. Был выбран [датасет](https://www.cvl.isy.liu.se/en/research/datasets/traffic-signs-dataset/). 

### Модель
Была выбрана модель YOLOv5 т.к. задача декомпозируется на детекцию и классификацию, а это как раз то что нам нужно в этой задаче. Далее возникла проблема, YOLO требует специальной аннотации, которая не совпадала с аннотацией нашего датасета. Поэтому было принято решение, написать скрипт, который трансформирует одну аннотацию в другую (`parsing.py`). Таким образом получилось собрать 4т. размеченных изображений, на 2.8т из которых был хотя бы 1 знак.

### Результат
 Модель обучалась на этих изображениях. Лучший из полученных результатов вы можете найти в `best/last.pt`. Чтобы оценить ее работоспособность, вы можете использовать консольную команду:
 ```
python3 notebooks/show.py best/last.pt data/day_alot.mp4
 ```
 Обратите, внимание файл day_alot.mp4 вы можете взять из наших данных по ссылке ниже (категория "обучение на вашем датасете")
 
 Также для проверки работы вы можете воспользоваться ноутбуками `yolo_test.ipynb` и `frame_test.ipynb`.
 Проверить качесто разметки можно с помощью файла `boundbox.py`.

## Установка
### Оргинизуем виртуальное окружение проекта
В корневой папке вашего репозитория выполните:
```
python3 -m venv venv
. venv/bin/activate
```

### Клонируем репозиторий с YOLO
В корневой папке вашего репозитория выполните:
```
git clone https://github.com/ultralytics/yolov5
cd yolo5
pip install -r requirements.txt
```
Далее нужно установить необходимые библиотеки для остальных файлов репозитория. Выполняем следущую команду из корня данного репозитория:
```
pip install -r requirements.txt
```

### Обучение на вашем датасете
Наши данные вы можете скачать по [ссылке](https://disk.yandex.ru/d/yLcFb1zlbjQQiw). Данный архив нужно распоковать в корневую директорию данного репозитория.

Для обучения на собственном датасете необходимо создать файл dataset.yaml. Этот файл должен отвечать определенным требованиям, которые вы можете увидеть по [ссылке](https://docs.ultralytics.com/yolov5/tutorials/train_custom_data/#11-create-datasetyaml). Я расположил данный файл в `notebooks/`.
Перед запуском обучения необходимо загрузить веса для дообучения.
```
python3
>>> import torch
>>> torch.hub.load('ultralytics/yolov5', 'yolov5s')
```
Чтобы запустить процесс обучения необходимо выполнить следующую консольную команду.
```
python3 yolov5/train.py --img 960 --batch 4 --epochs 20 --data notebooks/dataset.yaml --weights yolov5s.pt
```
Таким же образом можно дообучить вашу модель, просто поменяв путь до файла, например:
```
python3 yolov5/train.py --img 960 --batch 4 --epochs 20 --data notebooks/dataset.yaml --weights /yolov5/runs/train/exp/weights/last.pt
```


