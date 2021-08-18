class Subject(object):
    def __init__(self, name, date, homework):
        self.name = name
        self.date = date
        self.homework = homework


class Info(object):
    subjects = [
        Subject('обж',
                ['[0]_11:00'],
                'not defined'),

        Subject('ин яз',
                ['[0]_12:00', '[2]_13:00', '[5]_11:00'],
                'not defined'),

        Subject('алгебра',
                ['[0]_13:00', '[0]_14:00', '[4]_13:00', '[4]_14:00'],
                'not defined'),

        Subject('физика',
                ['[0]_15:00', '[1]_13:00', '[2]_11:00', '[3]_14:00'],
                'not defined'),

        Subject('экономика',
                ['[0]_16:00'],
                'not defined'),

        Subject('право',
                ['[0]_17:00'],
                'not defined'),

        Subject('практикум',
                ['[1]_11:00', '[1]_12:00'],
                'not defined'),

        Subject('химия',
                ['[1]_14:00'],
                'not defined'),

        Subject('литература',
                ['[1]_15:00', '[2]_16:00', '[5]_14:00'],
                'not defined'),

        Subject('русский',
                ['[1]_16:00', '[2]_14:00', '[2]_15:00', '[2]_17:00'],
                'not defined'),

        Subject('физкультура',
                ['[1]_17:00', '[3]_11:00'],
                'not defined'),

        Subject('информатика',
                ['[2]_12:00', '[4]_11:00', '[4]_12:00', '[5]_12:00'],
                'not defined'),

        Subject('обществознание',
                ['[3]_12:00', '[3]_13:00'],
                'not defined'),

        Subject('география',
                ['[3]_15:00'],
                'not defined'),

        Subject('геометрия',
                ['[3]_16:00', '[3]_17:00'],
                'not defined'),

        Subject('история',
                ['[4]_15:00', '[5]_13:00'],
                'not defined')
    ]

    @classmethod
    def get_homework(cls, date, hw):

        if date == 0:
            answer = '<b>Понедельник</b>' + '\n'
        elif date == 1:
            answer = '<b>Вторник</b>' + '\n'
        elif date == 2:
            answer = '<b>Среда</b>' + '\n'
        elif date == 3:
            answer = '<b>Четверг</b>' + '\n'
        elif date == 4:
            answer = '<b>Пятница</b>' + '\n'
        elif date == 5:
            answer = '<b>Суббота</b>' + '\n'
        else:
            answer = '<b>Воскресенье</b>' + '\n'

        mas = []

        for i in cls.subjects:

            for j in i.date:
                if '[' + str(date) + ']' in j:
                    if hw:
                        mas.append('\n' + j[4:] + '\t' + i.name + '\n' + i.homework.replace(' <-> ', '\n') + '\n')
                    else:
                        mas.append('\n' + j[4:] + '\t' + i.name)

        mas.sort()

        for i in mas:
            answer += i

        return answer

    @classmethod
    def get_schedule(cls):

        answer = ''

        for i in range(7):
            answer += cls.get_homework(i, False) + '\n\n'

        return answer

    @classmethod
    def set_homework(cls, text):
        for i in cls.subjects:
            if i.name + ' /\/ ' in text:
                i.homework = text.replace(i.name + ' /\/ ', '').replace('\n', ' <-> ')
                return True
        return False

    @classmethod
    def backup(cls):
        with open('backup.txt', 'w') as f:
            for i in cls.subjects:
                f.write(i.name + ' /\/ ' + i.homework + '\n')

    @classmethod
    def upload_hw_from_file(cls):
        with open('backup.txt', 'r') as f:
            hw = f.readlines()
            for i in hw:
                cls.set_homework(i.replace('\n', ''))
