# This script assumes you created an empty directory ./plotly-outputs under the current directory
# You can search+replace ./plotly-outputs below with the full path if needed
library(tidyverse)
library(plotly)
data<-read.table("/Users/nilo/Desktop/parallelbibles/model2-LC-NP/_TARGETWORDS_/when/when-data.txt") # Skip if already in your env 
matr<-read.table("/Users/nilo/Desktop/parallelbibles/model2-LC-NP/_TARGETWORDS_/when/when-matrix.txt") # Skip if already in your env 
datacsv<-read_csv("/Users/nilo/Desktop/parallelbibles/model2-LC-NP/_TARGETWORDS_/when/when.csv")
cont<- read_csv("/Users/nilo/Desktop/parallelbibles/model2-LC-NP/_TARGETWORDS_/when/when-contexts.csv")
cmd<-cmdscale(matr,k=20) # Skip if already in your env 
x<-cmd[,1];y<-cmd[,2] # Skip if already in your env 
df<- data.frame(x,y) # Skip if already in your env 

write_csv(datacsv, '/Users/nilo/Desktop/app/data/eng/when/when-datacsv.csv')
write_csv(df, '/Users/nilo/Desktop/app/data/eng/when/when-df.csv')
write_csv(cont, '/Users/nilo/Desktop/app/data/eng/when/when-contexts.csv')

fig <- plot_ly()
fig <- fig %>% 
layout(title = 'eng') %>% 
add_trace(type='scatter', mode='markers', x = x, y = y, color=data$eng, hovertext=cont$context_x)
htmlwidgets::saveWidget(as_widget(fig), "./plotly-outputs/eng.html")

fig <- plot_ly()
fig <- fig %>% 
layout(title = 'acu') %>% 
add_trace(type='scatter', mode='markers', x = x, y = y, color=data$acu, hovertext=cont$"acu-context")
htmlwidgets::saveWidget(as_widget(fig), "./plotly-outputs/acu.html")

fig <- plot_ly()
fig <- fig %>% 
layout(title = 'afr') %>% 
add_trace(type='scatter', mode='markers', x = x, y = y, color=data$afr, hovertext=cont$"afr-context")
htmlwidgets::saveWidget(as_widget(fig), "./plotly-outputs/afr.html")

fig <- plot_ly()
fig <- fig %>% 
layout(title = 'ake') %>% 
add_trace(type='scatter', mode='markers', x = x, y = y, color=data$ake, hovertext=cont$"ake-context")
htmlwidgets::saveWidget(as_widget(fig), "./plotly-outputs/ake.html")

fig <- plot_ly()
fig <- fig %>% 
layout(title = 'alb') %>% 
add_trace(type='scatter', mode='markers', x = x, y = y, color=data$alb, hovertext=cont$"alb-context")
htmlwidgets::saveWidget(as_widget(fig), "./plotly-outputs/alb.html")

fig <- plot_ly()
fig <- fig %>% 
layout(title = 'amh') %>% 
add_trace(type='scatter', mode='markers', x = x, y = y, color=data$amh, hovertext=cont$"amh-context")
htmlwidgets::saveWidget(as_widget(fig), "./plotly-outputs/amh.html")

fig <- plot_ly()
fig <- fig %>% 
layout(title = 'amu') %>% 
add_trace(type='scatter', mode='markers', x = x, y = y, color=data$amu, hovertext=cont$"amu-context")
htmlwidgets::saveWidget(as_widget(fig), "./plotly-outputs/amu.html")

fig <- plot_ly()
fig <- fig %>% 
layout(title = 'ara') %>% 
add_trace(type='scatter', mode='markers', x = x, y = y, color=data$ara, hovertext=cont$"ara-context")
htmlwidgets::saveWidget(as_widget(fig), "./plotly-outputs/ara.html")

fig <- plot_ly()
fig <- fig %>% 
layout(title = 'arm') %>% 
add_trace(type='scatter', mode='markers', x = x, y = y, color=data$arm, hovertext=cont$"arm-context")
htmlwidgets::saveWidget(as_widget(fig), "./plotly-outputs/arm.html")

