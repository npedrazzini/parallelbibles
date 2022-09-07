#Add the full path to "when-data.txt" and "when-matrix.txt" or start an R project in the same directory as those files
install.packages('Cairo') #if you haven't already
library(Cairo)
data<-read.table("when-data.txt")
matr<-read.table("when-matrix.txt")
datacsv<-read_csv("when.csv")
cmd<-cmdscale(matr,k=20)
cont<- as.vector(datacsv$context)
x<-cmd[,1];y<-cmd[,2]
df<- data.frame(x,y)

CairoPDF(file='when-plots.pdf',16, 12)

h<-data[,rep(1,2)]
h[,2]<-c(1:946)
lmap(df,h[,1],main="eng",levels = c(0.29,0.32,0.35),add = FALSE,position = "topright", grid = 30)


h<-data[,rep(2,2)]
h[,2]<-c(1:946)
lmap(df,h[,1],main="acu",levels = c(0.29,0.32,0.35),add = FALSE,position = "topright", grid = 30)


h<-data[,rep(3,2)]
h[,2]<-c(1:946)
lmap(df,h[,1],main="afr",levels = c(0.29,0.32,0.35),add = FALSE,position = "topright", grid = 30)


h<-data[,rep(4,2)]
h[,2]<-c(1:946)
lmap(df,h[,1],main="ake",levels = c(0.29,0.32,0.35),add = FALSE,position = "topright", grid = 30)


h<-data[,rep(5,2)]
h[,2]<-c(1:946)
lmap(df,h[,1],main="alb",levels = c(0.29,0.32,0.35),add = FALSE,position = "topright", grid = 30)


h<-data[,rep(6,2)]
h[,2]<-c(1:946)
lmap(df,h[,1],main="amu",levels = c(0.29,0.32,0.35),add = FALSE,position = "topright", grid = 30)


h<-data[,rep(7,2)]
h[,2]<-c(1:946)
lmap(df,h[,1],main="ara",levels = c(0.29,0.32,0.35),add = FALSE,position = "topright", grid = 30)


h<-data[,rep(8,2)]
h[,2]<-c(1:946)
lmap(df,h[,1],main="arm",levels = c(0.29,0.32,0.35),add = FALSE,position = "topright", grid = 30)


h<-data[,rep(9,2)]
h[,2]<-c(1:946)
lmap(df,h[,1],main="baq",levels = c(0.29,0.32,0.35),add = FALSE,position = "topright", grid = 30)


h<-data[,rep(10,2)]
h[,2]<-c(1:946)
lmap(df,h[,1],main="bsn",levels = c(0.29,0.32,0.35),add = FALSE,position = "topright", grid = 30)


h<-data[,rep(11,2)]
h[,2]<-c(1:946)
lmap(df,h[,1],main="bul",levels = c(0.29,0.32,0.35),add = FALSE,position = "topright", grid = 30)


h<-data[,rep(12,2)]
h[,2]<-c(1:946)
lmap(df,h[,1],main="cak",levels = c(0.29,0.32,0.35),add = FALSE,position = "topright", grid = 30)


h<-data[,rep(13,2)]
h[,2]<-c(1:946)
lmap(df,h[,1],main="ceb",levels = c(0.29,0.32,0.35),add = FALSE,position = "topright", grid = 30)


h<-data[,rep(14,2)]
h[,2]<-c(1:946)
lmap(df,h[,1],main="cha",levels = c(0.29,0.32,0.35),add = FALSE,position = "topright", grid = 30)


h<-data[,rep(15,2)]
h[,2]<-c(1:946)
lmap(df,h[,1],main="chi",levels = c(0.29,0.32,0.35),add = FALSE,position = "topright", grid = 30)


h<-data[,rep(16,2)]
h[,2]<-c(1:946)
lmap(df,h[,1],main="chq",levels = c(0.29,0.32,0.35),add = FALSE,position = "topright", grid = 30)


h<-data[,rep(17,2)]
h[,2]<-c(1:946)
lmap(df,h[,1],main="chr",levels = c(0.29,0.32,0.35),add = FALSE,position = "topright", grid = 30)


