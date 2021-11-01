#!/usr/bin/env python3

## Adapted from the code for Wälchli's (2010) paper 
## (https://journals.dartmouth.edu/cgi-bin/WebObjects/Journals.woa/xmlpage/1/article/356?htmlOnce=yes)
## This version merges all translations with less than 10 occurrences with NULLs and generates MDS plots (no kriging, 2 plots for each lang >/< 30 occurences)

import os
from os import write
import numpy as np
from math import *
import pandas as pd
import csv
from collections import Counter
from global_var import directme, target_word, mdsyesorno, krigingyesorno

if mdsyesorno == 'no':
    print('Done, your .csv file for "{}" was saved in "./{}/_TARGETWORDS_/{}/{}.csv"!'.format(target_word, directme, target_word, target_word))
else:
    if krigingyesorno == 'yes':
        print('Now converting {}.csv to {}.tsv'.format(target_word, target_word))
        data = pd.read_csv('./{}/_TARGETWORDS_/{}/{}.csv'.format(directme, target_word, target_word), keep_default_na=False, na_values=['_'])
        data.drop('context', inplace=True, axis=1)
        data.rename(columns={'sent_id':''},inplace=True)
        data.to_csv('./{}/_TARGETWORDS_/{}/{}-nocontext.csv'.format(directme, target_word, target_word), index=True)
        
        print('Now removing the column "context" from {}.tsv'.format(target_word))
        with open('./{}/_TARGETWORDS_/{}/{}-nocontext.csv'.format(directme, target_word, target_word)) as csvin, open('./{}/_TARGETWORDS_/{}/{}.txt'.format(directme, target_word, target_word), 'w') as tsvout:
            csvin = csv.reader(csvin)
            tsvout = csv.writer(tsvout, delimiter='\t')
            for row in csvin:
                tsvout.writerow(row)

        filename=target_word 

        def readt(f): #reads text file
            s=[]
            arow=[]
            try:
                with open('./{}/_TARGETWORDS_/{}/'.format(directme, target_word)+f+".txt",'r') as f:
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
                with open('./{}/_TARGETWORDS_/{}/'.format(directme, target_word)+f+'-data.txt','w') as f:  #assumes your project directory also includes your R project
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
                with open('./{}/_TARGETWORDS_/{}/'.format(directme, target_word)+f+'-MDS.R','w') as f: 
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

        #with open('./{}/_TARGETWORDS_/{}/'.format(directme, target_word)+filename+'-whole.txt', 'w') as fi:
            #csv_writer = csv.writer(fi, delimiter= '\t')
            #csv_writer.writerows(aband)
        #print('Now writing {}-whole.txt'.format(filename))

        #with open('./{}/_TARGETWORDS_/{}/'.format(directme, target_word)+filename+"-wholeor.txt", 'w') as fi:
            #csv_writer = csv.writer(fi, delimiter= '\t')
            #csv_writer.writerows(abor)
        #print('Now writing {}-wholeor.txt'.format(filename))

        with open('./{}/_TARGETWORDS_/{}/'.format(directme, target_word)+filename+"-matrix.txt", 'w') as fi:
            csv_writer = csv.writer(fi, delimiter= '\t')
            csv_writer.writerows(abmix)
        print('Now writing {}-matrix.txt'.format(filename))

        #with open('./{}/_TARGETWORDS_/{}/'.format(directme, target_word)+filename+"-rownames.txt", 'w') as fi:
            #csv_writer = csv.writer(fi, delimiter= '\t')
            #csv_writer.writerow(arow)
        #print('Now writing {}-rownames.txt'.format(filename))

        #with open('./{}/_TARGETWORDS_/{}/'.format(directme, target_word)+filename+"-colnames.txt", 'w') as fi:
            #csv_writer = csv.writer(fi, delimiter= '\t')
            #csv_writer.writerow(acol)
        #print('Now writing {}-colnames.txt'.format(filename))

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

        print('Now generating R script {}-MDS.R'.format(target_word))

        t="" #t is a string that will contain the R code 
        t+="#Add the full path to \""+filename+"-data.txt\" and \""+filename+"-matrix.txt\" or start an R project in the same directory as those files\n"
        t+="install.packages('Cairo') #if you haven't already\n"
        t+="library(Cairo)\n" 
        t+="data<-read.table(\""+filename+"-data.txt\")\n"
        t+="matr<-read.table(\""+filename+"-matrix.txt\")\n" #the R code pre-specifies the halfway identical count, if "matrix" 
        t+="datacsv<-read_csv(\""+filename+".csv\")\n" #the R code pre-specifies the halfway identical count, if "matrix" 
        t+="cmd<-cmdscale(matr,k=20)\n" #saves file with row and colnames
        t+="cont<- as.vector(datacsv$context)\n"
        t+="x<-cmd[,1];y<-cmd[,2]\n"
        t+="df<- data.frame(x,y)\n\n"

        t+="CairoPDF(file='{}-plots.pdf',16, 12)".format(target_word)
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
        data2 = pd.read_csv('./{}/_TARGETWORDS_/{}/{}.csv'.format(directme, target_word, target_word), keep_default_na=False, na_values=['_'])
        data2.rename(columns={'sent_id':''},inplace=True)
        sentids = data2['']
        finalaa.index=sentids
        finalaa.columns=acol
        finalaa.to_csv('./{}/_TARGETWORDS_/{}/{}-data.txt'.format(directme, target_word, target_word), sep="\t")

        print(finalaa)

        aa = finalaa
        
        writercode(filename,t) #writes the R code to a text file 
        p="# This script assumes you created an empty directory ./plotly-outputs under the current directory\n"
        p+="# You can search+replace ./plotly-outputs below with the full path if needed\n"
        p+="library(tidyverse)\n"
        p+="library(plotly)\n" 
        p+="data<-read.table(\""+filename+"-data.txt\") # Skip if already in your env \n"
        p+="matr<-read.table(\""+filename+"-matrix.txt\") # Skip if already in your env \n" #the R code pre-specifies the halfway identical count, if "matrix" 
        p+="datacsv<-read_csv(\""+filename+".csv\")\n" #the R code pre-specifies the halfway identical count, if "matrix" 
        p+="cmd<-cmdscale(matr,k=20) # Skip if already in your env \n" #saves file with row and colnames
        p+="cont<- as.vector(datacsv$context)\n"
        p+="x<-cmd[,1];y<-cmd[,2] # Skip if already in your env \n"
        p+="df<- data.frame(x,y) # Skip if already in your env \n\n"
        for i in range(len(langall)):
            p+="fig <- plot_ly()\n"
            p+="fig <- fig %>% \n"
            p+="layout(title = \'"+langall[i][0][0]+"\') %>% \n"
            p+="add_trace(type='scatter', mode='markers', x = x, y = y, color=data$"+langall[i][0][0]+", hovertext=cont)\n"
            p+="htmlwidgets::saveWidget(as_widget(fig), \"./plotly-outputs/"+langall[i][0][0]+".html\")\n\n"
        with open('./{}/_TARGETWORDS_/{}/{}-plotly.R'.format(directme, target_word, target_word),'w') as f: 
            f.write(p+"\n")
    else:
        data = pd.read_csv('./{}/_TARGETWORDS_/{}/{}.csv'.format(directme, target_word, target_word), keep_default_na=False, na_values=['_'])
        data.drop('context', inplace=True, axis=1)
        data.rename(columns={'sent_id':''},inplace=True)
        data.to_csv('./{}/_TARGETWORDS_/{}/{}-nocontext.csv'.format(directme, target_word, target_word), index=True)
        
        print('Now removing the column "context" from {}.tsv'.format(target_word))
        with open('./{}/_TARGETWORDS_/{}/{}-nocontext.csv'.format(directme, target_word, target_word)) as csvin, open('./{}/_TARGETWORDS_/{}/{}.txt'.format(directme, target_word, target_word), 'w') as tsvout:
            csvin = csv.reader(csvin)
            tsvout = csv.writer(tsvout, delimiter='\t')
            for row in csvin:
                tsvout.writerow(row)

        filename=target_word 

        def readt(f): #reads text file
            s=[]
            arow=[]
            try:
                with open('./{}/_TARGETWORDS_/{}-MDS/'.format(directme, target_word)+f+".txt",'r') as f:
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
                with open('./{}/_TARGETWORDS_/{}/'.format(directme, target_word)+f+'-data.txt','w') as f:  #assumes your project directory also includes your R project
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
                with open('./{}/_TARGETWORDS_/{}/'.format(directme, target_word)+f+'-MDS.R','w') as f: 
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

        #with open('./{}/_TARGETWORDS_/{}/'.format(directme, target_word)+filename+'-whole.txt', 'w') as fi:
            #csv_writer = csv.writer(fi, delimiter= '\t')
            #csv_writer.writerows(aband)
        #print('Now writing {}-whole.txt'.format(filename))

        #with open('./{}/_TARGETWORDS_/{}/'.format(directme, target_word)+filename+"-wholeor.txt", 'w') as fi:
            #csv_writer = csv.writer(fi, delimiter= '\t')
            #csv_writer.writerows(abor)
        #print('Now writing {}-wholeor.txt'.format(filename))

        with open('./{}/_TARGETWORDS_/{}/'.format(directme, target_word)+filename+"-matrix.txt", 'w') as fi:
            csv_writer = csv.writer(fi, delimiter= '\t')
            csv_writer.writerows(abmix)
        print('Now writing {}-matrix.txt'.format(filename))

        #with open('./{}/_TARGETWORDS_/{}/'.format(directme, target_word)+filename+"-rownames.txt", 'w') as fi:
            #csv_writer = csv.writer(fi, delimiter= '\t')
            #csv_writer.writerow(arow)
        #print('Now writing {}-rownames.txt'.format(filename))

        #with open('./{}/_TARGETWORDS_/{}/'.format(directme, target_word)+filename+"-colnames.txt", 'w') as fi:
            #csv_writer = csv.writer(fi, delimiter= '\t')
            #csv_writer.writerow(acol)
        #print('Now writing {}-colnames.txt'.format(filename))

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
            acholi6=[]
            for j in range(len(acholi4)):
                if acholi4[j][0] > 30:
                    acholi5+=[acholi4[j][1]]
                else:
                    acholi6+=[acholi4[j][1]]
            langall+=[[[acol[i]],acholi5]]
            langall2+=[[[acol[i]],acholi6]]

        print('Now generating R script {}-MDS.R'.format(target_word))

        t="" #t is a string that will contain the R code 
        t+="#Add the full path to \""+filename+"-data.txt\" and \""+filename+"-matrix.txt\" or start an R project in the same directory as those files\n"
        t+="data<-read.table(\""+filename+"-data.txt\")\n"
        t+="matr<-read.table(\""+filename+"-matrix.txt\")\n" #the R code pre-specifies the halfway identical count, if "matrix" 
        # is changed to "wholeor" or "wholeand" here or in the R code text file, one of the other distance matrices is used for the plots
        #t+="coln<-read.table(\""+filename+"-colnames.txt\")[,1]\n"
        #t+="rown<-read.table(\""+filename+"-rownames.txt\")[,1]\n"
        #t+="rown->rownames(matr)->colnames(matr)\n"
        #t+="write.table(matr,\""+filename+"-matrix.txt\")\n"
        t+="cmd<-cmdscale(matr,k=20)\n" #saves file with row and colnames
        t+="x<-cmd[,1];y<-cmd[,2]\n\n"
        #t+="plot(x,y,col=\"white\"); text(x,y,rown,cex=.6)\n" #plots dimensions 1 and 2 with rowname labels

        t+="category<-function(u,v,w,c){\n"
        t+="for(i in 1:length(u)) points(x[u[i]],y[u[i]],col=v, cex=c, pch=w)\n"
        t+="return()}\n" #a function category in R is defined which plots points of u in x and y with defined color, size and shape

        #color, shape and size symbols for the plots in R are determined arbitrarily, too many actually, 11 would be enough
        col1=["#e6194B","#3cb44b","#ffe119","#4363d8","#f58231","#42d4f4","#fabed4","#dcbeff","#fffac8","#aaffc3","#000075","#ffffff","#000000","#808000","#911eb4", "#bfef45", "#ffd8b1"]
        shape1=[16,17,18,15,16,17,18,15,16,17,18,15,16,17,18,15,16,17,18,15,16,17,18,15,16,17,18,15,16,17,18,15,16,17,18,15,16,17,18,15,16,17,18,15,16,17,18,15,16,17,18,15,16,17,18,15,16,17,18,15,16,17,18] #defines the shape of the symbols
        size1=[1.4,1.4,1.4,1.4,1.4,1.4,1.4,1.4,1.4,1.4,1.4,1.4,1.4,1.4,1.4,1.4,1.4,1.4,1.4,1.4,1.4,1.4,1.4,1.4,1.4,1.4,1.4,1.4,1.4,1.4,1.4,1.4,1.4,1.4,1.4,1.4,1.4,1.4,1.4,1.4,1.4,1.4,1.4,1.4,1.4,1.4]
        t+="pdf(file='./{}/{}-plots.pdf', width = 16, height = 12)".format(directme,target_word)
        for i in range(len(langall)):
            langlen=len(langall[i][1])
            langlen2 = len(langall2[i][1])
            t+="\n\nh<-data[,rep("+str(i+1)+",2)]\n"
            t+="h[,2]<-c(1:"+str(len(aa))+")\n"
            t+="split(h,h[,1])->g\n"
            t+="par(mar = c(5,4,4,8))\n"
            t+="plot(x,y, main=\""+langall[i][0][0]+"(> 30 occ.)"+"\",xlab=\"Dimension 1\",ylab=\"Dimension 2\",cex=.5)\n"

            for j in range(langlen):
                if langall[i][1][j] == 'NULL':
                    t+="category(g$\""+langall[i][1][j]+"\"[,2],\""+"#BEBEBE"+"\","+"15"+","+"1.5"+")\n"
                else:
                    t+="category(g$\""+langall[i][1][j]+"\"[,2],\""+col1[j]+"\","+str(shape1[j])+","+str(size1[j])+")\n"
            t+="legend(\"topright\", title = 'Translations', inset=c(-0.09,0), cex=.9, xpd=TRUE, legend=c(" #the legend is positioned in the upper left corner, if this turns out to be inconvenient
        #replace all instances of "min(x),max(y)" by the coordinates where the legend should appear in the R code
            for j in range(langlen):
                t+="\""+langall[i][1][j]+"\","
            t=t[:-1]
            t+="),col=c("
            for j in range(langlen):
                if langall[i][1][j] == 'NULL':
                    t+="\""+"#676565"+"\","
                else:
                    t+="\""+col1[j]+"\","
            t=t[:-1]
            t+=")," 
            t+="pch=c("
            for j in range(langlen):
                if langall[i][1][j] == 'NULL':
                    t+="15,"
                else:
                    t+=str(shape1[j])+","
            t=t[:-1]
            t+="),bty=\"n\",pt.cex=c("
            for j in range(langlen):
                if langall[i][1][j] == 'NULL':
                    t+="1.5,"
                else:
                    t+=str(size1[j])+","
            t=t[:-1]
            t+="))\n"

            t+="plot(x,y, main=\""+langall2[i][0][0]+"(< 30 occ.)"+"\",xlab=\"Dimension 1\",ylab=\"Dimension 2\",cex=.5)\n"
            
            for j in range(langlen2):
                if langall2[i][1][j] == 'NULL':
                    t+="category(g$\""+langall2[i][1][j]+"\"[,2],\""+"#BEBEBE"+"\","+"15"+","+"1.5"+")\n"
                else:
                    t+="category(g$\""+langall2[i][1][j]+"\"[,2],\""+col1[j]+"\","+str(shape1[j])+","+str(size1[j])+")\n"
            t+="legend(\"topright\", title = 'Translations', inset=c(-0.09,0), cex=.9, xpd=TRUE, legend=c(" #the legend is positioned in the upper left corner, if this turns out to be inconvenient
        #replace all instances of "min(x),max(y)" by the coordinates where the legend should appear in the R code
            for j in range(langlen2):
                t+="\""+langall2[i][1][j]+"\","
            t=t[:-1]
            t+="),col=c("
            for j in range(langlen2):
                if langall2[i][1][j] == 'NULL':
                    t+="\""+"#BEBEBE"+"\","
                else:
                    t+="\""+col1[j]+"\","
            t=t[:-1]
            t+=")," 
            t+="pch=c("
            for j in range(langlen2):
                if langall2[i][1][j] == 'NULL':
                    t+="15,"
                else:
                    t+=str(shape1[j])+","
            t=t[:-1]
            t+="),bty=\"n\",pt.cex=c("
            for j in range(langlen2):
                if langall2[i][1][j] == 'NULL':
                    t+="1.5,"
                else:
                    t+=str(size1[j])+","
            t=t[:-1]
            t+="))\n"
        t+="dev.off()"

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
        data2 = pd.read_csv('./{}/_TARGETWORDS_/{}/{}.csv'.format(directme, target_word, target_word), keep_default_na=False, na_values=['_'])
        data2.rename(columns={'sent_id':''},inplace=True)
        sentids = data2['']
        finalaa.index=sentids
        finalaa.columns=acol
        finalaa.to_csv('./{}/_TARGETWORDS_/{}/{}-data.txt'.format(directme, target_word, target_word), sep="\t")

        print(finalaa)

        aa = finalaa
        
        writercode(filename,t) #writes the R code to a text file 