fig <- plot_ly()
fig <- fig %>% 
layout(title = 'baq') %>% 
add_trace(type='scatter', mode='markers', x = x, y = y, color=data$baq, hovertext=cont$"baq-context")
htmlwidgets::saveWidget(as_widget(fig), "./plotly-outputs/baq.html")

fig <- plot_ly()
fig <- fig %>% 
layout(title = 'bsn') %>% 
add_trace(type='scatter', mode='markers', x = x, y = y, color=data$bsn, hovertext=cont$"bsn-context")
htmlwidgets::saveWidget(as_widget(fig), "./plotly-outputs/bsn.html")

fig <- plot_ly()
fig <- fig %>% 
layout(title = 'bul') %>% 
add_trace(type='scatter', mode='markers', x = x, y = y, color=data$bul, hovertext=cont$"bul-context")
htmlwidgets::saveWidget(as_widget(fig), "./plotly-outputs/bul.html")

fig <- plot_ly()
fig <- fig %>% 
layout(title = 'cak') %>% 
add_trace(type='scatter', mode='markers', x = x, y = y, color=data$cak, hovertext=cont$"cak-context")
htmlwidgets::saveWidget(as_widget(fig), "./plotly-outputs/cak.html")

fig <- plot_ly()
fig <- fig %>% 
layout(title = 'ceb') %>% 
add_trace(type='scatter', mode='markers', x = x, y = y, color=data$ceb, hovertext=cont$"ceb-context")
htmlwidgets::saveWidget(as_widget(fig), "./plotly-outputs/ceb.html")

fig <- plot_ly()
fig <- fig %>% 
layout(title = 'cha') %>% 
add_trace(type='scatter', mode='markers', x = x, y = y, color=data$cha, hovertext=cont$"cha-context")
htmlwidgets::saveWidget(as_widget(fig), "./plotly-outputs/cha.html")

fig <- plot_ly()
fig <- fig %>% 
layout(title = 'chi') %>% 
add_trace(type='scatter', mode='markers', x = x, y = y, color=data$chi, hovertext=cont$"chi-context")
htmlwidgets::saveWidget(as_widget(fig), "./plotly-outputs/chi.html")

fig <- plot_ly()
fig <- fig %>% 
layout(title = 'chq') %>% 
add_trace(type='scatter', mode='markers', x = x, y = y, color=data$chq, hovertext=cont$"chq-context")
htmlwidgets::saveWidget(as_widget(fig), "./plotly-outputs/chq.html")

fig <- plot_ly()
fig <- fig %>% 
layout(title = 'chr') %>% 
add_trace(type='scatter', mode='markers', x = x, y = y, color=data$chr, hovertext=cont$"chr-context")
htmlwidgets::saveWidget(as_widget(fig), "./plotly-outputs/chr.html")

fig <- plot_ly()
fig <- fig %>% 
layout(title = 'chu') %>% 
add_trace(type='scatter', mode='markers', x = x, y = y, color=data$chu, hovertext=cont$"chu-context")
htmlwidgets::saveWidget(as_widget(fig), "./plotly-outputs/chu.html")

fig <- plot_ly()
fig <- fig %>% 
layout(title = 'cjp') %>% 
add_trace(type='scatter', mode='markers', x = x, y = y, color=data$cjp, hovertext=cont$"cjp-context")
htmlwidgets::saveWidget(as_widget(fig), "./plotly-outputs/cjp.html")

fig <- plot_ly()
fig <- fig %>% 
layout(title = 'cni') %>% 
add_trace(type='scatter', mode='markers', x = x, y = y, color=data$cni, hovertext=cont$"cni-context")
htmlwidgets::saveWidget(as_widget(fig), "./plotly-outputs/cni.html")

