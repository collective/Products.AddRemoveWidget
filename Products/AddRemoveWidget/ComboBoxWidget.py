#
# ComboBoxWidget by Martin Aspeli <optilude@gmx.net>
#

from AccessControl import ClassSecurityInfo

from Products.Archetypes.Widget import TypesWidget
from Products.Archetypes.Registry import registerWidget

class ComboBoxWidget(TypesWidget):
    """Widget which presents a list box with a vocabulary, and an text box
    for optionally typing a value.
    """

    security = ClassSecurityInfo()

    _properties = TypesWidget._properties.copy()
    _properties.update({    'macro'             : 'widget_combobox',

                            # Size (num items) and width (measurement) of boxes
                            # Set width_absolute to 1 make width be fixed; else
                            #  it defines the min-width only.

                            'size'              : '7',
                            'width'             : '10em',
                            'width_absolute'    : 0,
                        },)

    security.declarePublic('process_form')
    def process_form(self, instance, field, form, empty_marker=None,
                     emptyReturnsMarker=False):
        """If a value was typed in the box, use this, else use the selected
        value.
        """
        name = field.getName()
        otherName = "%s_other" % name
        value = form.get(otherName, empty_marker)
        # If value is an empty string we check if the selection box have an usable value
        if value is empty_marker or not value:
            value = form.get(name, empty_marker)
        if (not value or value == empty_marker) and emptyReturnsMarker:
            return empty_marker
        return value, {}

registerWidget(ComboBoxWidget,
               title       = 'Combo box widget',
               description = ('Renders a HTML widget with a selection box and a box for optionally typing a value instead of selecting one',),
               used_for    = ('Products.Archetypes.Field.StringField',
                              'Products.Archetypes.Field.IntegerField')
              )
