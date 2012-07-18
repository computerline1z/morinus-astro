"""
This is a setup.py script generated by py2applet

Usage:
    python setup.py py2app
"""

from setuptools import setup

PROG_NAME = 'Morinus'
PROG_VERSION = '6.2.0'
AUTHOR_NAME = 'Robert Nagy (Hungary)'
AUTHOR_EMAIL = 'robert.pluto@gmail.com'

YEAR = 2012

APP = ['src/morinus.py']
DATA_FILES = ['src/Res', 'src/Hors', 'src/SWEP']
PLIST = dict(CFBundleName = PROG_NAME,
	#CFBundleIconFile = 'Editra.icns',
	CFBundleShortVersionString = PROG_VERSION,
	CFBundleGetInfoString = PROG_NAME + " " + PROG_VERSION,
	CFBundleExecutable = PROG_NAME,
	CFBundleIdentifier = 'org.morinus.%s' % PROG_NAME.title(),
	#CFBundleDocumentTypes = [dict(CFBundleTypeExtensions=fextents,
	#	CFBundleTypeIconFile='editra_doc',
	#	CFBundleTypeRole="Editor"
	#),
	#                         ],
	CFBundleTypeMIMETypes = ['text/plain',],
	CFBundleDevelopmentRegion = 'English',
	# TODO: Causes errors with the system menu translations and text rendering
	#             CFBundleLocalizations = ['English', 'Spanish', 'French', 'Japanese'],
	#             ['de_DE', 'en_US', 'es_ES', 'fr_FR',
	#                                      'it_IT', 'ja_JP', 'nl_NL', 'nn_NO',
	#                                      'pt_BR', 'ru_RU', 'sr_SR', 'tr_TR',
	#                                      'uk_UA', 'zh_CN'],
	#      NSAppleScriptEnabled="YES",
	NSHumanReadableCopyright = u"Copyright %s 2005-%d" % (AUTHOR_NAME, YEAR)
)
PY2APP_OPTIONS = dict(arch='i386',
	argv_emulation=True,
	plist = PLIST,
	optimize=True)

setup(
    app=APP,
	version = PROG_VERSION,
    data_files=DATA_FILES,
    options={'py2app': PY2APP_OPTIONS},
    setup_requires=['py2app'],
)