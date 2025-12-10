"""CLASSMETHOD И STATICMETHOD"""
from pyglet.lib import script_path

# import datetime
#
#
# class Employee:
#     num_of_emps = 0
#     raise_amt = 1.04
#
#     def __init__(self, first, last, pay):
#         self.first = first
#         self.last = last
#         self.email = first + '.' + last + '@email.com'
#         self.pay = pay
#         Employee.num_of_emps += 1
#
#
#     def fullname(self):
#         return f'{self.first} {self.last}'
#
#
#     def apply_raise(self):
#         self.pay = int(self.pay * self.raise_amt)
#
#
#     @classmethod
#     def set_raise_amt(cls, amount):
#         cls.raise_amt = amount
#
#
#     @classmethod
#     def from_string(cls, emp_str):
#         first, last, pay = emp_str.split('-')
#         return cls(first, last, pay)
#
#
#     @staticmethod
#     def is_workday(day):
#         if day.weekday() == 5 or day.weekday() == 6:
#             return False
#
#         return True

# emp_1 = Employee('Jon', 'Snow', 50000)
# emp_2 = Employee('Ivan', 'Ivanov', 60000)

# Employee.set_raise_amt(1.05)

# print(Employee.raise_amt)
# print(emp_1.raise_amt)
# print(emp_2.raise_amt)

# emp_str_1 = 'Jon-Snow-70000'
# emp_str_2 = 'Ivan-Ivanov-30000'
# emp_str_3 = 'Elena-Nikitina-90000'

# first, last, pay = emp_str_1.split('-')
# new_emp_1 = Employee(first, last, pay)

# new_emp_1 = Employee.from_string(emp_str_1)

# print(new_emp_1.email)
# print(new_emp_1.pay)

# my_date = datetime.date(2023, 1, 31)
# print(Employee.is_workday(my_date))

# ------------------------------------------------


"""РЕЖИМЫ ДОСТУПА АТРИБУТОВ"""

# class Employee:
#     """
#     Режим доступа к атрибутам: Public: first, last
#     """
#     def __init__(self, first, last):
#         self.first = first
#         self.last = last


# emp = Employee('Jon', 'Snow')
# Обращаемся к атрибутам экземпляра класса
# print(emp.first, emp.last)

# class Employee:
#     """
#     Режим доступа к атрибутам: Protected: _first, _last
#     """
#     def __init__(self, first, last):
#         self._first = first
#         self._last = last
#
# emp = Employee('Jon', 'Snow')
# Обращаемся к атрибутам экземпляра класса
# print(emp._first, emp._last)

# class Employee:
#     """
#     Режим доступа к атрибутам: Private: __first, __last
#     """
#     def __init__(self, first, last):
#         self.__first = first
#         self.__last = last

#     def fullname(self):
#         return f'{self.__first} {self.__last}'

# emp = Employee('Jon', 'Snow')
# Обращаемся к атрибутам экземпляра класса
# print(emp.__first, emp.__last)


# ПРИМЕР С ПРИВАТНЫМИ И ЗАЩИЩЕННЫМИ МЕТОДАМИ

# class Employee:
#
#         def __init__(self, first, last):
#             self.first = first
#             self.last = last
#
#         # Приватный метод, который может быть использован только внутри класса
#         def __send_mail(self):
#             """ Функционал отправки письма """
#
#         # Защищенный метод для использования внутри текущего класса и всех класса
#         def _pay_salary(self):
#             """ Функционал выплаты зарплат """
#
#         # Публичный метод, который можно вызывать от объекта
#         def fullname(self):
#             """ Функционал полного имени сотрудника """
#             return f'{self.first} {self.last}'
#
# emp = Employee('Jon', 'Snow')
#
# print(dir(emp))
# ['_Employee__first', '_Employee__last', '__class__']
#
# print(emp._Employee__first, emp._Employee__last)

# ------------------------------------------------


"""ГЕТТЕРЫ И СЕТТЕРЫ"""

# class Employee:
#     """
#     Базовые методы
#     """
#     def __init__(self, first, last):
#         self.first = first
#         self.last = last
#         self._email = f'{self.first}.{self.last}@email.com'
#
#     def get_email(self):
#         return self._email
#
#     def set_email(self, email):
#         self._email = email
#
#
# emp_1 = Employee('John', 'Snow')
# print(emp_1.get_email())
#
# emp_1.set_email('Tim.Snow@email.com')
# print(emp_1.get_email())


