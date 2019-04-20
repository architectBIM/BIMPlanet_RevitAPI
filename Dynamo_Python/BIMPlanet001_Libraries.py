# Importing clr (Common Language Runtime) module. This allows to import additional .NET assemblies and extension methods to out script
import clr
# Importing RevitServices.dll assembly
clr.AddReference('RevitServices') # AddReference method allows to add custom *.dll file to the reference list of clr
