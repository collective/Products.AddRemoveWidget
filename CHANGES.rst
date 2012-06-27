Changelog
=========

1.5.0 (2012-06-27)
------------------

- Moved code to github:
  https://github.com/collective/Products.AddRemoveWidget
  [maurits]

- Moved from i18n to locales.
  [maurits]


1.4.5 (2011-08-06)
------------------

* Added ordering support as an optional feature.
  [piv]

* Removed 'unicodeTestIn' call. This fixes #14.
  [jaroel/maerteijn]

* Add empty element to submitContainer when no items are selected. Fixes #13.
  [jaroel/maerteijn]


1.4.4 (2010-08-16)
------------------

* Added ``|nothing`` to tabindex in template for not breaking Plone 4 when 
  using comboboxwidget.
  [saily]


1.4.3 (2010-08-06)
------------------

- Fixed similar problem in ComboboxWidget.
  See http://plone.org/products/addremovewidget/issues/4
  [maurits]

- Fixed iteration over non-sequence in case of blank field, in
  combination with LinguaPlone.  Patch by Izak Burger.
  See http://plone.org/products/addremovewidget/issues/12
  [maurits]

- Fixed ASCII decode error by filtering the field vocabulary.
  See http://plone.org/products/addremovewidget/issues/10
  [dunlapm]


1.4.2 (2009-11-04)
------------------

- Rerelease as someone seems to have done a 1.4.1 egg release at the
  end of last year already.
  [maurits]


1.4.1 (2009-11-04)
------------------

* Added ``|nothing`` to tabindex in template for not breaking Plone 4.
  [maartenkling]

* Removed old-style install, added profile, moved version to setup.py.
  [jensens]


1.4 - 2008-09-10
----------------

* Fixed error with duplication of entries in the Available column. This fixes
  issue #9.
  [dunlapm]

* Fixed the long-standing issue with non-ascii characters in terms gathered from
  the catalog. Proper vocabularies should be just that, proper vocabularies
  where the "id" of a term consists of ascii characters and the "value" can
  contain unicode. Check the Vocabulary class in Products.Archetypes for a
  reference.
  [dunlapm]


1.3 - 2008-07-03
----------------

* Removed unecessary style attribute on the combo box text field which broke
  rendering in IE 7.
  [fschulze]


1.2 - 2008-06-27
----------------

* Added logic for drop-in replacement of KeywordWidget
  [dunlapm]


1.1 - 2008-05-20
----------------

* Initial release
