class Subject(object):
    def __init__(self, name, date, homework):
        self.name = name
        self.date = date
        self.homework = homework


class Info(object):
    subjects = []

    @classmethod
    def get_homework(cls, date, hw):

        if date == 1:
            answer = '<b>Понедельник</b>' + '\n'
        elif date == 2:
            answer = '<b>Вторник</b>' + '\n'
        elif date == 3:
            answer = '<b>Среда</b>' + '\n'
        elif date == 4:
            answer = '<b>Четверг</b>' + '\n'
        elif date == 5:
            answer = '<b>Пятница</b>' + '\n'
        elif date == 6:
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

        for i in range(1, 8):
            answer += cls.get_homework(i, False) + '\n\n'

        return answer

    # Homework

    @classmethod
    def set_hw(cls, text):
        for i in cls.subjects:
            if i.name + ' /\/ ' in text:
                i.homework = text.replace(i.name + ' /\/ ', '').replace('\n', ' <-> ')
                return True
        return False

    @classmethod
    def upload_hw(cls):
        with open('hw.txt', 'w') as f:
            for i in cls.subjects:
                f.write(i.name + ' /\/ ' + i.homework + '\n')

    @classmethod
    def download_hw(cls):
        with open('hw.txt', 'r') as f:
            hw = f.readlines()
            for i in hw:
                cls.set_hw(i.replace('\n', ''))

    # Schedule

    @classmethod
    def set_schedule(cls, text):
        with open('schedule.txt', 'w') as f:
            f.write(text)

    @classmethod
    def upload_schedule(cls):
        with open('schedule.txt', 'w') as f:
            for i in cls.subjects:
                f.write('Subject(\'' + i.name + '\', [')

                for j in range(len(i.date)):
                    f.write('\'' + i.date[j] + '\'')

                    if j != len(i.date) - 1:
                        f.write(', ')
                    else:
                        f.write('], \'')

                f.write(i.homework + '\')\n')

    @classmethod
    def download_schedule(cls):
        Info.subjects = []
        with open('schedule.txt', 'r') as f:
            mas = f.readlines()

            for i in range(len(mas)):
                Info.subjects.append(eval(mas[i]))
