"""
BIM Planet No1. Знакомство с Dynamo (https://stepik.org/course/50129)
Выборка элементов нескольких категорий на активном виде через фильтр
Copyright (c) 2019 Maxim Stepannikov, https://bimplanet.org
"""

import clr # Модуль для подгрузки .NET библиотек

# Библиотеки Revit API
clr.AddReference('RevitAPI') # Основная библиотека Revit API
from Autodesk.Revit.DB import * # Импорт всех классов

clr.AddReference('RevitServices') # Работа с документом и транзакциями
from RevitServices.Persistence import DocumentManager as DM # Класс по работе с документом Revit

# Системные библиотеки
import System # Работа с системными типами и структурами данных .NET
from System.Collections.Generic import List # Импортируем класс типизированного списка

doc = DM.Instance.CurrentDBDocument # Получение файла документа

cats = List[BuiltInCategory]() # Создание пустого типизированного списка c типом данных BuiltInCategory

catNames = ['OST_Walls','OST_Floors','OST_Rooms'] # Список имен системных категорий через запятую

for cn in catNames: # Создание цикла для добавления категорий в типизированный список
	exec('cat = BuiltInCategory.'+cn) # Исполнение кода на основе поданной строки
	cats.Add(cat)# Добавляем элементы в типизированный список

# Создание фильтра. Меняем False на True, если надо исключить элементы, а не оставить их в коллекторе
filter = ElementMulticategoryFilter(cats,False)
# Получение элементов на активном виде с примененным фильтром по нескольким категориям
elems = FilteredElementCollector(doc,doc.ActiveView.Id).WherePasses(filter).ToElements()
	
OUT = elems # Вывод элементов из узла Python Script
