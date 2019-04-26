"""
BIM Planet No1. Знакомство с Dynamo (https://bimplanet.org/)
Выборка элементов нескольких категорий через коллектор и цикл
MIT License, Copyright (c) 2019 Maxim Stepannikov
"""

import clr # Модуль для подгрузки .NET библиотек

# Библиотеки Revit API
clr.AddReference('RevitAPI') # Основная библиотека Revit API
from Autodesk.Revit.DB import * # Импорт всех классов

clr.AddReference('RevitServices') # Работа с документом и транзакциями
from RevitServices.Persistence import DocumentManager as DM

doc = DM.Instance.CurrentDBDocument # Получение файла документа

elems = [] # Создание пустого списка для будущих элементов

# Написание строки с именами системных категорий через запятую. Расщепляем строку разделителем.
catNames = 'OST_Walls,OST_Floors,OST_Rooms,OST_Doors'.split(',')
# catName = ['OST_Walls','OST_Floors','OST_Rooms'] # Можно просто через список строк

for cn in catNames: # Создание цикла для получение элементов каждой из категорий данного списка
	exec('cat = BuiltInCategory.'+cn) # Исполнение кода на основе поданной строки
	# Добавляем элементы в список. Если на выходе нужен плоский список - заменяем append на extend
	elems.append(FilteredElementCollector(doc).OfCategory(cat).WhereElementIsNotElementType().ToElements())
	# Заменить WhereElementIsNotElementType() на WhereElementIsElementType() для получения типоразмеров
	
OUT = elems # Вывод элементов из узла Python Script
