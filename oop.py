#ООП: классы, объекты, инкапсуляция, наследование, полиморфизм, абстракция.
#Пример создания и доступа к приватному методу класса.
class A:
    def _priv(self):
        print("from a")

a = A()
a._priv()

class B:
    def __private(self):
        print("from privated b")

b = B()
#b.__private()
b._B__private()

#Декоратор проперти, геттеры, сеттеры.
class Temperature:
    def __init__(self, temp_f):
        self._temp_f = temp_f

    @property
    def temp_f(self):
        return self._temp_f

    @temp_f.setter
    def temp_f(self, value):
        if value < -459.67:
            raise ValueError("Temperature cannot be below absolute zero")
        self._temp_f = value

# Create an instance
temp = Temperature(70)
print(temp.temp_f)  # Accessing the getter

temp.temp_f = 80 # Accessing the setter
print(temp.temp_f)

try:
    temp.temp_f = -500 # Trying to set invalid value
except ValueError as e:
    print(e)

print(temp.__dict__)
#Доступ к атрибуту через имя класса и через имя экземпляра.
class C:
    perem_c = 4

print(C.perem_c)
c = C()
print(c.perem_c)
#Динамическое добавление метода в класс.
class SomeClass():
    pass

def squareMethod(self, x):
    return x*x

SomeClass.square = squareMethod
obj = SomeClass()

print(obj.square(5)) # 25
#Декораторы статический метод и метод класса
class SomeClass():
    @staticmethod   #декоратор
    def hello():
        print("Hello, world")
                                   #Доступ к таким методам можно получить как из экземпляра класса, так и из самого класса
SomeClass.hello() # Hello, world
obj = SomeClass()
obj.hello() # Hello, world

#методы классов создаются с помощью декоратора @classmethod и требуют обязательную ссылку на класс (cls)
class SomeClass(object):
    @classmethod
    def hello(cls):
        print('Hello, класс {}'.format(cls.__name__))

SomeClass.hello() # Hello, класс SomeClass

#Статические и классовые методы доступны без инстанцирования

#метод __new__, который непосредственно создает новый экземпляр класса. Первым параметром он принимает ссылку на сам класс:
class SomeClass(object):
    def __new__(cls):
        print("new")
        return super(SomeClass, cls).__new__(cls)

    def __init__(self):
        print("init")

obj = SomeClass();
# new
# init
# Для создания иммутабельных объектов или реализации паттерна Синглтон:
class Singleton(object):
    obj = None # единственный экземпляр класса

    def __new__(cls, *args, **kwargs):
        if cls.obj is None:
            cls.obj = object.__new__(cls, *args, **kwargs)
        return cls.obj

single = Singleton()
single.attr = 42
newSingle = Singleton()
newSingle.attr # 42
newSingle is single # true

#другой способ организации межклассового взаимодействия – ассоциация (агрегация или композиция),
# при которой один класс является полем другого
# композиция
class Salary:
    def __init__(self,pay):
        self.pay = pay

    def getTotal(self):
        return (self.pay*12)

class Employee:
    def __init__(self,pay,bonus):
        self.pay = pay
        self.bonus = bonus
        self.salary = Salary(self.pay)

    def annualSalary(self):
        return "Total: " + str(self.salary.getTotal() + self.bonus)

employee = Employee(100,10)
print(employee.annualSalary())
#агрегация
class Salary(object):
    def __init__(self, pay):
        self.pay = pay

    def getTotal(self):
        return (self.pay * 12)

class Employee(object):
    def __init__(self, pay, bonus):
        self.pay = pay
        self.bonus = bonus

    def annualSalary(self):
        return "Total: " + str(self.pay.getTotal() + self.bonus)

salary = Salary(100)
employee = Employee(salary, 10)
print(employee.annualSalary())
#избегать циклического ссылания друг на друга. Помогают слабые ссылки (модуль weakref)

#Полиморфизм. Все методы в языке изначально виртуальные. Переопределение
class Mammal:
    def move(self):
        print('Двигается')

class Hare(Mammal):
    def move(self):
        print('Прыгает')

animal = Mammal()
animal.move() # Двигается
hare = Hare()
hare.move() # Прыгает

class English:
  def greeting(self):
    print ("Hello")

class French:
  def greeting(self):
    print ("Bonjour")

def intro(language):
  language.greeting()

john = English()
gerard = French()
intro(john) # Hello
intro(gerard) # Bonjour

#утиная типизация
#Метаклассы – это классы, инстансы которых тоже являются классами
class MetaClass(type):
    # выделение памяти для класса
    def __new__(cls, name, bases, dict):
        print("Создание нового класса {}".format(name))
        return type.__new__(cls, name, bases, dict)

    # инициализация класса
    def __init__(cls, name, bases, dict):
        print("Инициализация нового класса {}".format(name))
        return super(MetaClass, cls).__init__(name, bases, dict)

# порождение класса на основе метакласса
SomeClass = MetaClass("SomeClass", (), {})

# обычное наследование
class Child(SomeClass):
    def __init__(self, param):
        print(param)

# получение экземпляра класса
obj = Child("Hello")
#https://proglib.io/p/python-oop
#Абстракция
#Абстрактный класс в Python - это класс, который предназначен для наследования,
# но не может быть непосредственно экземпляризирован (создан в виде объекта). Он содержит один или более абстрактных методов,
# которые должны быть реализованы в подклассах

from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14159 * self.radius ** 2

    def perimeter(self):
        return 2 * 3.14159 * self.radius

# Rectangle - это конкретный класс, который наследуется от Shape и реализует все абстрактные методы.
rectangle = Rectangle(5, 10)
print(f"Area: {rectangle.area()}, Perimeter: {rectangle.perimeter()}")

# Circle - это другой конкретный класс, также наследуемый от Shape.
circle = Circle(2)
print(f"Area: {circle.area()}, Perimeter: {circle.perimeter()}")

# Можно создать объект абстрактного класса, но это не допускается.
#try:
#    shape = Shape()
#except TypeError as e:
#    print(e)
