#!/usr/bin/env python3

import os
import pandas as pd
import shutil
from global_var import targetpath, directme, xmltype

with open(targetpath) as langs:
    for line in langs:
        for target_language in line.split(','):
            if not os.path.exists('./{}/{}/data/{}.csv'.format(directme, target_language, target_language)):
                print('Now creating {}.csv'.format(target_language))
                mylist = []
                context = []
                with open('./{}/{}/data/out.A3.final_symal'.format(directme, target_language), 'r') as fi:
                    lines = fi.readlines()
                    for line in lines:
                        aligned = ''
                        compare = []
                        liness = line.split('{##}')
                        linex = liness[0].split()
                        liney = liness[1].split()
                        linez = liness[2].split()
                        parallels = [tuple(map(int, sub.split('-'))) for sub in linez]
                        for parallel in parallels:    
                            compare.append(parallel[0])
                        for token in linex:
                            if linex.index(token) not in compare:
                                aligned += token
                                aligned += ' (NULL) '
                            else:
                                parallel = [y for (x, y) in parallels if x == linex.index(token)]
                                aligned += token
                                aligned += ' ('
                                aligned += liney[int(parallel[0])]
                                aligned += ') '
                        mylist.append(aligned)
                        context.append(liness[0])
                dict = {'context': context, 'targ': mylist}
                df = pd.DataFrame(dict)
                df = df.astype(dtype={'context': 'string'})
                df['context'] = df['context'].str.strip()
                df.to_csv('./{}/{}/data/{}.csv'.format(directme, target_language, target_language), index=False)
                print(df.dtypes)
            else:
                print('Skipping {}.csv because it already exists'.format(target_language))

with open(targetpath) as langs:
    print('Now reducing clutter...') 
    for line in langs:
        for target_language in line.split(','):
            if not os.path.exists('./{}/{}/data/{}.csv'.format(directme, target_language, target_language)):
                print('Warning: {}.csv does not exist! Folder for {} was not deleted'.format(target_language, target_language))
            else:
                os.rename('./{}/{}/data/{}.csv'.format(directme, target_language, target_language), './{}/{}.csv'.format(directme, target_language))
                shutil.rmtree('./{}/{}'.format(directme, target_language))

if os.path.exists('./{}/_GENERAL_/sentences-{}.csv'.format(directme, xmltype)):
    os.remove('./{}/_GENERAL_/sentences-{}.csv'.format(directme, xmltype))

print('All done! Now go ahead and run "./extract.sh" to extract a target word and its translations')
