#!/usr/bin/env python3

# Takes monolingual xml files of either opus (https://opus.nlpl.eu/bible-uedin.php, rightmost lang-id column) or proiel format.
# There are different methods for preprocessing opus and proiel xmls, so this is asked by the prompt
# Outputs a .csv with three columns for each verse, for each language. E.g:
# b.GEN.1.1  rus  В начале сотворил Бог небо и землю.
# Creates a directory _OUTPUTS_, where all outputs will be stored
# Creates a directory _GENERAL_ inside _OUTPUTS_ where all general (language non-specific) and final outputs will be saved

from bs4 import BeautifulSoup
import glob
import csv
import re
import os
import pandas as pd

if __name__=='__main__':
    xmltype = input('Are you about to process opus XMLs, proiel XMLs, or mixed? (Enter opus, proiel or mixed) ') or 'mixed'
    xmlpath = './original-xmls'
    src_language = input('Choose a source language for your model (ISO-639-2/b code) (default: eng): ') or 'eng'
    targetpath = input('Press ENTER to use all other languages as targets or enter only the ones to be used (comma-separated ISO-639-2/b codes, e.g. "arm,chu,grc,lat"): ') or './targets.txt'
    punct = input('Do you want to remove all punctuation? Answer "yes" or "no" (default: yes): ') or 'yes'
    caps = input('Do you want to convert all uppercases to lowercases? Answer "yes" or "no" (default: yes): ') or 'yes'
    directme = input('Enter a name for your model (no spaces!): ') or 'noname'

    with open('./scripts/global_var.py','w') as vars:
        vars.write("xmltype = '%s'" % xmltype)
        vars.write("\nxmlpath = '%s'" % xmlpath)
        vars.write("\nsrc_language = '%s'" % src_language)
        vars.write("\ntargetpath = '%s'" % targetpath)
        vars.write("\ndirectme = '%s'" % directme)
        vars.write("\npunct = '%s'" % punct)
        vars.write("\ncaps = '%s'" % caps)

if xmltype == 'mixed':

    if not os.path.exists('./{}'.format(directme)):
        os.mkdir('./{}'.format(directme))
    if not os.path.exists('./{}/_GENERAL_'.format(directme)):
        os.mkdir('./{}/_GENERAL_'.format(directme))
    
    final = []

    filenames1 = glob.glob("{}/*.xml".format(xmlpath + '/opus-xmls'))
    
    for file in filenames1:
        with open(file, 'r') as tei:
            print('Now checking {}...'.format(file))
            soup = BeautifulSoup(tei, 'lxml')
            lang = soup.find('language')
            langid = lang.get('iso639')
            if targetpath != './targets.txt':
                if langid == src_language:
                    print("Processing file: {}".format(file))
                    for i in soup.find_all('seg'):
                        listtext = []
                        ids = i.get('id')
                        text = i.get_text(strip=True)
                        if text != '': # removes blank lines with blank text 
                            listtext.append(ids)
                            listtext.append(langid)
                            listtext.append(text)
                            final.append(listtext)
                else:
                    for target_language in targetpath.split(','):
                        if langid == target_language:
                            print("Processing file: {}".format(file))
                            for i in soup.find_all('seg'):
                                listtext = []
                                ids = i.get('id')
                                text = i.get_text(strip=True)
                                if text != '': # removes blank lines with blank text 
                                    listtext.append(ids)
                                    listtext.append(langid)
                                    listtext.append(text)
                                    final.append(listtext)
                        else:
                            continue
            else:
                print("Processing file: {}".format(file))
                for i in soup.find_all('seg'):
                    listtext = []
                    ids = i.get('id')
                    text = i.get_text(strip=True)
                    if text != '': # removes blank lines with blank text 
                        listtext.append(ids)
                        listtext.append(langid)
                        listtext.append(text)
                        final.append(listtext)

    filenames2 = glob.glob("{}/*.xml".format(xmlpath + '/proiel-xmls'))
    proieltokens = []
    for file in filenames2:
        print('Now checking {}...'.format(file))
        with open(file, 'r') as tei:
            soup = BeautifulSoup(tei, 'lxml')
            lang = soup.find('source')
            langid = lang.get('language')
            if targetpath != './targets.txt':
                if langid == src_language:
                    print("Processing file: {}".format(file))
                    for i in soup.find_all('token'):
                        listtext = []
                        ids = i.get('citation-part')
                        form = i.get('form')
                        if form != '':
                            listtext.append(ids)
                            listtext.append(langid)
                            listtext.append(form)
                            proieltokens.append(listtext)
                else:
                    for target_language in targetpath.split(','):
                        if langid == target_language:
                            print("Processing file: {}".format(file))
                            for i in soup.find_all('token'):
                                listtext = []
                                ids = i.get('citation-part')
                                form = i.get('form')
                                if form != '':                 
                                    listtext.append(ids)
                                    listtext.append(langid)
                                    listtext.append(form)
                                    proieltokens.append(listtext)
                        else:
                            continue
            else:
                print("Processing file: {}".format(file))
                for i in soup.find_all('token'):
                    listtext = []
                    ids = i.get('citation-part')
                    form = i.get('form')
                    if form != '':
                        listtext.append(ids)
                        listtext.append(langid)
                        listtext.append(form)
                        proieltokens.append(listtext)
    sentence = [] 
    frase = ''
    for token in proieltokens:
        sent_id = token[0]
        lang = token[1]
        text = str(token[2])
        if sent_id not in sentence:
            sentence.append(frase)
            final.append(sentence)
            sentence = []
            frase = ''
            sentence.append(sent_id)
            sentence.append(lang)
            if text != 'None':
                frase += text
                frase += ' '
        else:
            if text != 'None':
                frase += text
                frase += ' '

