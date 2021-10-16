#!/bin/sh
#Usage:
#./extract.sh
#
################################################################

#program path
ROOT=./scripts
extractoccurrence=$ROOT/extract_occur.py
mdskriging=$ROOT/MDSandKriging.py

source ./parallels-venv/bin/activate
chmod a+rwx "$extractoccurrence"
chmod a+rwx "$mdskriging"

#__begin timer___
START=$(date +%s)

#---------------
$extractoccurrence

#---------------
$mdskriging

#___end timer___
END=$(date +%s)
DIFF=$(( $END - $START ))
echo "It took $DIFF seconds"

echo ***Progam end***