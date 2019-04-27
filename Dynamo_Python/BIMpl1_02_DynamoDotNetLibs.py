clr.AddReference('ProtoGeometry') # Классы, аналогичные нодам Dynamo вкладки Geometry
from Autodesk.DesignScript.Geometry import * # Указать классы для импорта

clr.AddReference('DSCoreNodes') # Классы, аналогичные базовым нодам Dynamo
import DSCore # Импортирование пространства имен DSCore
clr.ImportExtensions(DSCore) # Добавление дополнительных методов к текущим классам
from DSCore import * # Указать классы для импорта

clr.AddReference('RevitNodes') # Классы, аналогичные базовым нодам Dynamo
import Revit # Импортирование пространства имен Revit
clr.ImportExtensions(Revit.Elements) # Добавление дополнительных методов к текущим классам
from Revit.Elements import * # Указать классы для импорта