fig <- plot_ly()
fig <- fig %>% 
layout(title = 'cop') %>% 
add_trace(type='scatter', mode='markers', x = x, y = y, color=data$cop, hovertext=cont$"cop-context")
htmlwidgets::saveWidget(as_widget(fig), "./plotly-outputs/cop.html")

fig <- plot_ly()
fig <- fig %>% 
layout(title = 'crp') %>% 
add_trace(type='scatter', mode='markers', x = x, y = y, color=data$crp, hovertext=cont$"crp-context")
htmlwidgets::saveWidget(as_widget(fig), "./plotly-outputs/crp.html")

fig <- plot_ly()
fig <- fig %>% 
layout(title = 'cze') %>% 
add_trace(type='scatter', mode='markers', x = x, y = y, color=data$cze, hovertext=cont$"cze-context")
htmlwidgets::saveWidget(as_widget(fig), "./plotly-outputs/cze.html")

fig <- plot_ly()
fig <- fig %>% 
layout(title = 'dan') %>% 
add_trace(type='scatter', mode='markers', x = x, y = y, color=data$dan, hovertext=cont$"dan-context")
htmlwidgets::saveWidget(as_widget(fig), "./plotly-outputs/dan.html")

fig <- plot_ly()
fig <- fig %>% 
layout(title = 'deu') %>% 
add_trace(type='scatter', mode='markers', x = x, y = y, color=data$deu, hovertext=cont$"deu-context")
htmlwidgets::saveWidget(as_widget(fig), "./plotly-outputs/deu.html")

fig <- plot_ly()
fig <- fig %>% 
layout(title = 'dik') %>% 
add_trace(type='scatter', mode='markers', x = x, y = y, color=data$dik, hovertext=cont$"dik-context")
htmlwidgets::saveWidget(as_widget(fig), "./plotly-outputs/dik.html")

fig <- plot_ly()
fig <- fig %>% 
layout(title = 'dje') %>% 
add_trace(type='scatter', mode='markers', x = x, y = y, color=data$dje, hovertext=cont$"dje-context")
htmlwidgets::saveWidget(as_widget(fig), "./plotly-outputs/dje.html")

fig <- plot_ly()
fig <- fig %>% 
layout(title = 'dop') %>% 
add_trace(type='scatter', mode='markers', x = x, y = y, color=data$dop, hovertext=cont$"dop-context")
htmlwidgets::saveWidget(as_widget(fig), "./plotly-outputs/dop.html")

fig <- plot_ly()
fig <- fig %>% 
layout(title = 'epo') %>% 
add_trace(type='scatter', mode='markers', x = x, y = y, color=data$epo, hovertext=cont$"epo-context")
htmlwidgets::saveWidget(as_widget(fig), "./plotly-outputs/epo.html")

fig <- plot_ly()
fig <- fig %>% 
layout(title = 'est') %>% 
add_trace(type='scatter', mode='markers', x = x, y = y, color=data$est, hovertext=cont$"est-context")
htmlwidgets::saveWidget(as_widget(fig), "./plotly-outputs/est.html")

fig <- plot_ly()
fig <- fig %>% 
layout(title = 'ewe') %>% 
add_trace(type='scatter', mode='markers', x = x, y = y, color=data$ewe, hovertext=cont$"ewe-context")
htmlwidgets::saveWidget(as_widget(fig), "./plotly-outputs/ewe.html")

fig <- plot_ly()
fig <- fig %>% 
layout(title = 'fin') %>% 
add_trace(type='scatter', mode='markers', x = x, y = y, color=data$fin, hovertext=cont$"fin-context")
htmlwidgets::saveWidget(as_widget(fig), "./plotly-outputs/fin.html")

fig <- plot_ly()
fig <- fig %>% 
layout(title = 'fra') %>% 
add_trace(type='scatter', mode='markers', x = x, y = y, color=data$fra, hovertext=cont$"fra-context")
htmlwidgets::saveWidget(as_widget(fig), "./plotly-outputs/fra.html")

