class Subject(object):
    def __init__(self, name, date, homework):
        self.name = name
        self.date = date
        self.homework = homework


class Info(object):
    subjects = [
        Subject('инфа',
                ['[0]_10:00', '[1]_11:00', '[2]_12:00', '[3]_13:00', '[4]_14:00'],
                'not defined'),

        Subject('русский',
                ['[0]_10:00', '[1]_11:00', '[2]_12:00', '[3]_13:00', '[4]_14:00'],
                'not defined'),

        Subject('матеша',
                ['[0]_10:00', '[1]_11:00', '[2]_12:00', '[3]_13:00', '[4]_14:00'],
                'not defined'),

        Subject('обж',
                ['[0]_10:00', '[1]_11:00', '[2]_12:00', '[3]_13:00', '[4]_14:00'],
                'not defined')
    ]

    @classmethod
    def get_homework(cls, date, hw):

        if date == 0:
            answer = 'Понедельник' + '\n'
        elif date == 1:
            answer = 'Вторник' + '\n'
        elif date == 2:
            answer = 'Среда' + '\n'
        elif date == 3:
            answer = 'Четверг' + '\n'
        elif date == 4:
            answer = 'Пятница' + '\n'
        elif date == 5:
            answer = 'Суббота' + '\n'
        else:
            answer = 'Воскресенье' + '\n'

        for i in cls.subjects:

            for j in i.date:
                if '[' + str(date) + ']' in j:
                    if hw:
                        answer += '\n' + i.date[date][4:] + '\t' + i.name + '\n' + i.homework
                    else:
                        answer += '\n' + i.date[date][4:] + '\t' + i.name

        return answer


    @classmethod
    def get_schedule(cls):

        answer = ''

        for i in range(7):
            answer += cls.get_homework(i, False) + '\n\n'

        return answer
