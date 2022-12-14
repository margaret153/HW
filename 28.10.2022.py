import random
class Animal:

    def __init__(self, name, age, height=160):
        self.name = name
        self.age = age
        self.height = height

    def __str__(self):
        return f'Name animal  {self.name} \nAge animal  {self.age} old'

    def __del__(self):
        print('DELETE object')

    def __bool__(self):
        return self.name != None
    def __len__(self):
        return self.height
    def __init__(self):
        self.name = name
        self.gladness = 25
        self.progress = 0
        self.alive = True


    def to_sleep(self):
        print('Sleep!')
        self.gladness += 6

    def to_chill(self):
        print('Rest time')
        self.progress += 0.1
        self.gladness += 6

    def is_alive(self):
        if self.progress < 4:
            print('Good')
            self.alive = True
        elif self.gladness <= 5:
            print('Happy...')
            self.alive = True
        elif self.progress > 5:
            print('Passed extremaly...')
            self.alive = False

    def end_to_day(self):
        print(f'Gladness = {self.gladness}')
        print(f'Progress = {round(self.progress, 2)}')

    def live(self, day):
        day = 'Day' + str(day) + 'of' + self.name + 'live'
        print(f"{day:=50}")
        live_cube = random.randint
        if live_cube == 1:
            self.to_study()
        elif live_cube == 2:
            self.to_sleep()
        elif live_cube == 3:
            self.to_chill()
        self.end_to_day()
        self.is_alive()
    def info_student(self):
        print(f'Name animal {self.name}\n'
              f'Age animal {self.age} old')


animal1 = Animal(name=None, age=4)
animal2 = Animal(name='Milly', age=3)
print(animal1)
print(animal2)
print(bool(animal1))
print(bool(animal2))
print(len(animal1))