"""
BIM Planet No1. Знакомство с Dynamo (https://stepik.org/course/50129)
Переименование типоразмеров стен
Copyright (c) 2019 Maxim Stepannikov, https://bimplanet.org
"""

import clr # Модуль для подгрузки .NET библиотек

# Библиотеки Revit API
clr.AddReference('RevitAPI') # Основная библиотека Revit API
from Autodesk.Revit.DB import * # Указать классы для импорта

# Библиотеки Dynamo
clr.AddReference('RevitServices') # Работа с документом и транзакциями
from RevitServices.Persistence import DocumentManager as DM # Менеджер документа
from RevitServices.Transactions import TransactionManager as TM # Менеджер транзакций

# Входные переменные с исходным фрагментом имени и текстом для его замены
old,new = [str(IN[i]) for i in range (2)]

doc = DM.Instance.CurrentDBDocument # Получение файла документа

wallTypes = FilteredElementCollector(doc).OfClass(WallType).ToElements() # Выборка типоразмеров стен

# Получение списка имен типоразмеров
names = [w.get_Parameter(BuiltInParameter.ALL_MODEL_TYPE_NAME).AsString() for w in wallTypes]
namesNew = [n.replace(old,new) for n in names] # Формирование списка новых имен

TM.Instance.EnsureInTransaction(doc) # Открытие транзакции

for t,n in zip(wallTypes,namesNew): # Цикл по переименованию типоразмеров
	t.Name = n # Присвоение типоразмеру нового имени
	
TM.Instance.TransactionTaskDone() # Закрытие транзакции

OUT = wallTypes # Вывод списка типоразмеров стен из узла Python Script
