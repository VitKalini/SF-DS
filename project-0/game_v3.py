"""Игра угадай число.
Компьютер сам загадывает и угадывает число
"""

import numpy as np

def game_core_v3(number: int = 1) -> int:
    """ Компьютер угадывает число методом бинарного поиска.
    Идея заключается в деление массива пополам, после чего в зависимости от медианного элемента в списке,
    мы переходим либо к левой, либо к правой половине массива )
    
    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    # Записываем лимиты диапазона, в котором находится искомое число
    upper_lim = 100
    lower_lim = 1 
    

    while True:
        count = 1
        
        if number == upper_lim: # Без этого условия цикл будет бесконечный, если загаданное число равно верхнему лимиту
            break
        
        else:
            while upper_lim > lower_lim+1: # Повторяем пока между двумя лимитами не останется элементов
                middle = (upper_lim + lower_lim) // 2 # Находим среднее значение в диапазоне
                count += 1 
                if middle > number: # Сравниваем значение с числом и присваеваем лимитам значение в зависимости от проверки
                    upper_lim = middle
                else:
                    lower_lim = middle
            
            predict_number = upper_lim - 1 # После всех преобразований верхний лимит будет следующим числом после искомого
            if predict_number == number: # Делаем финальную проверку
                count +=1
                break
    return count

def score_game(random_predict) -> int:
    """За какое количество попыток в среднем из 1000 подходов угадывает наш алгоритм

    Args:
        random_predict ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """
    count_ls = [] # список для сохранения количества попыток
    np.random.seed(1) # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1,101,size=(10000)) # загадали список чисел
    
    for number in random_array:
        count_ls.append(random_predict(number))
    
    score = int(np.mean(count_ls)) # находим среднее количество попыток
    
    print(f'Ваш алгоритм угадывает число в среднем за: {score} попыток')
    return score
if __name__ == '__main__':
    score_game(game_core_v3)
        
    
    
        
    
    
    
        





