"""
BIM Planet No1. Знакомство с Dynamo (https://stepik.org/course/50129)
Создание материалов Revit
Copyright (c) 2019 Maxim Stepannikov, https://bimplanet.org
"""

import clr # Модуль для подгрузки .NET библиотек

# Библиотеки Revit API
clr.AddReference('RevitAPI') # Основная библиотека Revit API
from Autodesk.Revit.DB import Color, Material # Необходимые классы для импорта

# Библиотеки Dynamo
clr.AddReference('RevitServices') # Работа с документом и транзакциями
from RevitServices.Persistence import DocumentManager as DM # Менеджер документа
from RevitServices.Transactions import TransactionManager as TM # Менеджер транзакций

# Входные переменные для числовых значений от 0 до 255 для каждого из трех каналов цветов
red,green,blue = [IN[i] for i in range(3)] # В каждую переменную подается от двух и более значений

mats = [] # Пустой список для будущих материалов

doc = DM.Instance.CurrentDBDocument # Получение файла документа

TM.Instance.EnsureInTransaction(doc) # Открытие транзакции

# Цикл, создающий материалы и присваивающий им соответствующие имена и значения цветов
for i in range(len(red)): # Перебор индексов элементов на основе длины списка
	r,g,b = red[i],green[i],blue[i] # Получение текущих значений цветовых каналов для материала
	name = '_'.join(['Material',str(r),str(g),str(b)]) # Генерация имени материала
	mat = doc.GetElement(Material.Create(doc,name)) # Создание материалов
	color = Color(r,g,b) # Создание цвета
	mat.Color = color # Присвоение цвета материалу
	mats.append(mat) # Добавление материала в список

TM.Instance.TransactionTaskDone() # Закрытие транзакции

OUT = mats # Вывод созданных материалов из узла Python Script
