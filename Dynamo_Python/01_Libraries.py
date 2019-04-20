""" Importing clr (Common Language Runtime) module. This allows to add additional .NET assemblies and extension methods to out script """

import clr # Use dir(clr) command to see various methods and properties of clr

""" Adding various .NET assemblies (*.dll) to the reference list of clr. From this list you can import various namespaces and classes
Use clr.References command to see the whole list of references """

# References to Dynamo libraries
clr.AddReference('ProtoGeometry') # DesignScript library for working with geometry
clr.AddReference('DSCoreNodes') # Dynamo core library
clr.AddReference('RevitNodes') # Dynamo library for various operations with Revit elements
clr.AddReference('RevitServices') # Dynamo library for working with Revit document and committing transactions in it

# References to Revit API libraries
clr.AddReference('RevitAPI') # Revit API library
clr.AddReference('RevitAPIUI') # Revit API User Interface library

""" Importing necessary classes and extension methods to our script """
