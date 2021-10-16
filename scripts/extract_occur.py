#!/usr/bin/env python3

import pandas as pd
import numpy as np
import csv
import re
import os
import shutil
import glob

if __name__=='__main__':
    directme = input('Enter name of GIZA model (e.g. "model1-UC-P"): ') or 'noname'
    
    with open('./scripts/global_var.py','w') as vars:
        vars.write("\ndirectme = '%s'" % directme)

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

target_word = input("What word(s) do you want to look up? (NB: 1. search is case insensitive 2. you can enter multiple words separated by a hyphen) ")
mdsyesorno = input("Do you want to perform multidimensional scaling? (yes or no; default: yes) ") or 'yes'
if mdsyesorno == 'yes':
    krigingyesorno = input("Do you want to run kriging? (yes or no; default: yes) ") or 'yes'
else:
    krigingyesorno = 'no'
NTonly = input("Do you only want to only plot the New Testament (yes or no; default: yes) ") or 'yes'

with open('./scripts/global_var.py','a') as vars:
    vars.write("\ntarget_word = '%s'" % target_word)
    vars.write("\nmdsyesorno = '%s'" % mdsyesorno)
    vars.write("\nkrigingyesorno = '%s'" % krigingyesorno)

if os.path.exists('./{}/_TARGETWORDS_/{}'.format(directme, target_word)):
    shutil.rmtree('./{}/_TARGETWORDS_/{}'.format(directme, target_word))
    os.mkdir('./{}/_TARGETWORDS_/{}'.format(directme, target_word))
    os.mkdir('./{}/_TARGETWORDS_/{}/temp'.format(directme, target_word))
else:
    os.mkdir('./{}/_TARGETWORDS_/{}'.format(directme, target_word))
    os.mkdir('./{}/_TARGETWORDS_/{}/temp'.format(directme, target_word))

listofdic = {}
listofdic["sent_id"] = []
listofdic["context"] = []
listofdic["{}".format(src_language)] = []
for target_language in targets.split(','):
    listofdic['{}'.format(target_language)] = []

target_words = target_word.split("-")
for word in target_words:
    print(word)
    if word == 'while':
        # Manually exclude 'while' as a noun and as part of 'meanwhile'. Not optimal solution though!
        target_expression = r'(?<!\bmean\s)(?<!\bthe\s)(?<!\ba\s)\b' + word + r'\s'
    else:
        target_expression = r'(?i)\b' + word + r'\s'
    
    occurrences = []
    with open('./{}/_GENERAL_/{}.csv'.format(directme, src_language), 'r') as csv_file:
        print('Extracting all occurrences of {} from the {} file'.format(word, src_language))
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
    with open('./{}/_TARGETWORDS_/{}.csv'.format(directme, word), 'w') as fi: 
        csv_writer = csv.writer(fi)
        csv_writer.writerow(["sent_id", "context", "{}".format(src_language)])
        csv_writer.writerows(occurrences) 

    df1 = pd.read_csv('./{}/_TARGETWORDS_/{}.csv'.format(directme, word))
    df1 = df1.astype(dtype={'context': 'string'})
    df1.context = df1.context.str.strip()
    df1.to_csv('./{}/_TARGETWORDS_/{}.csv'.format(directme, word), index=False)

    for target_language in targets.split(','):
        if os.path.exists('./{}/{}.csv'.format(directme, target_language)):
            print('Now extracting all sentences in {} containing a translation of {}'.format(target_language, word))
            targ = pd.read_csv('./{}/{}.csv'.format(directme, target_language))
            orig = pd.read_csv('./{}/_TARGETWORDS_/{}.csv'.format(directme, word)) 
            mergedcsv = pd.merge(orig,targ, how='left')
            mergedcsv.to_csv('./{}/_TARGETWORDS_/{}/temp/{}-{}.csv'.format(directme, target_word, target_language, word))
        else:
            print('{}.csv does not exist, so it was skipped'.format(target_language))

    df = pd.read_csv('./{}/_TARGETWORDS_/{}.csv'.format(directme, word))
    
    contextnoid = df['context'].str.split(n=1).str[1]

    for id in df['sent_id']:
        listofdic['sent_id'].append(id)
    for con in contextnoid:
        listofdic['context'].append(con)
    for sr in df["{}".format(src_language)]:
        listofdic["{}".format(src_language)].append(sr)

    for target_language in targets.split(','):
        if os.path.exists('./{}/{}.csv'.format(directme, target_language)):
            print('Now filling the "{}" column with "{}"\'s parallel'.format(target_language, word))
            with open('./{}/_TARGETWORDS_/{}/temp/{}-{}.csv'.format(directme, target_word, target_language, word)) as csv_file:
                csv_reader = csv.DictReader(csv_file, delimiter= ',')
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
                                    listofdic['{}'.format(target_language)].append('NULL')
                                else:
                                    listofdic['{}'.format(target_language)].append(i)
                        else: 
                            continue
                    else:
                        listofdic['{}'.format(target_language)].append('NA')

