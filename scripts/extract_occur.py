#!/usr/bin/env python3

import pandas as pd
import csv
import re
import os
import shutil
import glob

directme = input('Enter name of GIZA model (e.g. "model1-UC-P"): ')
if not os.path.exists('./{}/_TARGETWORDS_'.format(directme)):
    os.mkdir('./{}/_TARGETWORDS_'.format(directme))

src_path = glob.glob("{}/_GENERAL_/*.csv".format(directme))
src_path = ','.join(src_path)
src_path = src_path.split(',')
basename = os.path.basename(src_path[0])
src_language = os.path.splitext(basename)[0]

targets = []
filenames = glob.glob("{}/*.csv".format(directme))
filenames = ','.join(filenames)
filenames = filenames.split(',')
for file in filenames: 
    target_language = os.path.basename(file)
    target_language = os.path.splitext(target_language)[0]
    targets.append(target_language)
targets = sorted(targets)
targets = ','.join(targets)

anotherword = 'yes'

while anotherword != 'no':
    target_word = input("What word do you want to look up (NB: search is case insensitive)? ")
    target_expression = r'(?i)\b' + target_word + r'\s'

    if os.path.exists('./{}/_TARGETWORDS_/{}'.format(directme, target_word)):
        shutil.rmtree('./{}/_TARGETWORDS_/{}'.format(directme, target_word))
        os.mkdir('./{}/_TARGETWORDS_/{}'.format(directme, target_word))
    else:
        os.mkdir('./{}/_TARGETWORDS_/{}'.format(directme, target_word))

    occurrences = []
    with open('./{}/_GENERAL_/{}.csv'.format(directme, src_language), 'r') as csv_file:
        print('Extracting all occurrences of {} from the {} file'.format(target_word, src_language))
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            sent_id = row[0]
            text = row[1]
            matches = re.findall(target_expression, text)
            for match in matches:
                newmatch = []
                newmatch.append(sent_id)
                newmatch.append(text)
                match = re.sub(' ', '', match)
                newmatch.append(match)
                occurrences.append(newmatch)
    with open('./{}/_TARGETWORDS_/{}.csv'.format(directme, target_word), 'w') as fi: 
        csv_writer = csv.writer(fi)
        csv_writer.writerow(["sent_id", "context", "{}".format(src_language)])
        csv_writer.writerows(occurrences) 

    df1 = pd.read_csv('./{}/_TARGETWORDS_/{}.csv'.format(directme, target_word))
    df1 = df1.astype(dtype={'context': 'string'})
    df1.context = df1.context.str.strip()
    df1.to_csv('./{}/_TARGETWORDS_/{}.csv'.format(directme, target_word), index=False)

    for target_language in targets.split(','):
        if os.path.exists('./{}/{}.csv'.format(directme, target_language)):
            print('Now extracting all sentences in {} containing a translation of {}'.format(target_language, target_word))
            targ = pd.read_csv('./{}/{}.csv'.format(directme, target_language))
            orig = pd.read_csv('./{}/_TARGETWORDS_/{}.csv'.format(directme, target_word)) 
            mergedcsv = pd.merge(orig,targ, how='left')
            mergedcsv.to_csv('./{}/_TARGETWORDS_/{}/{}-{}.csv'.format(directme, target_word, target_language, target_word))
        else:
            print('{}.csv does not exist, so it was skipped'.format(target_language))

    df = pd.read_csv('./{}/_TARGETWORDS_/{}.csv'.format(directme, target_word))

    for target_language in targets.split(','):
        if os.path.exists('./{}/{}.csv'.format(directme, target_language)):
            print('Now adding a "{}" column to {}.csv with the parallels'.format(target_language, target_word))
            with open('./{}/_TARGETWORDS_/{}/{}-{}.csv'.format(directme, target_word, target_language, target_word)) as csv_file:
                csv_reader = csv.DictReader(csv_file, delimiter= ',')
                column = []
                sentenceids = []
                for row in csv_reader:
                    targ = row['targ']
                    sent_id = row['sent_id']
                    if targ != '':
                        if sent_id not in sentenceids:
                            sentenceids.append(sent_id)
                            pattern = target_expression + r'\(([^)]+|)\)' 
                            matches = re.findall(pattern,targ)
                            for i in matches:
                                if i == '':
                                    column.append('NULL')
                                else:
                                    column.append(i)
                        else: 
                            continue
                    else:
                        column.append('NA')
            df['{}'.format(target_language)] = column
                    
    df['context'] = df['context'].str.split(n=1).str[1]
    df.to_csv('./{}/_TARGETWORDS_/{}.csv'.format(directme, target_word), index=False)

    shutil.rmtree('./{}/_TARGETWORDS_/{}'.format(directme, target_word))
    
    print('Done, your .csv file for "{}" was saved in "./{}/_TARGETWORDS_/{}.csv"!'.format(target_word, directme, target_word))
    
    anotherword = input("Do you want to look up another word (enter 'yes' or 'no', default: no)? ") or 'no'

if anotherword == 'no':
    print('All done, your final .csv file for "{}" was saved in "./{}/_TARGETWORDS_/{}.csv"!'.format(target_word, directme, target_word))