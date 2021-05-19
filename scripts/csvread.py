#!/usr/bin/env python3

#Reads sentences.csv and outputs a src_trg.csv files for each target language
#Make sure that targets.txt only contains the target languages which you need
#Creates a folder for each target language.
#Creates and saves each src_trg.csv file in the relevant target language folder


import csv
import re
import os
import pandas as pd
from global_var import xmltype, src_language, targetpath, directme

if not os.path.exists('./parallel-csvs'):
    os.mkdir('./parallel-csvs')

with open(targetpath) as langs:
    for line in langs:
        for target_language in line.split(','):
            print("Now processing {}".format(target_language))
            if not os.path.exists('./{}/{}'.format(directme, target_language)):
                os.mkdir('./{}/{}'.format(directme, target_language))
            if os.path.exists('./parallel-csvs/{}_{}.csv'.format(src_language, target_language)):
                print('{}_{}.csv already exists'.format(src_language, target_language))
            else:
                with open('./parallel-csvs/{}_{}.csv'.format(src_language, target_language), 'w') as f:
                    with open('./{}/_GENERAL_/sentences-{}.csv'.format(directme, xmltype)) as csv_file:
                        csv1 = csv.writer(f)
                        csv1.writerow(["sent_id", "text", "sent_id2", "text2"])
                        csv_reader = csv.DictReader(csv_file, delimiter=',')
                        targets = []
                        sources = []
                        for row in csv_reader:
                            target = []
                            source = []
                            sent_id = row['sent_id']
                            lang = row['lang']
                            text = row['text']
                            if lang == target_language:
                                target_id = sent_id
                                target_text  = re.sub(r'([^\w\s])', r' \1 ', text) # puts a space before and after punctuation
                                target_text  = re.sub(' +', ' ', target_text ) #Removes multiple whitespaces
                                target_text  = re.sub('　', '', target_text ) #Removes special tab (?) in Chinese files 
                                target.append(target_id)
                                target.append(target_text)
                                targets.append(target)
                            if lang == src_language:
                                src_id = sent_id
                                src_text  = re.sub(r'([^\w\s])', r' \1 ', text) # puts a space before and after punctuation
                                src_text  = re.sub(' +', ' ', src_text ) #Removes multiple whitespaces
                                src_text  = re.sub('　', '', src_text ) #Removes special tab (?) in Chinese files 
                                source.append(src_id)
                                source.append(src_text)
                                sources.append(source)
                    for rows in sources:
                        newsource = []
                        ids1 = rows[0]
                        texts1 = rows[1]
                        for item in targets:
                            ids2 = item[0]
                            texts2 = item[1]
                            if ids1 == ids2:
                                newsource.append(ids1)
                                newsource.append(texts1)
                                newsource.append(ids2)
                                newsource.append(texts2)
                                if newsource[0] != '' and newsource[1] != '' and newsource[2] != '' and newsource[3] != '':
                                    csv1.writerow([newsource[0], newsource[1], newsource[2], newsource[3]])