elif xmltype == 'opus':

    if not os.path.exists('./{}'.format(directme)):
        os.mkdir('./{}'.format(directme))
    if not os.path.exists('./{}/_GENERAL_'.format(directme)):
        os.mkdir('./{}/_GENERAL_'.format(directme))
    
    final = []

    filenames1 = glob.glob("{}/*.xml".format(xmlpath + '/opus-xmls'))
    for file in filenames1:
        with open(file, 'r') as tei:
            print('Now checking {}...'.format(file))
            soup = BeautifulSoup(tei, 'lxml')
            lang = soup.find('language')
            langid = lang.get('iso639')
            if targetpath != './targets.txt':
                if langid == src_language:
                    print("Processing file: {}".format(file))
                    for i in soup.find_all('seg'):
                        listtext = []
                        ids = i.get('id')
                        text = i.get_text(strip=True)
                        if text != '': # removes blank lines with blank text 
                            listtext.append(ids)
                            listtext.append(langid)
                            listtext.append(text)
                            final.append(listtext)
                else:
                    for target_language in targetpath.split(','):
                        if langid == target_language:
                            print("Processing file: {}".format(file))
                            for i in soup.find_all('seg'):
                                listtext = []
                                ids = i.get('id')
                                text = i.get_text(strip=True)
                                if text != '': # removes blank lines with blank text 
                                    listtext.append(ids)
                                    listtext.append(langid)
                                    listtext.append(text)
                                    final.append(listtext)
                        else:
                            continue
            else:
                print("Processing file: {}".format(file))
                for i in soup.find_all('seg'):
                    listtext = []
                    ids = i.get('id')
                    text = i.get_text(strip=True)
                    if text != '': # removes blank lines with blank text 
                        listtext.append(ids)
                        listtext.append(langid)
                        listtext.append(text)
                        final.append(listtext)
