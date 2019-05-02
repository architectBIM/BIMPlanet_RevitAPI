"""
BIM Planet No1. Знакомство с Dynamo (https://stepik.org/course/50129)
Присвоение значений параметров различных типов данных
Copyright (c) 2019 Maxim Stepannikov, https://bimplanet.org
"""

import clr # Модуль для подгрузки .NET библиотек

# Библиотеки Revit API
clr.AddReference('RevitAPI') # Основная библиотека Revit API
from Autodesk.Revit.DB import * # Импорт всех классов

# Системные библиотеки
import System # Работа с системными типами и структурами данных .NET
from System import Guid # Импорт необходимого .NET класса для получения общего параметра по его Guid

# Библиотеки Dynamo
clr.AddReference('RevitServices') # Работа с документом и транзакциями
from RevitServices.Persistence import DocumentManager as DM
from RevitServices.Transactions import TransactionManager as TM

# Задание сразу нескольких входных переменных через конструкцию List Comprehension
elems,lev = [UnwrapElement(IN[i]) for i in range(2)] # В скобках - количество переменных
# Документ и транзакции
doc = DM.Instance.CurrentDBDocument # Получение файла документа

TM.Instance.EnsureInTransaction(doc) # Открытие транзакции

for el in elems: # цикл для присвоения значений параметров всем элементам списка
	el.GetParameters('Upper Limit')[0].Set(lev.Id) # Присвоение нового уровня через ElementId
	el.get_Parameter(BuiltInParameter.ROOM_NUMBER).Set('No1') # Присвоение строки
	stepik = el.get_Parameter(Guid('8d4e4384-2203-4066-b1b6-52c40c69eb15')).Set(1) # Присвоение целого числа
	el.LookupParameter('Limit Offset').Set(1200.5/304.8) # Присвоение дробного числа (перевод футов в метры)
	
TM.Instance.TransactionTaskDone() # Закрытие транзакции

OUT = elems
