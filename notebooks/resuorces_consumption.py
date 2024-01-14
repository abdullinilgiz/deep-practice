import psutil
import GPUtil


def get_process_memory_info(pid):
    try:
        process = psutil.Process(pid)
        memory_info = process.memory_info()
        return {
            'Использование оперативной памяти (MB)': memory_info.rss /
            (1024 * 1024),
        }
    except psutil.NoSuchProcess as e:
        return f"Процесс с PID {pid} не найден: {e}"


def get_process_gpu_info(pid):
    try:
        gpus = GPUtil.getGPUs()
        if pid in gpus:
            gpu = gpus[pid]
            return {
                'Имя GPU': gpu.name,
                'Использование видеопамяти (%)': gpu.memoryUtil * 100,
                'Общая видеопамять (MB)': gpu.memoryTotal,
                'Используемая видеопамять (MB)': gpu.memoryUsed,
                'Свободная видеопамять (MB)': gpu.memoryFree
            }
        return f"Процесс с PID {pid} не найден среди GPU-процессов."
    except Exception as e:
        return f"Ошибка при получении информации о GPU: {e}"


# Замените PID на актуальный
pid_to_check = 25410

memory_info = get_process_memory_info(pid_to_check)
print("Информация об использовании памяти для процесса:")
for key, value in memory_info.items():
    print(f"{key}: {value}")

gpu_info = get_process_gpu_info(pid_to_check)
print("\nИнформация об использовании видеопамяти для процесса:")
if isinstance(gpu_info, dict):
    for key, value in gpu_info.items():
        print(f"{key}: {value}")
else:
    print(gpu_info)
