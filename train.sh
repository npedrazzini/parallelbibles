#!/bin/sh
#Usage:
#./preprocess.sh
#
################################################################


#program path
ROOT=./scripts
xmltocsv=$ROOT/xmltocsv.py
csvread=$ROOT/csvread.py
extracttext=$ROOT/extract-text.py
rungiza=$ROOT/runsymgiza.py
readA3=$ROOT/readA3.py


source ./parallels-venv/bin/activate
chmod a+rwx "$xmltocsv"
chmod a+rwx "$csvread"
chmod a+rwx "$extracttext"
chmod a+rwx "$rungiza"
chmod a+rwx "$readA3"

#__begin timer___#
START=$(date +%s)

#__start preprocessing__#
$xmltocsv

#---------------
$csvread

#---------------
$extracttext

#__run giza__#
$rungiza

#__start postprocessing__#
$readA3

#___end timer___
END=$(date +%s)
DIFF=$(( $END - $START ))
echo "It took $DIFF seconds"

echo ***Progam end***