# class Employee:
#     """
#     Декоратор @property
#     """
#     def __init__(self, first, last):
#         self.first = first
#         self.last = last
#
#     @property
#     def email(self):
#         return f'{self.first}.{self.last}@email.com'
#
# emp_1 = Employee('John', 'Snow')
# emp_1.first = 'Tim'
#
# print(emp_1.email)


# class Employee:
#     """
#     Пропись поведения при записи в атрибуты при помощи декоратора @property
#     """
#     def __init__(self, first, last):
#         self.first = first
#         self.last = last
#
#     # Геттер для email
#     @property
#     def email(self):
#         """Возвращает email сотрудника. К атрибуту можно обращаться без ()."""
#         return f'{self.first}.{self.last}@email.com'
#
#     @property
#     def fullname(self):
#         """Возвращает email сотрудника. К атрибуту можно обращаться без ()."""
#         return f'{self.first} {self.last}'
#
#     # Чтобы иметь возможность присваивать атрибуту fullname-значения,
#     # надо определить его сеттер. Это работает только для атрибутов с @property
#     @fullname.setter
#     def fullname(self, name):
#         """Метод срабатывает при операции присваивания."""
#         first, last = name.split(' ')
#         self.first = first
#         self.last = last
#
#     @fullname.deleter
#     def fullname(self):
#         """Использование делитера"""
#         print('Delete Name!')
#         self.first = None
#         self.last = None
#
# emp_1 = Employee('Test', 'Test')
# emp_1.fullname = 'John Snow'
# print(emp_1.first)
#
# del emp_1.fullname
# print(emp_1.fullname)

# -----------------------------------------------


"""МАГИЧЕСКИЕ МЕТОДЫ"""


# class Employee:
#     """
#     Метод: __repr__
#     """
#     def __init__(self, first, last, pay):
#         self.first = first
#         self.last = last
#         self.pay = pay
#
#     @property
#     def email(self):
#         return f'{self.first}.{self.last}@email.com'
#
#     @property
#     def fullname(self):
#         return f'{self.first} {self.last}'
#
#     def __repr__(self):
#         return f'{self.__class__.__name__}("{self.first}", "{self.last}", "{self.pay}")'
#
# emp_1 = Employee('Ivan', 'Ivanov', 50000)
# print(emp_1)
# Вывод: Employee("Ivan", "Ivanov", "50000")


# class Employee:
#     """
#     Метод: __repr__ + __str__
#     """
#     def __init__(self, first, last, pay):
#         self.first = first
#         self.last = last
#         self.pay = pay
#
#     @property
#     def email(self):
#         return f'{self.first}.{self.last}@email.com'
#
#     @property
#     def fullname(self):
#         return f'{self.first} {self.last}'
#
#     def __repr__(self):
#         return f'{self.__class__.__name__}("{self.first}", "{self.last}", "{self.pay}")'
#
#     def __str__(self):
#         return f'{self.fullname} - {self.email}'
#
# emp_1 = Employee('Ivan', 'Ivanov', 50000)
# print(emp_1)
# Вывод: Ivan Ivanov - Ivan.Ivanov@email.com


# class Employee:
#     """
#     Метод: __add__
#
#     """
#
#     def __init__(self, first, last, pay):
#         self.first = first
#         self.last = last
#         self.pay = pay
#
#     @property
#     def email(self):
#         return f'{self.first}.{self.last}@email.com'
#
#     @property
#     def fullname(self):
#         return f'{self.first} {self.last}'
#
#     def __repr__(self):
#         return f'{self.__class__.__name__}("{self.first}", "{self.last}", "{self.pay}")'
#
#     def __str__(self):
#         return f'{self.fullname} - {self.email}'
#
#     def __add__(self, other):
#         """
#         Метод срабатывает, когда используется оператор сложения.
#         В параметр other хранится то, что справа от знака +
#         """
#         return self.pay + other.pay
#
# emp_1 = Employee('Ivan', 'Ivanov', 50000)
# emp_2 = Employee('Test', 'Employee', 60000)
# print(emp_1 + emp_2)
# Вывод: 110000


