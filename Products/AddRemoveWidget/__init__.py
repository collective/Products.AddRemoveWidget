from Products.CMFCore import utils
from Products.CMFCore.DirectoryView import registerDirectory
from config import *

registerDirectory(SKINS_DIR, GLOBALS)

from AddRemoveWidget import AddRemoveWidget
from ComboBoxWidget import ComboBoxWidget

def initialize(context):
    pass