else:

    if not os.path.exists('./{}'.format(directme)):
        os.mkdir('./{}'.format(directme))
    if not os.path.exists('./{}/_GENERAL_'.format(directme)):
        os.mkdir('./{}/_GENERAL_'.format(directme))
    
    final = []

    filenames2 = glob.glob("{}/*.xml".format(xmlpath + '/proiel-xmls'))
    proieltokens = []
    for file in filenames2:
        print('Now checking {}...'.format(file))
        with open(file, 'r') as tei:
            soup = BeautifulSoup(tei, 'lxml')
            lang = soup.find('source')
            langid = lang.get('language')
            if targetpath != './targets.txt':
                if langid == src_language:
                    print("Processing file: {}".format(file))
                    for i in soup.find_all('token'):
                        listtext = []
                        ids = i.get('citation-part')
                        form = i.get('form')
                        if form != '':
                            listtext.append(ids)
                            listtext.append(langid)
                            listtext.append(form)
                            proieltokens.append(listtext)
                else:
                    for target_language in targetpath.split(','):
                        if langid == target_language:
                            print("Processing file: {}".format(file))
                            for i in soup.find_all('token'):
                                listtext = []
                                ids = i.get('citation-part')
                                form = i.get('form')
                                if form != '':                 
                                    listtext.append(ids)
                                    listtext.append(langid)
                                    listtext.append(form)
                                    proieltokens.append(listtext)
                        else:
                            continue
            else:
                print("Processing file: {}".format(file))
                for i in soup.find_all('token'):
                    listtext = []
                    ids = i.get('citation-part')
                    form = i.get('form')
                    if form != '':
                        listtext.append(ids)
                        listtext.append(langid)
                        listtext.append(form)
                        proieltokens.append(listtext)
    sentence = [] 
    frase = ''
    for token in proieltokens:
        sent_id = token[0]
        lang = token[1]
        text = str(token[2])
        if sent_id not in sentence:
            sentence.append(frase)
            final.append(sentence)
            sentence = []
            frase = ''
            sentence.append(sent_id)
            sentence.append(lang)
            if text != 'None':
                frase += text
                frase += ' '
        else:
            if text != 'None':
                frase += text
                frase += ' '

with open('./{}/_GENERAL_/sentences-{}.csv'.format(directme, xmltype), 'w') as fi:
    print("Now writing to {}".format('sentences-{}.csv'.format(xmltype)))
    csv_writer = csv.writer(fi)
    csv_writer.writerow(["sent_id", "lang", "text"])
    csv_writer.writerows(final)

dictio = {'MATT ': 'b.MAT.',
          'MARK ': 'b.MAR.',
          'LUKE ': 'b.LUK.',
          'JOHN ': 'b.JOH.',
          'ACTS ': 'b.ACT.',
          'ROM ': 'b.ROM.',
          '1COR ': 'b.1CO.',
          '2COR ': 'b.2COR.',
          'GAL ': 'b.GAL.',
          'EPH ': 'b.EPH.',
          'PHIL ': 'b.PHI.',
          'COL ': 'b.COL.',
          '1THESS ': 'b.1TH.',
          '2THESS ': 'b.2TH.',
          '1TIM ': 'b.1TI.',
          '2TIM ': 'b.2TI.',
          'TIT ': 'b.TIT.',
          'PHILEM ': 'b.PHM.',
          'HEB ': 'b.HEB.',
          'JAS ': 'b.JAM.',
          '1PET ': 'b.1PE.',
          '3JOHN ': 'b.3JO.',
          'JUDE ': 'b.JUD.',
          'REV ': 'b.REV.'}

with open('./{}/_GENERAL_/sentences-{}.csv'.format(directme, xmltype), 'r') as ar: 
    csv_reader = csv.DictReader(ar, delimiter=',')
    final = []
    for row in csv_reader:
        rows = []
        sent_id = row['sent_id']
        lang = row['lang']
        text = row['text']
        for a,b in dictio.items():
            sent_id = re.sub(a, b, sent_id)
        rows.append(sent_id)
        rows.append(lang)
        rows.append(text)
        final.append(rows)

with open('./{}/_GENERAL_/sentences-{}.csv'.format(directme, xmltype), 'w') as fi:
    csv_writer = csv.writer(fi)
    csv_writer.writerow(["sent_id", "lang", "text"])
    csv_writer.writerows(final)

if targetpath != './targets.txt':
    with open('./scripts/global_var.py','a') as vars:
        targets = open('./targets.txt', 'w')
        targets.write(str(targetpath))
        vars.write("\ntargetpath = './targets.txt'")
else:
    with open('./{}/_GENERAL_/sentences-{}.csv'.format(directme, xmltype)) as csv_file:
        csv_reader = csv.DictReader(csv_file, delimiter=',')
        langs = []
        for line in csv_reader:
            lang = line['lang']
            if lang not in langs and lang != src_language and lang != '':
                langs.append(lang)
        langs = sorted(langs)
        langs = ','.join(langs)
        targets = open('./targets.txt', 'w')
        targets.write(langs)