import time
questions = {'Сколько планет в солнечной системе? ':'8',
             'Столица Франции':'Париж '}

score = 0

for q,a in questions.items():
    start_timer = time.time()
    user_answer = input(q + '')
    end_time = time.time()
    if round(end_time - start_timer,1) > 5:
        print('Вы не уложились в таймер 5 сек')
        user_answer = 'wrong'
    print(f'Время ответа: {round(end_time-start_timer,1)} сек')
    if user_answer.lower() == a.lower():
        print('Правильно!')
        score += 1
    else:
        print('Неверно!')

print(f'Ваш результат {score} из {len(questions)}')