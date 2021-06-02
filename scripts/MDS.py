#!/usr/bin/python3

## Adapted from the code for Wälchli's (2010) paper 
## (https://journals.dartmouth.edu/cgi-bin/WebObjects/Journals.woa/xmlpage/1/article/356?htmlOnce=yes)

import os
from os import write
import numpy as np
from math import *
import pandas as pd
import csv

directme = input('Enter name of GIZA model (e.g. "model1-UC-P"): ')
word = input('Enter word which you want to do plot: ')

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

    filename=word #replace by the name of your input data text file 

    def readt(f): #reads text file
        s=[]
        arow=[]
        try:
            with open('./{}/_TARGETWORDS_/{}-MDS/'.format(directme, word)+f+".txt",'r') as f: #Replace by the path of the folder where the input text file is saved
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
            with open('./{}/_TARGETWORDS_/{}-MDS/'.format(directme, word)+f+'-fuerR.txt','w') as f:  #specify the exact path of your R folder
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
            if data[s1][i]=="NA" or data[s2][i]=="NA": #Not attested
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

    with open('./{}/_TARGETWORDS_/{}-MDS/'.format(directme, word)+filename+"-wholemix.txt", 'w') as fi:
        csv_writer = csv.writer(fi, delimiter= '\t')
        csv_writer.writerows(abmix)
    print('Now writing {}-wholemix.txt'.format(filename))

    with open('./{}/_TARGETWORDS_/{}-MDS/'.format(directme, word)+filename+"-rownames.txt", 'w') as fi:
        csv_writer = csv.writer(fi, delimiter= '\t')
        csv_writer.writerow(arow)
    print('Now writing {}-rownames.txt'.format(filename))

    with open('./{}/_TARGETWORDS_/{}-MDS/'.format(directme, word)+filename+"-colnames.txt", 'w') as fi:
        csv_writer = csv.writer(fi, delimiter= '\t')
        csv_writer.writerow(acol)
    print('Now writing {}-colnames.txt'.format(filename))
    
    langall = []
    for i in range(len(aa[0])):
        allitems=[]
        acholi = map(spalte,zip(aa,[i]*len(aa)))
        acholi = list(acholi)
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
        acholi4=acholi4[:11]
        acholi5=[]
        for j in range(len(acholi4)):
            acholi5+=[acholi4[j][1]]
        langall+=[[[acol[i]],acholi5]]

    print('Now generating R script {}-MDS.R'.format(word))

    t="" #t is a string that will contain the R code 
    t+="data<-read.table(\""+filename+"-fuerR.txt\")\n"
    t+="matr<-read.table(\""+filename+"-wholemix.txt\")\n" #the R code pre-specifies the halfway identical count, if "wholemix" 
    # is changed to "wholeor" or "wholeand" here or in the R code text file, one of the other distance matrices is used for the plots
    t+="coln<-read.table(\""+filename+"-colnames.txt\")[,1]\n"
    t+="rown<-read.table(\""+filename+"-rownames.txt\")[,1]\n"
    t+="rown->rownames(matr)->colnames(matr)\n"
    t+="write.table(matr,\""+filename+"-wholemix.txt\")\n"
    t+="cmd<-cmdscale(matr,k=20)\n" #saves file with row and colnames
    t+="x<-cmd[,1];y<-cmd[,2]\n"
    t+="plot(x,y,col=\"white\"); text(x,y,rown,cex=.6)\n" #plots dimensions 1 and 2 with rowname labels

    t+="category<-function(u,v,w,c){\n"
    t+="for(i in 1:length(u)) points(x[u[i]],y[u[i]],col=v, cex=c, pch=w)\n"
    t+="return()}\n" #a function category in R is defined which plots points of u in x and y with defined color, size and shape

    #color, shape and size symbols for the plots in R are determined arbitrarily, too many actually, 11 would be enough
    col1=["#FF0000","#0000FF","#00FF00","#FFAA00","#00AA33","#AA00AA","#774400","#888888","#000000","#BB8800","#00FFFF","#FFFF00","#8855FF","#993300","#888888","#333333"] #defines the colors
    shape1=[15,16,17,18,15,16,17,18,15,16,17,18,15,16,17,18,15,16,17,18] #defines the shape of the symbols
    size1=[1,1.5,1.5,1.5,1,1.5,1.5,1.5,1,1.5,1.5,1.5,1,1.5,1.5,1.5,1,1.5,1.5,1.5] #defines the size of the symbols

    for i in range(len(langall)):
        langlen=len(langall[i][1])
        t+="h<-data[,rep("+str(i+1)+",2)]\n"
        t+="h[,2]<-c(1:"+str(len(aa))+")\n"
        t+="split(h,h[,1])->g\n"
        t+="plot(x,y, main=\""+langall[i][0][0]+"\",xlab=\"Dimension 1\",ylab=\"Dimension 2\",cex=.5)\n"

        for j in range(langlen):
            t+="category(g$\""+langall[i][1][j]+"\"[,2],\""+col1[j]+"\","+str(shape1[j])+","+str(size1[j])+")\n"
        t+="legend(min(x),max(y),legend=c(" #the legend is positioned in the upper left corner, if this turns out to be inconvenient
    #replace all instances of "min(x),max(y)" by the coordinates where the legend should appear in the R code
        for j in range(langlen):
            t+="\""+langall[i][1][j]+"\","
        t=t[:-1]
        t+="),col=c("
        for j in range(langlen):
            t+="\""+col1[j]+"\","
        t=t[:-1]
        t+=")," 
        t+="pch=c("
        for j in range(langlen):
            t+=str(shape1[j])+","
        t=t[:-1]
        t+="),bty=\"n\",pt.cex=c("
        for j in range(langlen):
            t+=str(size1[j])+","
        t=t[:-1]
        t+="))\n"
    
    writercode(filename,t) #writes the R code to a text file 
    writeforr(filename,aa,acol,arow) #writes the original data to a text file that is readable for R