fig <- plot_ly()
fig <- fig %>% 
layout(title = 'gbi') %>% 
add_trace(type='scatter', mode='markers', x = x, y = y, color=data$gbi, hovertext=cont$"gbi-context")
htmlwidgets::saveWidget(as_widget(fig), "./plotly-outputs/gbi.html")

fig <- plot_ly()
fig <- fig %>% 
layout(title = 'gla') %>% 
add_trace(type='scatter', mode='markers', x = x, y = y, color=data$gla, hovertext=cont$"gla-context")
htmlwidgets::saveWidget(as_widget(fig), "./plotly-outputs/gla.html")

fig <- plot_ly()
fig <- fig %>% 
layout(title = 'glv') %>% 
add_trace(type='scatter', mode='markers', x = x, y = y, color=data$glv, hovertext=cont$"glv-context")
htmlwidgets::saveWidget(as_widget(fig), "./plotly-outputs/glv.html")

fig <- plot_ly()
fig <- fig %>% 
layout(title = 'got') %>% 
add_trace(type='scatter', mode='markers', x = x, y = y, color=data$got, hovertext=cont$"got-context")
htmlwidgets::saveWidget(as_widget(fig), "./plotly-outputs/got.html")

fig <- plot_ly()
fig <- fig %>% 
layout(title = 'grc') %>% 
add_trace(type='scatter', mode='markers', x = x, y = y, color=data$grc, hovertext=cont$"grc-context")
htmlwidgets::saveWidget(as_widget(fig), "./plotly-outputs/grc.html")

fig <- plot_ly()
fig <- fig %>% 
layout(title = 'gre') %>% 
add_trace(type='scatter', mode='markers', x = x, y = y, color=data$gre, hovertext=cont$"gre-context")
htmlwidgets::saveWidget(as_widget(fig), "./plotly-outputs/gre.html")

fig <- plot_ly()
fig <- fig %>% 
layout(title = 'guj') %>% 
add_trace(type='scatter', mode='markers', x = x, y = y, color=data$guj, hovertext=cont$"guj-context")
htmlwidgets::saveWidget(as_widget(fig), "./plotly-outputs/guj.html")

fig <- plot_ly()
fig <- fig %>% 
layout(title = 'heb') %>% 
add_trace(type='scatter', mode='markers', x = x, y = y, color=data$heb, hovertext=cont$"heb-context")
htmlwidgets::saveWidget(as_widget(fig), "./plotly-outputs/heb.html")

fig <- plot_ly()
fig <- fig %>% 
layout(title = 'hin') %>% 
add_trace(type='scatter', mode='markers', x = x, y = y, color=data$hin, hovertext=cont$"hin-context")
htmlwidgets::saveWidget(as_widget(fig), "./plotly-outputs/hin.html")

fig <- plot_ly()
fig <- fig %>% 
layout(title = 'hrv') %>% 
add_trace(type='scatter', mode='markers', x = x, y = y, color=data$hrv, hovertext=cont$"hrv-context")
htmlwidgets::saveWidget(as_widget(fig), "./plotly-outputs/hrv.html")

fig <- plot_ly()
fig <- fig %>% 
layout(title = 'hun') %>% 
add_trace(type='scatter', mode='markers', x = x, y = y, color=data$hun, hovertext=cont$"hun-context")
htmlwidgets::saveWidget(as_widget(fig), "./plotly-outputs/hun.html")

fig <- plot_ly()
fig <- fig %>% 
layout(title = 'ind') %>% 
add_trace(type='scatter', mode='markers', x = x, y = y, color=data$ind, hovertext=cont$"ind-context")
htmlwidgets::saveWidget(as_widget(fig), "./plotly-outputs/ind.html")

fig <- plot_ly()
fig <- fig %>% 
layout(title = 'isl') %>% 
add_trace(type='scatter', mode='markers', x = x, y = y, color=data$isl, hovertext=cont$"isl-context")
htmlwidgets::saveWidget(as_widget(fig), "./plotly-outputs/isl.html")

