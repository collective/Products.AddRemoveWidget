#!/bin/bash
# Run this script to update the translations.

i18ndude rebuild-pot --pot locales/AddRemoveWidget.pot --create AddRemoveWidget .

# Sync plone po files; but commented out by default as we have no code that updates the plone.pot file.
# i18ndude sync --pot locales/plone.pot $(find . -name 'plone-.po')

i18ndude sync --pot locales/AddRemoveWidget.pot $(find . -name 'AddRemoveWidget.po')
