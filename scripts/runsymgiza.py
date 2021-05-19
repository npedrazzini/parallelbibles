#!/usr/bin/env python3

#Runs symgiza's ./run.sh script on all sentence-aligned files
#Outputs vcb, snt, cooccurrence files, and trains a bidirectional GIZA model. 
#Everything is saved in the right directory (./_OUTPUTS_/[target language])

import subprocess
import os
from global_var import src_language, targetpath, directme

with open(targetpath) as langs:
    for line in langs:
        for target_language in line.split(','):
            if not os.path.exists('./{}/{}/data/out.A3.final_symal'.format(directme, target_language)):
                subprocess.call(['./scripts/symgiza.sh', '{}'.format(src_language), '{}'.format(target_language), './{}/{}'.format(directme, target_language)])