#!/bin/bash
#

#
# set -n # Uncomment to check script syntax, without execution.
# set -x # Uncomment to debug this shell script
#

TMPDIRDMG="./tmpdmg"
if [ -d "$TMPDIRDMG" ]; then
    rm -rfd $TMPDIRDMG
fi
mkdir $TMPDIRDMG

hdiutil create -size 70m -fs HFS+ -volname morinus $TMPDIRDMG/morin-big.dmg

hdiutil mount $TMPDIRDMG/morin-big.dmg

ditto -rsrcFork ./dist/Morinus.app /Volumes/morinus/Morinus.app
cp ./doc/README /Volumes/morinus/

hdiutil eject /Volumes/morinus/

DMGNAME="$TMPDIRDMG/morinus-6.2.0-r01.dmg"
echo $DMGNAME
hdiutil convert $TMPDIRDMG/morin-big.dmg -format UDZO -imagekey zlib-level=9 -o $DMGNAME

# copy dmg into distribution and archive directory
cp $DMGNAME ./dist/

DIRARCHIVE="./archive"
if [ ! -d $DIRARCHIVE ]; then
    mkdir $DIRARCHIVE
fi
cp $DMGNAME $DIRARCHIVE/

# clean up
rm -rfd $TMPDIRDMG