fig <- plot_ly()
fig <- fig %>% 
layout(title = 'ita') %>% 
add_trace(type='scatter', mode='markers', x = x, y = y, color=data$ita, hovertext=cont$"ita-context")
htmlwidgets::saveWidget(as_widget(fig), "./plotly-outputs/ita.html")

fig <- plot_ly()
fig <- fig %>% 
layout(title = 'jak') %>% 
add_trace(type='scatter', mode='markers', x = x, y = y, color=data$jak, hovertext=cont$"jak-context")
htmlwidgets::saveWidget(as_widget(fig), "./plotly-outputs/jak.html")

fig <- plot_ly()
fig <- fig %>% 
layout(title = 'jap') %>% 
add_trace(type='scatter', mode='markers', x = x, y = y, color=data$jap, hovertext=cont$"jap-context")
htmlwidgets::saveWidget(as_widget(fig), "./plotly-outputs/jap.html")

fig <- plot_ly()
fig <- fig %>% 
layout(title = 'jiv') %>% 
add_trace(type='scatter', mode='markers', x = x, y = y, color=data$jiv, hovertext=cont$"jiv-context")
htmlwidgets::saveWidget(as_widget(fig), "./plotly-outputs/jiv.html")

fig <- plot_ly()
fig <- fig %>% 
layout(title = 'kab') %>% 
add_trace(type='scatter', mode='markers', x = x, y = y, color=data$kab, hovertext=cont$"kab-context")
htmlwidgets::saveWidget(as_widget(fig), "./plotly-outputs/kab.html")

fig <- plot_ly()
fig <- fig %>% 
layout(title = 'kbh') %>% 
add_trace(type='scatter', mode='markers', x = x, y = y, color=data$kbh, hovertext=cont$"kbh-context")
htmlwidgets::saveWidget(as_widget(fig), "./plotly-outputs/kbh.html")

fig <- plot_ly()
fig <- fig %>% 
layout(title = 'kor') %>% 
add_trace(type='scatter', mode='markers', x = x, y = y, color=data$kor, hovertext=cont$"kor-context")
htmlwidgets::saveWidget(as_widget(fig), "./plotly-outputs/kor.html")

fig <- plot_ly()
fig <- fig %>% 
layout(title = 'lat') %>% 
add_trace(type='scatter', mode='markers', x = x, y = y, color=data$lat, hovertext=cont$"lat-context")
htmlwidgets::saveWidget(as_widget(fig), "./plotly-outputs/lat.html")

fig <- plot_ly()
fig <- fig %>% 
layout(title = 'lav') %>% 
add_trace(type='scatter', mode='markers', x = x, y = y, color=data$lav, hovertext=cont$"lav-context")
htmlwidgets::saveWidget(as_widget(fig), "./plotly-outputs/lav.html")

fig <- plot_ly()
fig <- fig %>% 
layout(title = 'lit') %>% 
add_trace(type='scatter', mode='markers', x = x, y = y, color=data$lit, hovertext=cont$"lit-context")
htmlwidgets::saveWidget(as_widget(fig), "./plotly-outputs/lit.html")

fig <- plot_ly()
fig <- fig %>% 
layout(title = 'mam') %>% 
add_trace(type='scatter', mode='markers', x = x, y = y, color=data$mam, hovertext=cont$"mam-context")
htmlwidgets::saveWidget(as_widget(fig), "./plotly-outputs/mam.html")

fig <- plot_ly()
fig <- fig %>% 
layout(title = 'mao') %>% 
add_trace(type='scatter', mode='markers', x = x, y = y, color=data$mao, hovertext=cont$"mao-context")
htmlwidgets::saveWidget(as_widget(fig), "./plotly-outputs/mao.html")

fig <- plot_ly()
fig <- fig %>% 
layout(title = 'mar') %>% 
add_trace(type='scatter', mode='markers', x = x, y = y, color=data$mar, hovertext=cont$"mar-context")
htmlwidgets::saveWidget(as_widget(fig), "./plotly-outputs/mar.html")