dffinal = pd.DataFrame(listofdic)

# Number (i.e. add a letter suffix) to sent_id, since MDS won't accept duplicate citations
letters = np.array(list('abcdefghijklmnopqrstuvwxyz'))

dffinal.to_csv('./{}/_TARGETWORDS_/{}/{}.csv'.format(directme, target_word, target_word), index=False)

# Only keep NT/OT if requested
if NTonly == 'yes':
    NTbooks = ("b.ACT.", "b.ROM.", "b.1CO.", "b.2CO.", "b.GAL.", "b.EPH.", "b.PHI.", "b.COL.", "b.1TH.", "b.2TH.", "b.1TI.", "b.2TI.", "b.TIT.", "b.PHM.", "b.HEB.", "b.JAM.", "b.1PE.", "b.2PE.", "b.1JO.", "b.2JO.", "b.3JO.", "b.JUD.", "b.MAT.", "b.MAR.", "b.LUK.", "b.JOH.")

    with open('./{}/_TARGETWORDS_/{}/{}.csv'.format(directme, target_word, target_word), 'r') as csv_file, open('./{}/_TARGETWORDS_/{}/temp/{}2.csv'.format(directme, target_word, target_word), 'w') as fi:
        csv_NT = csv.reader(csv_file, delimiter=',')
        csv_writer = csv.writer(fi)
        csv_writer.writerow(next(csv_NT))
        for row in csv_NT:
            sent_id = row[0]
            for name in NTbooks:
                if name in sent_id:
                    csv_writer.writerow(row)

    # Remove heb and amh because they only have Old Testament, and gla as it only has Mark
    dffinal = pd.read_csv('./{}/_TARGETWORDS_/{}/temp/{}2.csv'.format(directme, target_word, target_word), keep_default_na=False, na_values=['_'])
    dffinal.drop('heb', inplace=True, axis=1)
    dffinal.drop('amh', inplace=True, axis=1)
    dffinal.drop('gla', inplace=True, axis=1)
    # Add suffix from -a to -z to sent_id (MDS does not accept duplicate indexes)
    dffinal['sent_id'] = dffinal['sent_id'].astype(str) + letters[dffinal['sent_id'].groupby(dffinal['sent_id']).cumcount()]
    dffinal.to_csv('./{}/_TARGETWORDS_/{}/{}.csv'.format(directme, target_word, target_word), index=False)
else:
    dffinal['sent_id'] = dffinal['sent_id'].astype(str) + letters[dffinal['sent_id'].groupby(dffinal['sent_id']).cumcount()]
    dffinal.to_csv('./{}/_TARGETWORDS_/{}/{}.csv'.format(directme, target_word, target_word), index=False)

datapath = './{}/_TARGETWORDS_/{}/{}.csv'.format(directme, target_word, target_word)
with open('./scripts/global_var.py','a') as vars:
    vars.write("\ndatapath = '%s'" % datapath)

shutil.rmtree('./{}/_TARGETWORDS_/{}/temp'.format(directme, target_word))