h<-data[,rep(18,2)]
h[,2]<-c(1:946)
lmap(df,h[,1],main="chu",levels = c(0.29,0.32,0.35),add = FALSE,position = "topright", grid = 30)


h<-data[,rep(19,2)]
h[,2]<-c(1:946)
lmap(df,h[,1],main="cjp",levels = c(0.29,0.32,0.35),add = FALSE,position = "topright", grid = 30)


h<-data[,rep(20,2)]
h[,2]<-c(1:946)
lmap(df,h[,1],main="cni",levels = c(0.29,0.32,0.35),add = FALSE,position = "topright", grid = 30)


h<-data[,rep(21,2)]
h[,2]<-c(1:946)
lmap(df,h[,1],main="cop",levels = c(0.29,0.32,0.35),add = FALSE,position = "topright", grid = 30)


h<-data[,rep(22,2)]
h[,2]<-c(1:946)
lmap(df,h[,1],main="crp",levels = c(0.29,0.32,0.35),add = FALSE,position = "topright", grid = 30)


h<-data[,rep(23,2)]
h[,2]<-c(1:946)
lmap(df,h[,1],main="cze",levels = c(0.29,0.32,0.35),add = FALSE,position = "topright", grid = 30)


h<-data[,rep(24,2)]
h[,2]<-c(1:946)
lmap(df,h[,1],main="dan",levels = c(0.29,0.32,0.35),add = FALSE,position = "topright", grid = 30)


h<-data[,rep(25,2)]
h[,2]<-c(1:946)
lmap(df,h[,1],main="deu",levels = c(0.29,0.32,0.35),add = FALSE,position = "topright", grid = 30)


h<-data[,rep(26,2)]
h[,2]<-c(1:946)
lmap(df,h[,1],main="dik",levels = c(0.29,0.32,0.35),add = FALSE,position = "topright", grid = 30)


h<-data[,rep(27,2)]
h[,2]<-c(1:946)
lmap(df,h[,1],main="dje",levels = c(0.29,0.32,0.35),add = FALSE,position = "topright", grid = 30)


h<-data[,rep(28,2)]
h[,2]<-c(1:946)
lmap(df,h[,1],main="dop",levels = c(0.29,0.32,0.35),add = FALSE,position = "topright", grid = 30)


h<-data[,rep(29,2)]
h[,2]<-c(1:946)
lmap(df,h[,1],main="epo",levels = c(0.29,0.32,0.35),add = FALSE,position = "topright", grid = 30)


h<-data[,rep(30,2)]
h[,2]<-c(1:946)
lmap(df,h[,1],main="est",levels = c(0.29,0.32,0.35),add = FALSE,position = "topright", grid = 30)


h<-data[,rep(31,2)]
h[,2]<-c(1:946)
lmap(df,h[,1],main="ewe",levels = c(0.29,0.32,0.35),add = FALSE,position = "topright", grid = 30)


h<-data[,rep(32,2)]
h[,2]<-c(1:946)
lmap(df,h[,1],main="fin",levels = c(0.29,0.32,0.35),add = FALSE,position = "topright", grid = 30)


h<-data[,rep(33,2)]
h[,2]<-c(1:946)
lmap(df,h[,1],main="fra",levels = c(0.29,0.32,0.35),add = FALSE,position = "topright", grid = 30)


h<-data[,rep(34,2)]
h[,2]<-c(1:946)
lmap(df,h[,1],main="gbi",levels = c(0.29,0.32,0.35),add = FALSE,position = "topright", grid = 30)


h<-data[,rep(35,2)]
h[,2]<-c(1:946)
lmap(df,h[,1],main="glv",levels = c(0.29,0.32,0.35),add = FALSE,position = "topright", grid = 30)


h<-data[,rep(36,2)]
h[,2]<-c(1:946)
lmap(df,h[,1],main="got",levels = c(0.29,0.32,0.35),add = FALSE,position = "topright", grid = 30)


h<-data[,rep(37,2)]
h[,2]<-c(1:946)
lmap(df,h[,1],main="grc",levels = c(0.29,0.32,0.35),add = FALSE,position = "topright", grid = 30)