fig <- plot_ly()
fig <- fig %>% 
layout(title = 'mya') %>% 
add_trace(type='scatter', mode='markers', x = x, y = y, color=data$mya, hovertext=cont$"mya-context")
htmlwidgets::saveWidget(as_widget(fig), "./plotly-outputs/mya.html")

fig <- plot_ly()
fig <- fig %>% 
layout(title = 'nep') %>% 
add_trace(type='scatter', mode='markers', x = x, y = y, color=data$nep, hovertext=cont$"nep-context")
htmlwidgets::saveWidget(as_widget(fig), "./plotly-outputs/nep.html")

fig <- plot_ly()
fig <- fig %>% 
layout(title = 'nhg') %>% 
add_trace(type='scatter', mode='markers', x = x, y = y, color=data$nhg, hovertext=cont$"nhg-context")
htmlwidgets::saveWidget(as_widget(fig), "./plotly-outputs/nhg.html")

fig <- plot_ly()
fig <- fig %>% 
layout(title = 'nld') %>% 
add_trace(type='scatter', mode='markers', x = x, y = y, color=data$nld, hovertext=cont$"nld-context")
htmlwidgets::saveWidget(as_widget(fig), "./plotly-outputs/nld.html")

fig <- plot_ly()
fig <- fig %>% 
layout(title = 'nor') %>% 
add_trace(type='scatter', mode='markers', x = x, y = y, color=data$nor, hovertext=cont$"nor-context")
htmlwidgets::saveWidget(as_widget(fig), "./plotly-outputs/nor.html")

fig <- plot_ly()
fig <- fig %>% 
layout(title = 'ojb') %>% 
add_trace(type='scatter', mode='markers', x = x, y = y, color=data$ojb, hovertext=cont$"ojb-context")
htmlwidgets::saveWidget(as_widget(fig), "./plotly-outputs/ojb.html")

fig <- plot_ly()
fig <- fig %>% 
layout(title = 'pck') %>% 
add_trace(type='scatter', mode='markers', x = x, y = y, color=data$pck, hovertext=cont$"pck-context")
htmlwidgets::saveWidget(as_widget(fig), "./plotly-outputs/pck.html")

fig <- plot_ly()
fig <- fig %>% 
layout(title = 'pes') %>% 
add_trace(type='scatter', mode='markers', x = x, y = y, color=data$pes, hovertext=cont$"pes-context")
htmlwidgets::saveWidget(as_widget(fig), "./plotly-outputs/pes.html")

fig <- plot_ly()
fig <- fig %>% 
layout(title = 'plt') %>% 
add_trace(type='scatter', mode='markers', x = x, y = y, color=data$plt, hovertext=cont$"plt-context")
htmlwidgets::saveWidget(as_widget(fig), "./plotly-outputs/plt.html")

fig <- plot_ly()
fig <- fig %>% 
layout(title = 'pol') %>% 
add_trace(type='scatter', mode='markers', x = x, y = y, color=data$pol, hovertext=cont$"pol-context")
htmlwidgets::saveWidget(as_widget(fig), "./plotly-outputs/pol.html")

fig <- plot_ly()
fig <- fig %>% 
layout(title = 'por') %>% 
add_trace(type='scatter', mode='markers', x = x, y = y, color=data$por, hovertext=cont$"por-context")
htmlwidgets::saveWidget(as_widget(fig), "./plotly-outputs/por.html")

fig <- plot_ly()
fig <- fig %>% 
layout(title = 'pot') %>% 
add_trace(type='scatter', mode='markers', x = x, y = y, color=data$pot, hovertext=cont$"pot-context")
htmlwidgets::saveWidget(as_widget(fig), "./plotly-outputs/pot.html")

fig <- plot_ly()
fig <- fig %>% 
layout(title = 'ppk') %>% 
add_trace(type='scatter', mode='markers', x = x, y = y, color=data$ppk, hovertext=cont$"ppk-context")
htmlwidgets::saveWidget(as_widget(fig), "./plotly-outputs/ppk.html")

