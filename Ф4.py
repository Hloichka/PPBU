from calendar import error


def analyze_log(file_name):
    counter = {'info':0, 'error':0, 'warning':0}

    try:
        with open(file_name, encoding="utf-8") as file:
            for line in file:
                if "[info]" in line:
                    counter['info'] += 1
                elif "[error]" in line:
                    counter['error'] += 1
                elif "[warning]" in line:
                    counter['warning'] += 1
        for k, v in counter.items():
            print(f'{k}: {v}')
    except FileNotFoundError:
        print(f' Файл {file_name} не найден. ')
    except Exception as e:
        print(f'Произошла ошибка: {e}')

analyze_log('log.txt')
