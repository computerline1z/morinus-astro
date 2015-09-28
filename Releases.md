# Morinus Releases #

Summary about program releases and number of downloads in each release.

## Downloads ##

|release file|# downloads|
|:-----------|:----------|
|morinus-6.2.0-[r04](https://code.google.com/p/morinus-astro/source/detail?r=04).dmg|38         |
|morinus-6.2.0-[r03](https://code.google.com/p/morinus-astro/source/detail?r=03).dmg|35         |
|morinus-6.2.0-[r02](https://code.google.com/p/morinus-astro/source/detail?r=02).dmg|11         |
|morinus-6.2.0-[r01](https://code.google.com/p/morinus-astro/source/detail?r=01).dmg|6          |
|morinus-6.2.0-[r00](https://code.google.com/p/morinus-astro/source/detail?r=00).dmg|33         |

The download count includes only dmg downloads with or without Swiss ephemeris, it does not include zip archive downloads.

## Requirements ##
Morinus runs on Mac OS X 10.5.x and higher, on Mountain Lion has not yet been tested but should run without problems due to the used infrastructure and frameworks.
## Release details ##

#### 6.2.0r05 - 2012 September 6 ####
  * added GUI functionality - closing window with Ctrl+W, standard Mac OSX behavior
  * added Swiss ephemeris compiled library into source code zip archive. Library sweastrology.so has following structure:
    * sweastrology.so: Mach-O universal binary with 2 architectures
    * sweastrology.so (for architecture i386):	Mach-O bundle i386
    * sweastrology.so (for architecture x86\_64):	Mach-O 64-bit bundle x86\_64
  * used frameworks and libraries
    * identical with previous release


#### 6.2.0r04 - 2012 August 19 ####
  * added Swiss ephemeris files
  * created two dmg packages, one with Swiss ephemeris data files and one without
  * used frameworks and libraries
    * identical with previous release

#### 6.2.0r03 - 2012 August 1 ####
  * fixed - problem with displaying of Synastry result
  * used frameworks and libraries
    * identical with previous release

#### 6.2.0r02 - 2012 July 23 ####
  * added standard Mac behavior in About menu and Quit menu
  * fixed - the bug in about menu (Mac OSX)
  * fixed - the bug in Colors picker dialog - replacing Std. Button with GenButton from wx.lib.buttons (limitation of wx framework on all platforms - see. https://groups.google.com/forum/?fromgroups#!msg/wxpython-users/cF6TSH-ywRI/exkF76HzYKwJ)
  * used frameworks and libraries
    * identical with previous release

#### 6.2.0r01 - 2012 July 22 ####
  * fix - Charts functions enabled (Transits, Revolutions, Sun-transits, Secondary directions, Elections, Square, Profections)
  * still open
    * Chart function Mundane disabled
    * Synastry disabled
  * used frameworks and libraries
    * identical with previous release

#### 6.2.0r00 ####
  * first Mac OS X release as standalone application
  * following program functions are disabled (Synastry and all Charts), the reason is bug in program Mac OS X version, on MS Windows runs everything without problems
  * there are no Swiss ephemeris data files in application bundle
  * used frameworks and libraries
    * python - Mac original 2.7.1
    * wxPython - 2.8.12.1 mac-unicode
    * Swiss Ephemeris - 1.76.00
    * PIL - 1.1.7