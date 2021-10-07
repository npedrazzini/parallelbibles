#!/usr/bin/python3

## Adapted from the code for Wälchli's (2010) paper 
## (https://journals.dartmouth.edu/cgi-bin/WebObjects/Journals.woa/xmlpage/1/article/356?htmlOnce=yes)
## This version merges all translations with less than 10 occurrences with NULLs, but generates plots AND lmaps using kriging


import os
from os import write
import numpy as np
from math import *
import pandas as pd
import csv
from collections import Counter

directme = input('Enter name of GIZA model (e.g. "model1-UC-P"): ')
word = input('Enter word which you want to plot: ')

if not os.path.exists('./{}/_TARGETWORDS_/{}.csv'.format(directme, word)):
    print('./{}/_TARGETWORDS_/{}.csv does not exist yet! Extract {} first by running ./extract.sh!'.format(directme, word, word))
else:
    os.mkdir('./{}/_TARGETWORDS_/{}-MDS'.format(directme, word))
    print('Now creating directory ./{}/_TARGETWORDS_/{}-MDS'.format(directme, word))
    print('Now converting {}.csv to {}.tsv'.format(word, word))
    data = pd.read_csv('./{}/_TARGETWORDS_/{}.csv'.format(directme, word), keep_default_na=False, na_values=['_'])
    data.drop('context', inplace=True, axis=1)
    data.rename(columns={'sent_id':''},inplace=True)
    data.to_csv('./{}/_TARGETWORDS_/{}-MDS/{}-nocontext.csv'.format(directme, word, word), index=True)
    
    print('Now removing the column "context" from {}.tsv'.format(word))
    with open('./{}/_TARGETWORDS_/{}-MDS/{}-nocontext.csv'.format(directme, word, word)) as csvin, open('./{}/_TARGETWORDS_/{}-MDS/{}.txt'.format(directme, word, word), 'w') as tsvout:
        csvin = csv.reader(csvin)
        tsvout = csv.writer(tsvout, delimiter='\t')
        for row in csvin:
            tsvout.writerow(row)

    filename=word 

    def readt(f): #reads text file
        s=[]
        arow=[]
        try:
            with open('./{}/_TARGETWORDS_/{}-MDS/'.format(directme, word)+f+".txt",'r') as f:
                acol = f.readline().split()
                i = f.readline()
                while i != "":
                    ii=i.split()
                    s += [ii[2:]]
                    arow+=[ii[1]+str(ii[0])]
                    i = f.readline()
        except:
            print("File", f, "not found")
        return s,arow,acol

    def writeforr(f,aa,acol,arow): #saves the input data text file for R
        try:
            with open('./{}/_TARGETWORDS_/{}-MDS/'.format(directme, word)+f+'-data.txt','w') as f:  #assumes your project directory also includes your R project
                tt=" "
                for i in range(len(acol)):
                    tt+=acol[i]+" "
                tt=tt[:-1]+"\n"
                f.write(tt)
                for i in range(len(aa)):
                    tt=""
                    tt+=arow[i]+" "
                    for j in range(len(acol)):
                        tt+=aa[i][j]+" "
                    tt=tt[:-1]+"\n"
                    f.write(tt)  
        except:
            print("Could not save")

    def writercode(f,p1): #saves the text file containing the R code
        try:
            with open('./{}/_TARGETWORDS_/{}-MDS/'.format(directme, word)+f+'-MDS.R','w') as f: 
                f.write(p1+"\n")
        except:
            print("Could not save")

    def hammingdist(s1,s2,data): #calculates the distance for the distance matrix in three different ways
        l=len(data[0])
        diffand=0;diffor=0;diffmix=float(0)
        avail=l
        for i in range(l):
            if data[s1][i]=="NA" or data[s2][i]=="NA": #Not attested (got rid of '_' and '#' from Walchli's code)
                avail-=1
            elif data[s1][i]==data[s2][i]:
                diffand+=1;diffor+=1;diffmix+=1
            else:
                mix=0
                sb1=data[s1][i].split("=");sb2=data[s2][i].split("=")
                for j in range(len(sb1)):
                    for k in range(len(sb2)):
                        if sb1[j]==sb2[k]:
                            mix=1
                if mix==1:
                    diffor+=1;diffmix+=0.5
        return float(1)-(float(diffand)/avail),float(1)-(float(diffor)/avail), float(1)-(float(diffmix)/avail)

    def simlines(data): #calculates the three distance matrices
        n=len(data)
        resultand=np.zeros((n,n),dtype=float)
        resultor=np.zeros((n,n),dtype=float)
        resultmix=np.zeros((n,n),dtype=float)
        for i in range(n):
            for j in range(0,i):
                resultand[i][j],resultor[i][j],resultmix[i][j]=hammingdist(i,j,data)
                resultand[j][i]=resultand[i][j];resultor[j][i]=resultor[i][j];resultmix[j][i]=resultmix[i][j]
        return resultand,resultor,resultmix

    def spalte(a):
        return(a[0][a[1]])

    print('Now creating a similarity matrix - this may take a while...')
    aa,arow,acol=readt(filename) #reads the data from a text file to aa, and the rownames and column names to arow and acol

    rowl=len(aa[0]) #some rough checks whether the data has the form it should have, in case of an Error the file must be corrected
    
    for i in range(len(aa)):
        if len(aa[i]) != rowl:
            print("Length of Row Error in Line",i,":",arow[i],"  ",len(aa[i]),"Items")
    if len(acol) != rowl:
        print("Length of Colnames Error")
    if len(arow) != len(aa):
        print("Length of Rownames Error")

    aband,abor,abmix=simlines(aa)

    with open('./{}/_TARGETWORDS_/{}-MDS/'.format(directme, word)+filename+'-whole.txt', 'w') as fi:
        csv_writer = csv.writer(fi, delimiter= '\t')
        csv_writer.writerows(aband)
    print('Now writing {}-whole.txt'.format(filename))

    with open('./{}/_TARGETWORDS_/{}-MDS/'.format(directme, word)+filename+"-wholeor.txt", 'w') as fi:
        csv_writer = csv.writer(fi, delimiter= '\t')
        csv_writer.writerows(abor)
    print('Now writing {}-wholeor.txt'.format(filename))

    with open('./{}/_TARGETWORDS_/{}-MDS/'.format(directme, word)+filename+"-matrix.txt", 'w') as fi:
        csv_writer = csv.writer(fi, delimiter= '\t')
        csv_writer.writerows(abmix)
    print('Now writing {}-matrix.txt'.format(filename))

    with open('./{}/_TARGETWORDS_/{}-MDS/'.format(directme, word)+filename+"-rownames.txt", 'w') as fi:
        csv_writer = csv.writer(fi, delimiter= '\t')
        csv_writer.writerow(arow)
    print('Now writing {}-rownames.txt'.format(filename))

    with open('./{}/_TARGETWORDS_/{}-MDS/'.format(directme, word)+filename+"-colnames.txt", 'w') as fi:
        csv_writer = csv.writer(fi, delimiter= '\t')
        csv_writer.writerow(acol)
    print('Now writing {}-colnames.txt'.format(filename))

    def mergetonulls(lst, k):
        counted = Counter(lst)
        temp_lst = []
        for el in lst:
            if counted[el] > k:
                temp_lst.append(el)    
            else:
                temp_lst.append('NULL')     
        return(temp_lst)

    langall = []
    langall2 = []
    for i in range(len(aa[0])):
        allitems=[]
        acholi = map(spalte,zip(aa,[i]*len(aa)))
        acholi = list(acholi)
        acholi = mergetonulls(acholi, 10)
        for item in acholi:
            allitems.append(item)
            acholi2 = dict.fromkeys(allitems)
        for j in acholi2:
            k=allitems.count(j)
            acholi2[j] = k
        acholi2["NA"]=0
        acholi3=list(acholi2.items())
        acholi4=[]
        for j in range(len(acholi3)):
            if acholi3[j][1] > 1:
                acholi4+=[[acholi3[j][1],acholi3[j][0]]]
        acholi4.sort(reverse=True)
        acholi5=[]
        for j in range(len(acholi4)):
            acholi5+=[acholi4[j][1]]
        langall+=[[[acol[i]],acholi5]]

    print('Now generating R script {}-MDS.R'.format(word))

    t="" #t is a string that will contain the R code 
    t+="#Add the full path to \""+filename+"-data.txt\" and \""+filename+"-matrix.txt\" or start an R project in the same directory as those files\n"
    t+="install.packages('Cairo') #if you haven't already\n"
    t+="library(Cairo)\n" 
    t+="data<-read.table(\""+filename+"-data.txt\")\n"
    t+="matr<-read.table(\""+filename+"-matrix.txt\")\n" #the R code pre-specifies the halfway identical count, if "matrix" 

    t+="cmd<-cmdscale(matr,k=20)\n" #saves file with row and colnames
    t+="x<-cmd[,1];y<-cmd[,2]\n"
    t+="df<- data.frame(x,y)\n\n"

    t+="CairoPDF(file='{}-plots.pdf',16, 12)".format(word)
    for i in range(len(langall)):
        langlen=len(langall[i][1])
        t+="\n\nh<-data[,rep("+str(i+1)+",2)]\n"
        t+="h[,2]<-c(1:"+str(len(aa))+")\n"
        t+="lmap(df,h[,1],main=\""+langall[i][0][0]+"\",levels = c(0.29,0.32,0.35),add = FALSE,position = \"topright\", grid = 30)\n"
    t+="\ndev.off()"

#explain what's going on here
    newaa = []
    for i in range(len(aa[0])):
        conv = map(spalte,zip(aa,[i]*len(aa)))
        conv = list(conv)
        newaa.append(conv)
    finalaa = []
    for lst in newaa:
        counted = Counter(lst)
        new_lst = []
        for el in lst:
            if counted[el] > 2:
                new_lst.append(el)    
            else:
                new_lst.append('NULL')
        finalaa.append(new_lst)

    finalaa = pd.DataFrame(finalaa)
    finalaa = finalaa.transpose()
    finalaa.index=arow
    finalaa.columns=acol
    finalaa.to_csv('./{}/_TARGETWORDS_/{}-MDS/{}-data.txt'.format(directme, word, word), sep="\t")

    print(finalaa)

    aa = finalaa
    
    writercode(filename,t) #writes the R code to a text file 