# class Employee:
#
#     def __init__(self, first, last, pay):
#         self.first = first
#         self.last = last
#         self.pay = pay
#
#     @property
#     def email(self):
#         return f'{self.first}.{self.last}@email.com'
#
#     @property
#     def fullname(self):
#         return f'{self.first} {self.last}'
#
#     def __repr__(self):
#         """
#         Метод для отображения информации
#         об объекте класса в режиме отладки
#         """
#         return f'{self.__class__.__name__}("{self.first}", "{self.last}", "{self.pay}")'
#
#     def __str__(self):
#         """
#         Метод для отображения информации об объекте класса
#         для пользователей (для функции print() или str()): __str__
#         """
#         return f'{self.fullname} - {self.email}'
#
#     def __add__(self, other):
#         """
#         Метод срабатывает, когда используется оператор сложения.
#         В параметр other хранится то, что справа от знака +
#         Подобие функционала метода __add__ обладают также следующие методы:
#         - __sub__ - Операция вычитания
#         - __mul__ - Операция умножения
#         - __truediv__ - Операция деления
#         - __lt__ - Операция сравнения "<"
#         - __le__ - Операция сравнения "<="
#         - __gt__ - Операция сравнения ">"
#         - __ge__ - Операция сравнения ">="
#         - __hash__ - Демонстрация уникальности
#         - __bool__ - Возврат True или False
#         """
#         return self.pay + other.pay
#
#     def __len__(self):
#         """
#         Метод позволяющий применять функцию len(): __len__
#         """
#         return len(self.fullname)
#
#
# emp_1 = Employee('Ivan', 'Ivanov', 50000)
# emp_2 = Employee('Test', 'Employee', 60000)
#
# print(emp_1)
# # Вывод благодаря методу __repr__: Employee("Ivan", "Ivanov", "50000")
#
# print(emp_1)
# # Вывод благодаря методу __str__: Ivan Ivanov - Ivan.Ivanov@email.com
#
# print(emp_1 + emp_2)
# # Вывод благодаря методу __add__: 110000
#
# print(len(emp_1))
# # Вывод благодаря методу __len__: 11


# class StripChars:
#     """
#     Метод __call__ - это
#     метод, который позволяет сделать
#     объект класса callable-объектом
#     """
#     def __init__(self, chars):
#         """Инициализация символов для удаления"""
#         self.__chars = chars
#
#     def __call__(self, *args, **kwargs):
#         """Удаление символов из строки"""
#         return args[0].strip(self.__chars)
#
#
# st1 = StripChars('!')
# st2 = StripChars('_')
#
# print(st1('!Attention!'))
# print(st1('_Attention_'))
# print(st2('_Attention_'))


# class EvenRange:
#     """
#     Методы __iter и __next__
#     Итератор, возвращающий только четные числа в диапазоне от 0 до stop.
#     """
#     def __init__(self, stop):
#         """
#         Инициализирует итератор.
#
#         Args:
#             stop (int): Верхняя граница диапазона чисел.
#
#         Raises:
#             ValueError: Если переданное значение не является целым неотрицательным
#         """
#         if not isinstance(stop, int):
#             raise ValueError('Число должно быть целым')
#         if stop < 0:
#             raise ValueError('Число должно быть неотрицательным')
#         self.stop = stop
#
#     def __iter__(self):
#         """Возвращает итератор."""
#         self.current_value = -2
#         return self
#
#     def __next__(self):
#         """Возвращает следующее четное число в диапазоне.
#
#         Returns:
#             int: Следующее четное число.
#
#         Raises:
#             StopIteration: Если достигнута верхняя граница диапазона.
#         """
#         if self.current_value + 2 < self.stop:
#             self.current_value += 2
#             return self.current_value
#         else:
#             raise StopIteration
#
# r = EvenRange(9)
#
# print(list(r))
#
# for i in r:
#     print(i)


