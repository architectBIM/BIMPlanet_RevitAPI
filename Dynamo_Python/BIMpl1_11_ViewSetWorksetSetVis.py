"""
BIM Planet No1. Знакомство с Dynamo (https://stepik.org/course/50129)
Изменение настроек видимости рабочих наборов на видах
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

views = [] # Пустой список для отфильтрованных видов

doc = DM.Instance.CurrentDBDocument # Получение файла документа

# Полный список планов этажей и их шаблонов
allViews = FilteredElementCollector(doc).OfClass(ViewPlan).ToElements()

for view in allViews: # Цикл для фильтрации исходного списка видов и шаблонов
	if view!=None and not view.IsTemplate: # Исключение нулевых значений и шаблонов вида
		views.append(view) # Добавление видов, прошедших проверку, в новый список

worksets = FilteredWorksetCollector(doc).OfKind(WorksetKind.UserWorkset) # Получение рабочих наборов

TM.Instance.EnsureInTransaction(doc) # Открытие транзакции

for v in views: # Цикл для поочередной обработки видов
	for ws in worksets: # Цикл для поочередной работы с каждым из рабочих наборов
		if 'BIM Planet' in ws.Name: # Проверка имени рабочего набора
			# Скрытие рабочего набора, прошедшего проверку, на виде
			v.SetWorksetVisibility(ws.Id, WorksetVisibility.Hidden)

TM.Instance.TransactionTaskDone() # Закрытие транзакции

OUT = # Вывод списка видов из узла Python Script
