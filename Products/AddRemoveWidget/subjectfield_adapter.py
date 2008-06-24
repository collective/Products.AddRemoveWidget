from archetypes.schemaextender.interfaces import ISchemaModifier

from Products.ATContentTypes.content import document, event, file, folder, image, link, newsitem, topic

from Products.AddRemoveWidget import AddRemoveWidget

from zope.interface import implements
from zope.component import adapts

class SchemaModifier(object):
    implements(ISchemaModifier)
    adapts(document.ATDocument,
    #       event.ATEvent,
    #       file.ATFile,
    #       folder.ATFolder,folder.ATBTreeFolder,
    #       image.ATImage,
    #       link.ATLink,
    #       newsitem.ATNewsItem,
    #       topic.ATTopic
           )
    
    def __init__(self,context):
        self.context = context
        
    def fiddle(self,schema):
       oldlabel = schema['subject'].widget.label
       olddesc  = schema['subject'].widget.description
       schema['subject'].widget = AddRemoveWidget(label=oldlabel,
                                                  description = olddesc,
                                                  role_based_add = True)
