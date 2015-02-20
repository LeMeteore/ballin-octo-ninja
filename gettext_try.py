#!/usr/bin/env python
# -*- coding: utf-8 -*-

import gettext
from gettext import gettext as _

# pas de traduction disponible,
# message ecrit tel quel
filename = 'mylog.txt'
# les lignes du type _('...') seront captées par pygettext
# afin de generer tte clé devant etre traduite
message = _('writing a log message\n')
fp = open(filename, 'a')
fp.write(message)
fp.close()

# generer le fichier contenant le dictionnaire .pot
# pygettext -d mondomaine monscript.py

# editer l'ensemble des traduction
# msgid ""
# msgstr ""

# generer les binaires utilisés par la fonction de traduction .mo
# msgfmt mondomaine -o mondomaine.mo


# mes .pot et mes .mo sont dans un repertoire custom
locale_path = '/home/nsukami/GITHUB/ballin-octo-ninja/datas/locale/'
#print current_locale, encoding
#print gettext.find('translationex', locale_path, all=True)

language = gettext.translation ('mondomaine', locale_path,)
_ = language.gettext

# message ecrit en français
filename = 'mylog.txt'
message = _('writing a log message\n')
fp = open(filename, 'a')
fp.write(message)
fp.close()
