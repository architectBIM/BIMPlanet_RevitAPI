"""
BIM Planet No1. Знакомство с Dynamo (https://bimplanet.org/)
Компактный мини-шаблон нода Python Script
MIT License, Copyright (c) 2019 Maxim Stepannikov
"""

import clr # Модуль для подгрузки .NET библиотек

# Библиотеки Revit API
clr.AddReference('RevitAPI') # Основная библиотека Revit API
clr.AddReference('RevitAPIUI') # Библиотека Revit API интерфейса
from Autodesk.Revit.DB import * # Указать классы для импорта
# from Autodesk.Revit.UI import * # Убрать решетку (если надо) и указать классы

# Библиотеки Dynamo
clr.AddReference('RevitNodes') # Конвертация элементов и геометрии
import Revit # Расширяем исходные методы классов через ImportExtensions
clr.ImportExtensions(Revit.GeometryConversion)
clr.ImportExtensions(Revit.Elements)
clr.AddReference('RevitServices') # Работа с документом и транзакциями
from RevitServices.Persistence import DocumentManager as DM
from RevitServices.Transactions import TransactionManager as TM

# Системные библиотеки
import System # Работа с системными типами и структурами данных .NET
from System.Collections.Generic import * # Можно конкретно указать List
import sys # Настройки интерпретатора IronPython, путь к библиотекам
sys.path.append(r'C:\Program Files (x86)\IronPython 2.7\Lib')

# Документ и транзакции
doc = DM.Instance.CurrentDBDocument # Получение файла документа
# uidoc = DM.Instance.CurrentUIApplication.ActiveUIDocument # Интерфейс
TM.Instance.EnsureInTransaction(doc) # Открытие транзакции
### Действия внутри транзакции ###
TM.Instance.TransactionTaskDone() # Закрытие транзакции