fig <- plot_ly()
fig <- fig %>% 
layout(title = 'quc') %>% 
add_trace(type='scatter', mode='markers', x = x, y = y, color=data$quc, hovertext=cont$"quc-context")
htmlwidgets::saveWidget(as_widget(fig), "./plotly-outputs/quc.html")

fig <- plot_ly()
fig <- fig %>% 
layout(title = 'quw') %>% 
add_trace(type='scatter', mode='markers', x = x, y = y, color=data$quw, hovertext=cont$"quw-context")
htmlwidgets::saveWidget(as_widget(fig), "./plotly-outputs/quw.html")

fig <- plot_ly()
fig <- fig %>% 
layout(title = 'rom') %>% 
add_trace(type='scatter', mode='markers', x = x, y = y, color=data$rom, hovertext=cont$"rom-context")
htmlwidgets::saveWidget(as_widget(fig), "./plotly-outputs/rom.html")

fig <- plot_ly()
fig <- fig %>% 
layout(title = 'rum') %>% 
add_trace(type='scatter', mode='markers', x = x, y = y, color=data$rum, hovertext=cont$"rum-context")
htmlwidgets::saveWidget(as_widget(fig), "./plotly-outputs/rum.html")

fig <- plot_ly()
fig <- fig %>% 
layout(title = 'rus') %>% 
add_trace(type='scatter', mode='markers', x = x, y = y, color=data$rus, hovertext=cont$"rus-context")
htmlwidgets::saveWidget(as_widget(fig), "./plotly-outputs/rus.html")

fig <- plot_ly()
fig <- fig %>% 
layout(title = 'shi') %>% 
add_trace(type='scatter', mode='markers', x = x, y = y, color=data$shi, hovertext=cont$"shi-context")
htmlwidgets::saveWidget(as_widget(fig), "./plotly-outputs/shi.html")

fig <- plot_ly()
fig <- fig %>% 
layout(title = 'slk') %>% 
add_trace(type='scatter', mode='markers', x = x, y = y, color=data$slk, hovertext=cont$"slk-context")
htmlwidgets::saveWidget(as_widget(fig), "./plotly-outputs/slk.html")

fig <- plot_ly()
fig <- fig %>% 
layout(title = 'slv') %>% 
add_trace(type='scatter', mode='markers', x = x, y = y, color=data$slv, hovertext=cont$"slv-context")
htmlwidgets::saveWidget(as_widget(fig), "./plotly-outputs/slv.html")

fig <- plot_ly()
fig <- fig %>% 
layout(title = 'sna') %>% 
add_trace(type='scatter', mode='markers', x = x, y = y, color=data$sna, hovertext=cont$"sna-context")
htmlwidgets::saveWidget(as_widget(fig), "./plotly-outputs/sna.html")

fig <- plot_ly()
fig <- fig %>% 
layout(title = 'som') %>% 
add_trace(type='scatter', mode='markers', x = x, y = y, color=data$som, hovertext=cont$"som-context")
htmlwidgets::saveWidget(as_widget(fig), "./plotly-outputs/som.html")

fig <- plot_ly()
fig <- fig %>% 
layout(title = 'spa') %>% 
add_trace(type='scatter', mode='markers', x = x, y = y, color=data$spa, hovertext=cont$"spa-context")
htmlwidgets::saveWidget(as_widget(fig), "./plotly-outputs/spa.html")

fig <- plot_ly()
fig <- fig %>% 
layout(title = 'srp') %>% 
add_trace(type='scatter', mode='markers', x = x, y = y, color=data$srp, hovertext=cont$"srp-context")
htmlwidgets::saveWidget(as_widget(fig), "./plotly-outputs/srp.html")

fig <- plot_ly()
fig <- fig %>% 
layout(title = 'ssw') %>% 
add_trace(type='scatter', mode='markers', x = x, y = y, color=data$ssw, hovertext=cont$"ssw-context")
htmlwidgets::saveWidget(as_widget(fig), "./plotly-outputs/ssw.html")

