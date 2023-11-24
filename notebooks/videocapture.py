import cv2
import time

# Путь к видеофайлу или 0 для использования камеры
video_path = 'curvy_road.mp4'  # ИЛИ 0 для использования камеры

# Открываем видеопоток
cap = cv2.VideoCapture(video_path)

# Проверяем, успешно ли открыт видеопоток
if not cap.isOpened():
    print("Ошибка при открытии видеофайла или камеры.")
    exit()

# Получаем частоту кадров видео
fps = cap.get(cv2.CAP_PROP_FPS)

# Определяем, что нужно получать один кадр в секунду
frames_per_second = 1
frame_interval = int(fps // frames_per_second)

# Переменная для отслеживания текущего кадра
current_frame = 0

while True:
    # Перемещаемся к следующему кадру
    cap.set(cv2.CAP_PROP_POS_FRAMES, current_frame)
    
    # Считываем кадр из видеопотока
    ret, frame = cap.read()
    print(ret)
    print(frame)
    
    # Проверяем, успешно ли считан кадр
    if not ret:
        print("Не удалось прочитать кадр.")
        break

    # Отображаем кадр
    cv2.imshow('Video Frame', frame)
    time.sleep(1)
    # Увеличиваем счетчик кадров
    current_frame += frame_interval

    # Для завершения программы нажмите 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Закрываем видеопоток и окна OpenCV
cap.release()
cv2.destroyAllWindows()