h<-data[,rep(38,2)]
h[,2]<-c(1:946)
lmap(df,h[,1],main="gre",levels = c(0.29,0.32,0.35),add = FALSE,position = "topright", grid = 30)


h<-data[,rep(39,2)]
h[,2]<-c(1:946)
lmap(df,h[,1],main="guj",levels = c(0.29,0.32,0.35),add = FALSE,position = "topright", grid = 30)


h<-data[,rep(40,2)]
h[,2]<-c(1:946)
lmap(df,h[,1],main="hin",levels = c(0.29,0.32,0.35),add = FALSE,position = "topright", grid = 30)


h<-data[,rep(41,2)]
h[,2]<-c(1:946)
lmap(df,h[,1],main="hrv",levels = c(0.29,0.32,0.35),add = FALSE,position = "topright", grid = 30)


h<-data[,rep(42,2)]
h[,2]<-c(1:946)
lmap(df,h[,1],main="hun",levels = c(0.29,0.32,0.35),add = FALSE,position = "topright", grid = 30)


h<-data[,rep(43,2)]
h[,2]<-c(1:946)
lmap(df,h[,1],main="ind",levels = c(0.29,0.32,0.35),add = FALSE,position = "topright", grid = 30)


h<-data[,rep(44,2)]
h[,2]<-c(1:946)
lmap(df,h[,1],main="isl",levels = c(0.29,0.32,0.35),add = FALSE,position = "topright", grid = 30)


h<-data[,rep(45,2)]
h[,2]<-c(1:946)
lmap(df,h[,1],main="ita",levels = c(0.29,0.32,0.35),add = FALSE,position = "topright", grid = 30)


h<-data[,rep(46,2)]
h[,2]<-c(1:946)
lmap(df,h[,1],main="jak",levels = c(0.29,0.32,0.35),add = FALSE,position = "topright", grid = 30)


h<-data[,rep(47,2)]
h[,2]<-c(1:946)
lmap(df,h[,1],main="jap",levels = c(0.29,0.32,0.35),add = FALSE,position = "topright", grid = 30)


h<-data[,rep(48,2)]
h[,2]<-c(1:946)
lmap(df,h[,1],main="jiv",levels = c(0.29,0.32,0.35),add = FALSE,position = "topright", grid = 30)


h<-data[,rep(49,2)]
h[,2]<-c(1:946)
lmap(df,h[,1],main="kab",levels = c(0.29,0.32,0.35),add = FALSE,position = "topright", grid = 30)


h<-data[,rep(50,2)]
h[,2]<-c(1:946)
lmap(df,h[,1],main="kbh",levels = c(0.29,0.32,0.35),add = FALSE,position = "topright", grid = 30)


h<-data[,rep(51,2)]
h[,2]<-c(1:946)
lmap(df,h[,1],main="kor",levels = c(0.29,0.32,0.35),add = FALSE,position = "topright", grid = 30)


h<-data[,rep(52,2)]
h[,2]<-c(1:946)
lmap(df,h[,1],main="lat",levels = c(0.29,0.32,0.35),add = FALSE,position = "topright", grid = 30)


h<-data[,rep(53,2)]
h[,2]<-c(1:946)
lmap(df,h[,1],main="lav",levels = c(0.29,0.32,0.35),add = FALSE,position = "topright", grid = 30)


h<-data[,rep(54,2)]
h[,2]<-c(1:946)
lmap(df,h[,1],main="lit",levels = c(0.29,0.32,0.35),add = FALSE,position = "topright", grid = 30)


h<-data[,rep(55,2)]
h[,2]<-c(1:946)
lmap(df,h[,1],main="mam",levels = c(0.29,0.32,0.35),add = FALSE,position = "topright", grid = 30)


h<-data[,rep(56,2)]
h[,2]<-c(1:946)
lmap(df,h[,1],main="mao",levels = c(0.29,0.32,0.35),add = FALSE,position = "topright", grid = 30)