fig <- plot_ly()
fig <- fig %>% 
layout(title = 'swe') %>% 
add_trace(type='scatter', mode='markers', x = x, y = y, color=data$swe, hovertext=cont$"swe-context")
htmlwidgets::saveWidget(as_widget(fig), "./plotly-outputs/swe.html")

fig <- plot_ly()
fig <- fig %>% 
layout(title = 'syr') %>% 
add_trace(type='scatter', mode='markers', x = x, y = y, color=data$syr, hovertext=cont$"syr-context")
htmlwidgets::saveWidget(as_widget(fig), "./plotly-outputs/syr.html")

fig <- plot_ly()
fig <- fig %>% 
layout(title = 'tel') %>% 
add_trace(type='scatter', mode='markers', x = x, y = y, color=data$tel, hovertext=cont$"tel-context")
htmlwidgets::saveWidget(as_widget(fig), "./plotly-outputs/tel.html")

fig <- plot_ly()
fig <- fig %>% 
layout(title = 'tgl') %>% 
add_trace(type='scatter', mode='markers', x = x, y = y, color=data$tgl, hovertext=cont$"tgl-context")
htmlwidgets::saveWidget(as_widget(fig), "./plotly-outputs/tgl.html")

fig <- plot_ly()
fig <- fig %>% 
layout(title = 'tha') %>% 
add_trace(type='scatter', mode='markers', x = x, y = y, color=data$tha, hovertext=cont$"tha-context")
htmlwidgets::saveWidget(as_widget(fig), "./plotly-outputs/tha.html")

fig <- plot_ly()
fig <- fig %>% 
layout(title = 'tmh') %>% 
add_trace(type='scatter', mode='markers', x = x, y = y, color=data$tmh, hovertext=cont$"tmh-context")
htmlwidgets::saveWidget(as_widget(fig), "./plotly-outputs/tmh.html")

fig <- plot_ly()
fig <- fig %>% 
layout(title = 'tur') %>% 
add_trace(type='scatter', mode='markers', x = x, y = y, color=data$tur, hovertext=cont$"tur-context")
htmlwidgets::saveWidget(as_widget(fig), "./plotly-outputs/tur.html")

fig <- plot_ly()
fig <- fig %>% 
layout(title = 'ukr') %>% 
add_trace(type='scatter', mode='markers', x = x, y = y, color=data$ukr, hovertext=cont$"ukr-context")
htmlwidgets::saveWidget(as_widget(fig), "./plotly-outputs/ukr.html")

fig <- plot_ly()
fig <- fig %>% 
layout(title = 'usp') %>% 
add_trace(type='scatter', mode='markers', x = x, y = y, color=data$usp, hovertext=cont$"usp-context")
htmlwidgets::saveWidget(as_widget(fig), "./plotly-outputs/usp.html")

fig <- plot_ly()
fig <- fig %>% 
layout(title = 'wal') %>% 
add_trace(type='scatter', mode='markers', x = x, y = y, color=data$wal, hovertext=cont$"wal-context")
htmlwidgets::saveWidget(as_widget(fig), "./plotly-outputs/wal.html")

fig <- plot_ly()
fig <- fig %>% 
layout(title = 'wol') %>% 
add_trace(type='scatter', mode='markers', x = x, y = y, color=data$wol, hovertext=cont$"wol-context")
htmlwidgets::saveWidget(as_widget(fig), "./plotly-outputs/wol.html")

fig <- plot_ly()
fig <- fig %>% 
layout(title = 'xho') %>% 
add_trace(type='scatter', mode='markers', x = x, y = y, color=data$xho, hovertext=cont$"xho-context")
htmlwidgets::saveWidget(as_widget(fig), "./plotly-outputs/xho.html")

fig <- plot_ly()
fig <- fig %>% 
layout(title = 'zul') %>% 
add_trace(type='scatter', mode='markers', x = x, y = y, color=data$zul, hovertext=cont$"zul-context")
htmlwidgets::saveWidget(as_widget(fig), "./plotly-outputs/zul.html")


