class Bird:
    def __init__(self, name, size):
        self.name = name
        self.size = size

    def describe(self, full=False):
        return f'Размер птицы {self.name} — {self.size}.'


class Parrot(Bird):
    def __init__(self, name, size, color):
        super().__init__(name, size)
        self.color = color
    
    def describe(self, full=False):
        if full is True: 
            return (f'Попугай {self.name} — заметная птица, окрас её '
                    f'перьев — {self.color}, а размер — {self.size}.'
                    f' Интересный факт: попугаи чувствуют ритм, а вовсе' 
                    f' не бездумно двигаются под музыку. Если сменить' 
                    f' композицию, то и темп движений птицы изменится.')
        else:
            return f'Размер птицы {self.name} — {self.size}.'
    # Переопределите метод describe().


class Penguin(Bird):
    def __init__(self, name, size, genus):
        super().__init__(name, size)
        self.genus = genus
    
    def describe(self, full=False):
        if full is True:
            return (f'Размер пингвина {self.name} из рода '
                    f'{self.genus} — {self.size} Интересный факт:' 
                    f'однажды группа геологов-разведчиков похитила ' 
                    f'пингвинье яйцо, и их принялась преследовать'
                    f'вся стая, не пытаясь, впрочем, при этом нападать.'
                    f'посовещавшись, похитители вернули птицам яйцо,'
                    f'и те отстали.')
        else:
            return f'Размер птицы {self.name} — {self.size}.'
    # Переопределите метод describe().


kesha = Parrot('Ара', 'средний', 'красный')
kowalski = Penguin('Королевский', 'большой', 'Aptenodytes')

# Вызов метода у созданных объектов.
kesha.describe()
kowalski.describe(True)