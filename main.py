questions = {'Сколько планет в солнечной системе? ':'8',
             'Столица Франции':'Париж '}

score = 0

for q,a in questions.items():
    user_answer = input(q + '')
    if user_answer.lower() == a.lower():
        print('Правильно!')
        score += 1
    else:
        print('Неверно!')

print(f'Ваш результат {score} из {len(questions)}')