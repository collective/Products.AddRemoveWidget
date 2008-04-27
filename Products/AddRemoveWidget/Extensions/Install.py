from StringIO import StringIO
from Products.CMFCore.utils import getToolByName
from Products.Archetypes.Extensions.utils import installTypes, install_subskin

from Products.AddRemoveWidget.config import *

def install(self):
    out = StringIO()
    install_subskin(self, out, GLOBALS)
    out.write("Successfully installed %s." % PROJECTNAME)
    return out.getvalue()
