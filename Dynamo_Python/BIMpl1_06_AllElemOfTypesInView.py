"""
BIM Planet No1. Знакомство с Dynamo (https://stepik.org/course/50129)
Выборка элементов нескольких классов на активном виде через фильтр
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
from System import Type # Импорт класса Type, необходимого для создания типизированного списка классов
from System.Collections.Generic import List # Импорт класса типизированного списка

doc = DM.Instance.CurrentDBDocument # Получение файла документа

types = [FamilyInstance,Wall,Floor] # Создание списка необходимых классов
typeList = List[Type]() # Создание пустого типизированного списка c типом данных Type (класс)

for t in types: # Создание цикла для добавления классов в типизированный список
	typeList.Add(t) # Добавляем элементы в типизированный список методом Add

# Создание фильтра. Меняем False на True, если надо исключить элементы, а не оставить их в коллекторе
filter = ElementMulticlassFilter(typeList,False)
# Получение элементов на активном виде с примененным фильтром по нескольким классам
elems = FilteredElementCollector(doc,doc.ActiveView.Id).WherePasses(filter).ToElements()

OUT = elems
