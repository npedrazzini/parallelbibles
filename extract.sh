#!/bin/sh
#Usage:
#./preprocess.sh
#
################################################################

#program path
ROOT=./scripts
extractoccurrence=$ROOT/extract_occur.py

source ./parallels-venv/bin/activate
chmod a+rwx "$extractoccurrence"

#__begin timer___
START=$(date +%s)

#---------------
$extractoccurrence

#___end timer___
END=$(date +%s)
DIFF=$(( $END - $START ))
echo "It took $DIFF seconds"

echo ***Progam end***