h<-data[,rep(57,2)]
h[,2]<-c(1:946)
lmap(df,h[,1],main="mar",levels = c(0.29,0.32,0.35),add = FALSE,position = "topright", grid = 30)


h<-data[,rep(58,2)]
h[,2]<-c(1:946)
lmap(df,h[,1],main="mya",levels = c(0.29,0.32,0.35),add = FALSE,position = "topright", grid = 30)


h<-data[,rep(59,2)]
h[,2]<-c(1:946)
lmap(df,h[,1],main="nep",levels = c(0.29,0.32,0.35),add = FALSE,position = "topright", grid = 30)


h<-data[,rep(60,2)]
h[,2]<-c(1:946)
lmap(df,h[,1],main="nhg",levels = c(0.29,0.32,0.35),add = FALSE,position = "topright", grid = 30)


h<-data[,rep(61,2)]
h[,2]<-c(1:946)
lmap(df,h[,1],main="nld",levels = c(0.29,0.32,0.35),add = FALSE,position = "topright", grid = 30)


h<-data[,rep(62,2)]
h[,2]<-c(1:946)
lmap(df,h[,1],main="nor",levels = c(0.29,0.32,0.35),add = FALSE,position = "topright", grid = 30)


h<-data[,rep(63,2)]
h[,2]<-c(1:946)
lmap(df,h[,1],main="ojb",levels = c(0.29,0.32,0.35),add = FALSE,position = "topright", grid = 30)


h<-data[,rep(64,2)]
h[,2]<-c(1:946)
lmap(df,h[,1],main="pck",levels = c(0.29,0.32,0.35),add = FALSE,position = "topright", grid = 30)


h<-data[,rep(65,2)]
h[,2]<-c(1:946)
lmap(df,h[,1],main="pes",levels = c(0.29,0.32,0.35),add = FALSE,position = "topright", grid = 30)


h<-data[,rep(66,2)]
h[,2]<-c(1:946)
lmap(df,h[,1],main="plt",levels = c(0.29,0.32,0.35),add = FALSE,position = "topright", grid = 30)


h<-data[,rep(67,2)]
h[,2]<-c(1:946)
lmap(df,h[,1],main="pol",levels = c(0.29,0.32,0.35),add = FALSE,position = "topright", grid = 30)


h<-data[,rep(68,2)]
h[,2]<-c(1:946)
lmap(df,h[,1],main="por",levels = c(0.29,0.32,0.35),add = FALSE,position = "topright", grid = 30)


h<-data[,rep(69,2)]
h[,2]<-c(1:946)
lmap(df,h[,1],main="pot",levels = c(0.29,0.32,0.35),add = FALSE,position = "topright", grid = 30)


h<-data[,rep(70,2)]
h[,2]<-c(1:946)
lmap(df,h[,1],main="ppk",levels = c(0.29,0.32,0.35),add = FALSE,position = "topright", grid = 30)


h<-data[,rep(71,2)]
h[,2]<-c(1:946)
lmap(df,h[,1],main="quc",levels = c(0.29,0.32,0.35),add = FALSE,position = "topright", grid = 30)


h<-data[,rep(72,2)]
h[,2]<-c(1:946)
lmap(df,h[,1],main="quw",levels = c(0.29,0.32,0.35),add = FALSE,position = "topright", grid = 30)


h<-data[,rep(73,2)]
h[,2]<-c(1:946)
lmap(df,h[,1],main="rom",levels = c(0.29,0.32,0.35),add = FALSE,position = "topright", grid = 30)


h<-data[,rep(74,2)]
h[,2]<-c(1:946)
lmap(df,h[,1],main="rum",levels = c(0.29,0.32,0.35),add = FALSE,position = "topright", grid = 30)


h<-data[,rep(75,2)]
h[,2]<-c(1:946)
lmap(df,h[,1],main="rus",levels = c(0.29,0.32,0.35),add = FALSE,position = "topright", grid = 30)


h<-data[,rep(76,2)]
h[,2]<-c(1:946)
lmap(df,h[,1],main="shi",levels = c(0.29,0.32,0.35),add = FALSE,position = "topright", grid = 30)


