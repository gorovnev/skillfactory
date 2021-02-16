import numpy as np


def game_core_v1(number):
    """Просто угадываем на random, никак не используя информацию о больше или меньше.
       Функция принимает загаданное число и возвращает число попыток"""
    count = 0
    while True:
        count += 1
        predict = np.random.randint(1, 101)  # предполагаемое число
        if number == predict:
            return count  # выход из цикла, если угадали


def score_game(game_core):
    """Запускаем игру 1000 раз, чтобы узнать, как быстро игра угадывает число"""
    count_ls = []
    np.random.seed(1)  # фиксируем RANDOM SEED, чтобы ваш эксперимент был воспроизводим!
    random_array = np.random.randint(1, 101, size=(1000))
    for number in random_array:
        count_ls.append(game_core(number))
    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за {score} попыток")
    return score


def game_core_v2(number):
    '''Сначала устанавливаем любое random число, а потом уменьшаем или увеличиваем его в зависимости от того, больше оно или меньше нужного.
       Функция принимает загаданное число и возвращает число попыток'''
    count = 1
    predict = np.random.randint(1, 101)
    while number != predict:
        count += 1
        if number > predict:
            predict += 1
        elif number < predict:
            predict -= 1
    return count  # выход из цикла, если угадали


def game_core_v3(number):
    return binary_search(1, 101, number)


def binary_search(start, end, number):
    # Check boundaries
    if number < start or number > end:
        return 0
    cnt = 1  # init attempts counter
    while True:
        # Calculate half of a range
        half = start + int((end - start) / 2)
        # Check if we already found a number
        if number == start or number == end or number == half:
            return cnt
        # Check if we are in first half
        if start <= number < half:
            end = half
            cnt += 1
        # Check if we are in second half
        elif half < number < end:
            start = half
            cnt += 1
        # Just in case...
        else:
            cnt += 1


def game_core_v4(number):
    # Simple and straightforward implementation that takes only 1 shot
    a_list = list(range(1, 101))
    if number in a_list:
        return 1
    return 0


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    score_game(game_core_v3)
