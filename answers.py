def get_answer(question):
    question = question.lower()
    answers = {'привет':'И тебе привет!', 'как дела':'Лучше всех', 'пока':'Увидимся'}
    dialog = answers.get(question)
    print(dialog) 
    return dialog

get_answer('КАК ДЕЛА')