# class MyOpen:
#     """
#     Методы __enter__ и __exit__
#
#     Класс, который создает объект, который можно использовать
#     вместо open(), чтобы автоматически закрывать файл.
#     :param filename: имя файла
#     :param mode: режим открытия файла (по умолчанию 'r')
#     """
#     def __init__(self, filename, mode='r'):
#         self.filename = filename
#         self.mode = mode
#
#     def __enter__(self):
#         """
#         Метод, который вызывается при входе в блок контекста.
#         Он открывает файл и возвращает файловый дескриптор.
#         :return: файловый дескриптор
#         """
#         self.fp = open(self.filename, self.mode)
#         return self.fp
#
#     def __exit__(self, exc_type, exc_val, exc_tb):
#         """
#         Метод, который вызывается при выходе из блока контекста.
#         Он закрывает файл
#
#         exc_type, exc_val, exc_tb в методе __exit__ — это дополнительные
#         параметры, в которые записывается информация об исключении, если исключение
#         возникает.
#         В простых примерах не используется.
#         """
#         self.fp.close()
#
#
# with MyOpen('text.txt', 'r') as fp: # Открываем файл
#     print(fp.read()) # Читаем файл

# ------------------------------------------------


"""НАСЛЕДОВАНИЕ В PYTHON"""

# class Employee:
#
#     raise_amt = 1.04
#
#     def __init__(self, first, last, pay):
#         self.first = first
#         self.last = last
#         self.pay = pay
#
#     def fullname(self):
#         return f'{self.first} {self.last}'
#
#     def apply_raise(self):
#         self.pay = int(self.pay * self.raise_amt)
#
#
# class Developer(Employee):
#     raise_amt = 1.10
#
#
# dev_1 = Developer('Ivan', 'Ivanov', 60000)
# dev_1.apply_raise()
# print(dev_1.pay)
# print(dev_1.fullname())


# class Employee:
#     """
#     Расширение базового класса
#     """
#     def __init__(self, first, last, pay):
#         self.first = first
#         self.last = last
#         self.pay = pay
#
#     def fullname(self):
#         return print(f'{self.first} {self.last}')
#
#
# class Developer(Employee):
#     @staticmethod
#     def code():
#         print("I'm coding now!")
#
# dev_1 = Developer('Ivan', 'Ivanov', 60000)
# dev_1.fullname()
# dev_1.code()


# class Employee:
#     """
#     Переопределение метода
#     """
#     def __init__(self, first, last, pay):
#         self.first = first
#         self.last = last
#         self.pay = pay
#
#     def fullname(self):
#         return print(f'{self.first} {self.last}')
#
#     @staticmethod
#     def code(self):
#         print("I'm coding as an employee.")
#
#
# class Developer(Employee):
#
#     def code(self):
#         print(f"I'm coding as a developer now!")
#
# dev_1 = Developer('Ivan', 'Ivanov', 60000)
# dev_1.fullname()
# dev_1.code()


# class Employee:
#     """
#     Функция super()
#     """
#     def __init__(self, first, last, pay):
#         self.first = first
#         self.last = last
#         self.pay = pay
#
#     def fullname(self):
#         return print(f'{self.first} {self.last}')
#
#     @staticmethod
#     def code(self):
#         print("I'm coding as an employee.")
#
#
# class Developer(Employee):
#     raise_amt = 1.10
#     # Переопределяем метод базового класса
#     def __init__(self, first, last, pay, prog_lang):
#         # Вызываем метод базового класса
#         super().__init__(first, last, pay)
#         # Дополнительный код
#         self.prog_lang = prog_lang
#
# dev_1 = Developer('Ivan', 'Ivanov', 60000, 'Python')
# dev_2 = Developer('Petr', 'Petrov', 70000, 'Java')


# class Employee:
#     """
#     Пример
#     """
#     def work(self):
#         print('Do some work')
#
#
# class Developer(Employee):
#     def work(self):
#         super().work()
#         print('Write code')
#
# class JavaDeveloper(Developer):
#     def work(self):
#         super().work()
#         print('Write tests for code')


