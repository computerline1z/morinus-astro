#!/bin/bash
#

#
# set -n # Uncomment to check script syntax, without execution.
# set -x # Uncomment to debug this shell script
#
 
# Error codes
wrong_params=5
interrupted=99
default_error=1
 
# Function to echo in color. Don't supply color for normal color.
echo_color()
{
  message="$1"
  color="$2"
 
  red_begin="\033[01;31m"
  green_begin="\033[01;32m"
  yellow_begin="\033[01;33m"
  color_end="\033[00m"
 
  # Set color to normal when there is no color
  [ ! "$color" ] && color_begin="$color_end"
 
  if [ "$color" == "red" ]; then
    color_begin="$red_begin"
  fi
 
  if [ "$color" == "green" ]; then
    color_begin="$green_begin"
  fi
 
  if [ "$color" == "yellow" ]; then
    color_begin="$yellow_begin"
  fi
 
  echo -e "$color_begin" "$message" "$color_end"
}

end()
{
  message="$1"
  exit_status="$2"
 
  if [ -z "$exit_status" ]; then
    exit_status="0"
  fi
 
  if [ ! "$exit_status" -eq "0" ]; then
    echo_color "$message" "red"
  else
    echo_color "$message" "green"
  fi
 
  if [ "$exit_status" -eq "$wrong_params" ]; then
    dohelp
  fi
 
  exit $exit_status
}
 
# Define function to call when SIGTERM is received
#   1 - Terminal line hangup
#   2 - Interrupt program
#   3 - Quit program
#  15 - Software termination signal
trap "end 'Interrupted' $interrupted" 1 2 3 15
 
dohelp()
{
  echo ""
  echo "createdmg script"
  echo ""
  echo "    creates dmg for morinus distribution"
  echo ""
  echo "    options:"
  echo "       --dmg dmg-name   creates dmg with the dmg.name.dmg"
  echo "       --help     		displays help"
  echo ""
  echo "    examples:"
  echo "        createdmg.sh --dmg morinus-6.2.0-r03"
  echo "            creates dmg with with the name morinus-6.2.0-r03.dmg"
  echo ""
 
}


# options check
prev_params=$* 
opt_dmgfile=""
while [ -n "$*" ]; do
  flag=$1
  value=$2
 
  case "$flag" in
    "--help")
      dohelp
      exit
    ;;
    "--dmg")
      opt_dmgfile="$value"
      shift
    ;;
    *)
      end "unknown option $flag. Type --help" "$wrong_params"
    ;;
  esac
 
  shift
done
if [ -z "$opt_dmgfile" ]; then
  end "--dmg not given" $wrong_params
fi

echo "--> created dmg: $opt_dmgfile.dmg"

#
#	main script
#
TMPDIRDMG="./tmpdmg"
DMGNAME="$TMPDIRDMG/$opt_dmgfile.dmg"

if [ -d "$TMPDIRDMG" ]; then
    rm -rfd $TMPDIRDMG
fi
mkdir $TMPDIRDMG

hdiutil create -size 97m -fs HFS+ -volname morinus $TMPDIRDMG/morin-big.dmg

hdiutil mount $TMPDIRDMG/morin-big.dmg

ditto -rsrcFork ./dist/Morinus.app /Volumes/morinus/Morinus.app
cp ./doc/README /Volumes/morinus/

hdiutil eject /Volumes/morinus/

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
rm ./dist/*.dmg
