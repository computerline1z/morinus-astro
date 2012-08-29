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
  echo "createsrczip script"
  echo ""
  echo "    creates source archive for morinus distribution"
  echo ""
  echo "    options:"
  echo "       --zip zip-name   creates zip archive with the zip-name.zip"
  echo "       --help     		displays help"
  echo ""
  echo "    examples:"
  echo "        createsrczip.sh --zip morinus-6.2.0-r03"
  echo "            creates zip archive with the name morinus-6.2.0-r03.zip"
  echo ""
 
}


# options check
prev_params=$* 
opt_zipfile=""
while [ -n "$*" ]; do
  flag=$1
  value=$2
 
  case "$flag" in
    "--help")
      dohelp
      exit
    ;;
    "--zip")
      opt_zipfile="$value"
      shift
    ;;
    *)
      end "unknown option $flag. Type --help" "$wrong_params"
    ;;
  esac
 
  shift
done
if [ -z "$opt_zipfile" ]; then
  end "--zip not given" $wrong_params
fi

echo "--> created zip: $opt_zipfile.zip"

#
#	main script
#
TMPDIRSRC="./tmpsrc"
DIRSRC="./src"
DIRSWEP="./swep_src"
ZIPNAME="$TMPDIRSRC/$opt_zipfile.zip"

if [ ! -d "$DIRSRC" ]; then
  	end "src directory does not exist in current path"
fi

if [ -d "$TMPDIRSRC" ]; then
    rm -rfd $TMPDIRSRC
fi
mkdir $TMPDIRSRC

ditto $DIRSRC $TMPDIRSRC
rm -fr $TMPDIRSRC/*.pyc
rm -fr $TMPDIRSRC/SWEP/Ephem/*.se1
ditto $DIRSWEP $TMPDIRSRC/SWEP/src
cp ./doc/README $TMPDIRSRC

# zip and copy src archive into archive directory
DIRARCHIVE="./archive"
if [ ! -d $DIRARCHIVE ]; then
    mkdir $DIRARCHIVE
fi
zip -r $ZIPNAME $TMPDIRSRC
cp $ZIPNAME $DIRARCHIVE/

# clean up
rm -rfd $TMPDIRSRC
