"""
BIM Planet No1. Знакомство с Dynamo (https://stepik.org/course/50129)
Методы получение параметров различными методами и для различных типов данных
Copyright (c) 2019 Maxim Stepannikov, https://bimplanet.org
"""

import clr # Модуль для подгрузки .NET библиотек

# Библиотеки Revit API
clr.AddReference('RevitAPI') # Основная библиотека Revit API
from Autodesk.Revit.DB import * # Импорт всех классов

# Библиотеки Dynamo
clr.AddReference('RevitServices') # Работа с документом и транзакциями
from RevitServices.Persistence import DocumentManager as DM

# Системные библиотеки
import System # Работа с системными типами и структурами данных .NET
from System import Guid # Импорт необходимого .NET класса для получения общего параметра по его Guid

# Объекты Revit, полученные через Dynamo, необходимо разворачивать для работы с ними через Revit API
elems = UnwrapElement(IN[0]) # Разворачивание списка элементов Revit
vals = [] # Создание пустого списка для значений параметров

# Документ и транзакции
doc = DM.Instance.CurrentDBDocument # Получение файла документа

# Создание цикла для получения значений параметров нескольких элементов
for el in elems: # Получение значений параметров различными методами и для различных типов данных

	# Получение параметра по имени. Возвращает все найденные параметры. Получение значения в виде ElementId
	level = doc.GetElement(el.GetParameters('Level')[0].AsElementId()) # GetElement() - объект по его Id
	# Получение параметров по системному имени. Получение значения в виде строки
	number = el.get_Parameter(BuiltInParameter.ROOM_NUMBER).AsString()
	# Получение параметров по Guid. Получение значения в виде целого числа
	stepik = el.get_Parameter(Guid('8d4e4384-2203-4066-b1b6-52c40c69eb15')).AsInteger()
	# Получение параметра по имени. Метод возвращает первый найденный параметр
	area = el.LookupParameter('Area').AsDouble()/(1/0.3048**2) # Получение значения в виде дробного числа
	# (1/0.3048**2) - перевод из квадратных футов в квадратные метры
	
	vals.append([level,number,stepik,area]) # Добавление полученных значений в список
		
OUT = vals # Вывод значений из узла Python Script
