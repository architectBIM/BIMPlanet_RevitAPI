# Importing clr (Common Language Runtime) module. This allows to import additional .NET assemblies and extension methods to out script
import clr # To see various methods and properties of clr you can use dir(clr) command

# Adding various .NET assemblies (*.dll) to the reference list of clr. From this list you can import various namespaces and classes.
clr.AddReference('RevitServices') # Assembly for working with Revit document and committing transactions in it

