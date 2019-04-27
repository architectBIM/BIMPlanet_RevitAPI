"""
BIM Planet No1. Знакомство с Dynamo (https://stepik.org/course/50129)
Выборка элементов нескольких классов через коллектор и цикл
Copyright (c) 2019 Maxim Stepannikov, https://bimplanet.org
"""


import clr # Модуль для подгрузки .NET библиотек

# Библиотеки Revit API
clr.AddReference('RevitAPI') # Основная библиотека Revit API
from Autodesk.Revit.DB import * # Импорт всех классов

# Библиотеки Dynamo
clr.AddReference('RevitServices') # Работа с документом и транзакциями
from RevitServices.Persistence import DocumentManager as DM # Класс по работе с документом Revit

doc = DM.Instance.CurrentDBDocument # Получение файла документа

elems = [] # Создание пустого списка для будущих элементов
classes = [WallType,Floor,FamilyInstance] # Создание списка необходимых классов

# Создание цикла для получение элементов каждой из категорий данного списка
for cl in classes:
	
	# Добавляем элементы в список. Если на выходе нужен двухмерный список - заменяем extend на append
	elems.extend(FilteredElementCollector(doc).OfClass(cl).ToElements())
	
OUT = elems # Вывод элементов из узла Python Script
