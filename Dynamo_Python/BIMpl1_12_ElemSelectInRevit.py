"""
BIM Planet No1. Знакомство с Dynamo (https://stepik.org/course/50129)
Выделение списка элементов в интерфейсе Revit
Copyright (c) 2019 Maxim Stepannikov, https://bimplanet.org
"""

import clr # Модуль для подгрузки .NET библиотек

# Библиотеки Revit API
clr.AddReference('RevitAPI') # Основная библиотека Revit API
clr.AddReference('RevitAPIUI') # Библиотека Revit API интерфейса
from Autodesk.Revit.DB import * # Импорт всех классов данного пространства имен

clr.AddReference('RevitServices') # Работа с документом и транзакциями
from RevitServices.Persistence import DocumentManager as DM # Менеджер документа

# Системные библиотеки
import System # Работа с системными типами и структурами данных .NET
from System.Collections.Generic import List # Импорт класса типизированного списка

doc = DM.Instance.CurrentDBDocument # Получение файла документа
uidoc=DM.Instance.CurrentUIApplication.ActiveUIDocument # Получение файла документа пользовательского интерфейса

# Выборка всех экземпляров стен в проекте, получение их в виде ElementId
elemIds = FilteredElementCollector(doc).OfCategory(BuiltInCategory.OST_Walls).WhereElementIsNotElementType().ToElementIds()

uidoc.Selection.SetElementIds(List[ElementId](elemIds)) # Выделение элементов в интерфейсе Revit

OUT = [doc.GetElement(id) for id in elemIds] # Вывод списка выделенных элементов из узла Python Script