# class Employee:
#     """
#     Функции issubclass() и isinstance
#     """
#     def __init__(self, first, last, pay):
#         self.first = first
#         self.last = last
#         self.pay = pay
#
#     def fullname(self):
#         return print(f'{self.first} {self.last}')
#
#
# class Developer(Employee):
#     raise_amt = 1.10
#
#     def __init__(self, first, last, pay, prog_lang):
#         super().__init__(first, last, pay)
#         self.prog_lang = prog_lang
#
#     def __add__(self, other):
#         if not isinstance(other, Employee):
#             raise ValueError('Складывать можно только объекты Employee и Developer')
#         return self.pay + other.pay
#
#
# dev_1 = Developer('Ivan', 'Ivanov', 60000, 'Python')
# dev_2 = Developer('Petr', 'Petrov', 70000, 'Java')
# print(dev_1 + dev_2)
#
# emp_1 = Employee('Petr', 'Petrov', 50000)
# print(dev_1 + emp_1)
#
# print(dev_2 + 10000)


# class Employee:
#     """Базовый класс сотрудника"""
#
#     def set_salary(self):
#         """Метод для начисления зарплаты"""
#         print('Pay salary')
#
#
# class Developer(Employee):
#     """Класс разработчика"""
#     pass
#
# class Client:
#     def get_payment(self):
#         """Метод получения оплаты от клиента/"""
#         print('Get payment')
#
# system_users = [Employee(), Developer(), Developer(), Client()]
#
# for user in system_users:
#     if issubclass(user.__class__, Employee):
#         # Если класс объекта сотрудник, то начисляем зарплату
#         user.set_salary()
#     else:
#         # В случае, если объект не является сотрудником, то запрашиваем выплату
#         user.get_payment()

# ------------------------------------------------


"""МНОЖЕСТВЕННОЕ НАСЛЕДОВАНИЕ"""

# class Employee:
#     """
#     Абстрактные методы и классы
#     """
#     def work(self):
#         pass
#
# class Developer(Employee):
#     def work(self):
#         print('Пишет код')
#
# class Accountant(Employee):
#     def work(self):
#         print('Считает зарплату')
#
# emp = Employee()
# dev = Developer()
# acc = Accountant()
#
# emp.work()
# dev.work()
# acc.work()

# from abc import ABC, abstractmethod
#
# class Employee(ABC):
#     @abstractmethod
#     def work(self):
#         pass
#
# class Developer(Employee):
#     def work(self):
#         print('Пишет код')
#
# class Accountant(Employee):
#     def work(self):
#         print('Считает зарплату')
#
#
# emp = Employee()
# dev = Developer()
# acc = Accountant()
#
# emp.work()
# dev.work()
# acc.work()


# from abc import ABC, abstractmethod
#
# class Employee(ABC):
#     @abstractmethod
#     def work(self):
#         pass
#
# class Developer(Employee):
#     def work(self):
#         print('Пишет код')
#
# class Accountant(Employee):
#     def work(self):
#         print('Считает зарплату')
#
# def test_work(employee):
#     """Общий интерфейс для классов Developer и Accountant,
#     также использование их через полиморфизм"""
#     employee.work()
#
# dev = Developer()
# acc = Accountant()
#
# test_work(dev)
# test_work(acc)


# class Employee:
#     """Множественное наследование и MRO"""
#     def __init__(self, name, surname):
#         super().__init__()
#         self.name = name
#         self.surname = surname
#
# class MixinLog:
#     ID = 1
#
#     def __init__(self):
#         self.id = self.ID
#         MixinLog.ID += 1
#
#     def order_log(self):
#         print(f'{self.id}-й сотрудник')
#
#
# class Developer(Employee, MixinLog):
#     pass
#
# dev_1 = Developer('Ivan', 'Ivanov')
# dev_1.order_log()
#
# dev2 = Developer('Elena', 'Ivanova')
# dev2.order_log()


# class Point:
#     """Коллекция __dict__"""
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
# pt = Point(10, 20)
# pt.z = 100
# print(pt.__dict__)


# class PointSlots:
#     """Коллекция __slots__"""
#     MAX_VALUE = 1000
#     __slots__ = ('x', 'y')
#
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
# pts = PointSlots(10, 20)
# print(pts.x)
# print(pts.y)
# # pts.z = 100
# print(pts.MAX_VALUE)
# print(pts.__slots__)


