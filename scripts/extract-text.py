#!/usr/bin/env python3

#Reads each eng_[target language].csv files, creates an eng.txt and [target language].txt 
#with the same number and order of sentences (but without citation info)
#It also makes does some text preprocessing to make sure that: 
#1) Punctuation is correctly identified and counted as a token
#2) Extra white space is removed

import csv
import re
import os
import pandas as pd
from global_var import src_language, targetpath, xmltype, punct, caps, directme

if punct == 'yes':
    with open('./{}/_GENERAL_/sentences-{}.csv'.format(directme, xmltype), 'r') as csv_file:
        print('Now stripping punctuation and creating {}.csv'.format(src_language))
        csv_reader = csv.reader(csv_file, delimiter=',')
        finalsrc = []
        for row in csv_reader:
            sent_id = row[0]
            lang = row[1]
            text = row[2]
            sentence = []
            if lang == src_language:
                sentence.append(sent_id)
                if caps == 'yes':
                    text = text.lower()
                    text = re.sub(r'([^\w\s])', ' ', text)
                    text = re.sub(' +', ' ', text)
                else:
                    text = re.sub(r'([^\w\s])', ' ', text)
                    text = re.sub(' +', ' ', text)
                sentence.append(sent_id + ' ' + text)
                finalsrc.append(sentence)
else:
    with open('./{}/_GENERAL_/sentences-{}.csv'.format(directme, xmltype), 'r') as csv_file:
        print('Now creating {}.csv'.format(src_language))
        csv_reader = csv.reader(csv_file, delimiter=',')
        finalsrc = []
        for row in csv_reader:
            sent_id = row[0]
            lang = row[1]
            text = row[2]
            sentence = []
            if lang == src_language:
                if caps == 'yes':
                    text = text.lower()
                    text  = re.sub(r'([^\w\s])', r' \1 ', text) # puts a space before and after punctuation
                    text  = re.sub(' +', ' ', text) #Removes multiple whitespaces
                    text  = re.sub('　', '', text)
                else:
                    text  = re.sub(r'([^\w\s])', r' \1 ', text) # puts a space before and after punctuation
                    text  = re.sub(' +', ' ', text) #Removes multiple whitespaces
                    text  = re.sub('　', '', text)
                sentence.append(sent_id)
                sentence.append(sent_id + ' ' + text)
                finalsrc.append(sentence) 

with open('./{}/_GENERAL_/{}.csv'.format(directme, src_language), 'w') as fi: 
    csv_writer = csv.writer(fi)
    csv_writer.writerow(["sent_id", "context"])
    csv_writer.writerows(finalsrc)

with open(targetpath) as langs:
    for line in langs:
        for target_language in line.split(','):
            print('Now extracting plain text for {}'.format(target_language))
            inputfile = csv.reader(open('./parallel-csvs/{}_{}.csv'.format(src_language, target_language), 'r'))
            outputfile = open('./{}/{}/{}'.format(directme, target_language, src_language), 'w')
            outputfile2 = open('./{}/{}/{}'.format(directme, target_language, target_language), 'w')
            for row in inputfile:
                sent_id1 = row[0]
                text1 = row[1]
                sent_id2 = row[2]
                text2 = row[3]
                if text1 == 'text':
                    continue
                if punct == 'yes':
                    text1 = re.sub(r'([^\w\s])', ' ', text1) # puts a space before and after punctuation
                    text2 = re.sub(r'([^\w\s])', ' ', text2)
                    text1 = re.sub(' +', ' ', text1) #Removes multiple whitespaces
                    text2 = re.sub(' +', ' ', text2)
                if caps == 'yes':
                    text1 = text1.lower()
                    text2 = text2.lower()
                outputfile.write(str(sent_id1) + ' ' + str(text1) + '\n')
                outputfile2.write(str(sent_id2) + ' ' + str(text2) + '\n')