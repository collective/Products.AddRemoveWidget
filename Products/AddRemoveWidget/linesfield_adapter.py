from archetypes.schemaextender.interfaces import ISchemaModifier

from Products.ATContentTypes.interfaces import IATContentType

from Products.AddRemoveWidget import AddRemoveWidget
from Products.Archetypes import atapi

from zope.interface import implements
from zope.component import adapts

class SchemaModifier(object):
    implements(ISchemaModifier)
    adapts(IATContentType)
    
    def __init__(self,context):
        self.context = context
        
    def fiddle(self,schema):
        #Don't mess with fields that don't use the existing KeywordWidget and
        #aren't LinesFields
        fields = [i for i in schema.values() if isinstance(i,atapi.LinesField) and
                                       isinstance(i.widget, atapi.KeywordWidget)]
        
        for field in fields:
            oldlabel = field.widget.label
            olddesc  = field.widget.description
            field.widget = AddRemoveWidget(label=oldlabel,
                                                       description = olddesc,
                                                       role_based_add = True)
        