# class Point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#     def get_set_del(self):
#         self.x += 1
#         del self.y
#         self.y = 0
#
#
# class PointSlots:
#     __slots__ = ('x', 'y')
#
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#     def get_set_del(self):
#         self.x += 1
#         del self.y
#         self.y = 0
#
# pt = Point(10, 20)
# pts = PointSlots(10, 20)
#
# import timeit
#
# t1 = timeit.timeit(pt.get_set_del) # Без __slots
# t2 = timeit.timeit(pts.get_set_del) # Cо __slots
#
# print(t1, t2)
# print((t1 - t2) / t1 * 100)


# Некоторые правила по использованию __slots__ с наследованием

# class Parent:
#     __slots__ = ['a', 'b']
#
# class Child(Parent):
#     pass
#
# child = Child()
# child.a = 1
# child.b = 2
# child.c = 3 # Нет ошибки,
# # так как в дочернем классе не определена коллекция __slots__


# class Parent:
#     __slots__ = ['a', 'b']
#
# class Child(Parent):
#     __slots__ = ['c', 'd']
#
# child = Child()
# child.a = 1
# child.b = 2
# child.c = 3
# child.d = 4
# child.e = 5 # Ошибка, так как атрибут 'e' не определен
# # ни в __slots__ родительского, ни в __slots__ дочернего класса


# class Parent:
#     pass
#
# class Child(Parent):
#     __slots__ = ['c', 'd']
#
# child = Child()
# child.c = 1
# child.d = 2
# child.a = 0 # Ошибка, так как атрибут 'a' не определен
# # в __slots__ дочернего класса


# ------------------------------------------------

"""Исключения"""

# class Exp:
#     """
#     Распространение исключений v.1
#     """
#     def func1(self):
#         self.func2()
#         print('Штатное завершение func1()')
#
#     def func2(self):
#         self.func3()
#         print('Штатное завершение func2()')
#
#     def func3(self):
#         print(100 / 0)
#         print('Штатное завершение func3()')
#
# ob = Exp()
# try:
#     ob.func1()
# except ZeroDivisionError:
#     print('Ошибка где-то в цепочке вызовов func1().')
#
# print('Выход.')


# class Exp:
#
#     def func1(self):
#         try:
#             self.func2()
#         except ZeroDivisionError:
#             print('Ошибка в func1()')
#         print('Штатное завершение func1()')
#
#     def func2(self):
#         try:
#             self.func3()
#         except ZeroDivisionError:
#             print('Ошибка в func2()')
#         print('Штатное завершение func2()')
#
#     def func3(self):
#         try:
#             print(100 / 0)
#         except ZeroDivisionError:
#             print('Ошибка в func3()')
#         print('Штатное завершение func3()')
#
# ob = Exp()
#
# try:
#     ob.func1()
# except ZeroDivisionError:
#     print('Ошибка где-то в классе Exp.')
#
# print('Выход.')


# class ShellScriptError:
#     """
#     ПОЛЬЗОВАТЕЛЬСКИЕ ИСКЛЮЧЕНИЯ И ИНСТРУКЦИЯ RAISE.
#     Общий класс исключения для скриптов
#     """
#     def __init__(self, *args, **kwargs):
#         self.message = args[0] if args else 'Неизвестная ошибка скрипта.'
#
#     def __str__(self):
#         return self.message
#
#
# class ShellScriptEmpty(ShellScriptError):
#     """Класс исключения при отсутствии кода скрипта"""
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         self.message = args[0] if args else 'Файл пустой'
#
#
# class ShellScriptShebang(ShellScriptError):
#     """Класс исключения при отсутствии shebang"""
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         self.message = args[0] if args else 'В файле отсутствует shebang'
#
# class ShellScript:
#     """Класс для работы с шелл-скриптами"""
#     def __init__(self, script: str):
#         if not script:
#             raise ShellScriptEmpty
#         elif script[0:2] !='#!':
#             raise ShellScriptShebang
#         else:
#             self.script = script
#
#     def evaluate(self):
#         """Код исполнения скрипта"""
#         pass
#
# content = ''
# try:
#     script = ShellScript(content)
# except ShellScriptEmpty:
#     print('Отсутствует текс скрипта.')
# except ShellScriptShebang:
#     print('Добавьте шебанг в скрипт.')
# except ShellScriptError:
#     print('Ошибка при работе скрипта.')





















































