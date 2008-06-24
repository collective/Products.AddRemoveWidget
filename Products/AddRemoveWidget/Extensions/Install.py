from StringIO import StringIO
from Products.CMFCore.utils import getToolByName
from Products.Archetypes.Extensions.utils import installTypes, install_subskin

from Products.AddRemoveWidget.config import *

def install(self):
    out = StringIO()
    install_subskin(self, out, GLOBALS)
    if ALWAYS_MODIFY_SUBJECT:
        portal_setup = getToolByName(self, 'portal_setup')
        portal_quickinstaller = getToolByName(self, 'portal_quickinstaller')
        profilename = 'Products.' + PROJECTNAME + ':default'
        portal_setup.runAllImportStepsFromProfile('profile-%s' % profilename, purge_old=False)
        product_name = profilename.split(':')[0]
        portal_quickinstaller.notifyInstalled(product_name)
    out.write("Successfully installed %s." % PROJECTNAME)
    return out.getvalue()