h<-data[,rep(77,2)]
h[,2]<-c(1:946)
lmap(df,h[,1],main="slk",levels = c(0.29,0.32,0.35),add = FALSE,position = "topright", grid = 30)


h<-data[,rep(78,2)]
h[,2]<-c(1:946)
lmap(df,h[,1],main="slv",levels = c(0.29,0.32,0.35),add = FALSE,position = "topright", grid = 30)


h<-data[,rep(79,2)]
h[,2]<-c(1:946)
lmap(df,h[,1],main="sna",levels = c(0.29,0.32,0.35),add = FALSE,position = "topright", grid = 30)


h<-data[,rep(80,2)]
h[,2]<-c(1:946)
lmap(df,h[,1],main="som",levels = c(0.29,0.32,0.35),add = FALSE,position = "topright", grid = 30)


h<-data[,rep(81,2)]
h[,2]<-c(1:946)
lmap(df,h[,1],main="spa",levels = c(0.29,0.32,0.35),add = FALSE,position = "topright", grid = 30)


h<-data[,rep(82,2)]
h[,2]<-c(1:946)
lmap(df,h[,1],main="srp",levels = c(0.29,0.32,0.35),add = FALSE,position = "topright", grid = 30)


h<-data[,rep(83,2)]
h[,2]<-c(1:946)
lmap(df,h[,1],main="ssw",levels = c(0.29,0.32,0.35),add = FALSE,position = "topright", grid = 30)


h<-data[,rep(84,2)]
h[,2]<-c(1:946)
lmap(df,h[,1],main="swe",levels = c(0.29,0.32,0.35),add = FALSE,position = "topright", grid = 30)


h<-data[,rep(85,2)]
h[,2]<-c(1:946)
lmap(df,h[,1],main="syr",levels = c(0.29,0.32,0.35),add = FALSE,position = "topright", grid = 30)


h<-data[,rep(86,2)]
h[,2]<-c(1:946)
lmap(df,h[,1],main="tel",levels = c(0.29,0.32,0.35),add = FALSE,position = "topright", grid = 30)


h<-data[,rep(87,2)]
h[,2]<-c(1:946)
lmap(df,h[,1],main="tgl",levels = c(0.29,0.32,0.35),add = FALSE,position = "topright", grid = 30)


h<-data[,rep(88,2)]
h[,2]<-c(1:946)
lmap(df,h[,1],main="tha",levels = c(0.29,0.32,0.35),add = FALSE,position = "topright", grid = 30)


h<-data[,rep(89,2)]
h[,2]<-c(1:946)
lmap(df,h[,1],main="tmh",levels = c(0.29,0.32,0.35),add = FALSE,position = "topright", grid = 30)


h<-data[,rep(90,2)]
h[,2]<-c(1:946)
lmap(df,h[,1],main="tur",levels = c(0.29,0.32,0.35),add = FALSE,position = "topright", grid = 30)


h<-data[,rep(91,2)]
h[,2]<-c(1:946)
lmap(df,h[,1],main="ukr",levels = c(0.29,0.32,0.35),add = FALSE,position = "topright", grid = 30)


h<-data[,rep(92,2)]
h[,2]<-c(1:946)
lmap(df,h[,1],main="usp",levels = c(0.29,0.32,0.35),add = FALSE,position = "topright", grid = 30)


h<-data[,rep(93,2)]
h[,2]<-c(1:946)
lmap(df,h[,1],main="wal",levels = c(0.29,0.32,0.35),add = FALSE,position = "topright", grid = 30)


h<-data[,rep(94,2)]
h[,2]<-c(1:946)
lmap(df,h[,1],main="wol",levels = c(0.29,0.32,0.35),add = FALSE,position = "topright", grid = 30)


h<-data[,rep(95,2)]
h[,2]<-c(1:946)
lmap(df,h[,1],main="xho",levels = c(0.29,0.32,0.35),add = FALSE,position = "topright", grid = 30)


h<-data[,rep(96,2)]
h[,2]<-c(1:946)
lmap(df,h[,1],main="zul",levels = c(0.29,0.32,0.35),add = FALSE,position = "topright", grid = 30)

dev.off()
