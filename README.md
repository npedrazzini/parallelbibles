# parallelbibles

Word-alignment models for Bible translations in 100+ historical and contemporary languages


## Requirements

1. Installation and dependencies: 

Download or clone the repository:

`$ git clone https://github.com/npedrazzini/parallelbibles`

From the root directory (./parallelbibles), build the repository:

`$ make`

This will download and build [SyMGIZA++](https://github.com/emjotde/symgiza-pp)[[1]](#1), and install all the required dependencies.

2. XML files, which can be of two formats:
 
a. OPUS (untokenized) (from https://opus.nlpl.eu/bible-uedin.php)

b. PROIEL (from https://proiel.github.io)

This repository comes with OPUS XMLs (in original-xmls/opus-xmls) and PROIEL XMLs for New Testament Greek, Old Church Slavonic and Gothic (in original/proiel-xmls).

## Train word-alignment models

`$ ./train.sh`

This step will: 
1. convert OPUS/PROIEL XML files to GIZA-readable CSV files
2. train a word-alignment model for each target language
3. make GIZA's outputs easily readable and queryable 

You will be prompted to:
1. specify the input XML format (OPUS, PROIEL, or mixed)
2. enter the desired source language
3. enter the target languages (or have all the remaining as targets)
4. specify if you want to strip punctuation
5. specify if you want to bring everything to lowercase
6. provide a name for your model

NB: the chosen languages must be entered in their ISO 639-3 code. See [here](https://iso639-3.sil.org/code_tables/639/read) for the complete list and the [table](https://github.com/npedrazzini/parallelbibles#languages) below for the languages included in the models.

## Extract a word and its translations

`$ ./extract.sh`

This step will:
1. extract every occurrence of a word in the source language and its translation in the target languages.
2. output a CSV file for each word. The file will contain one occurrence per line, its citation (Bible verse), context, and the translations in each target language.

You will be prompted to enter:
1. the name of the model you want to use
2. a target word

NB:
- *NULL* will indicate that the model did not find a match for the word in the target language.
- *NA* will indicate that the target language did not have a Bible translations of that particular verse in the first place (e.g. some languages lack a translation for the whole Old Testament). 

## Calculate semantic similarity and build semantic maps

> These scripts are an adaptation of the code by [[2]](#2).

- `./scripts/postprocessing/MDS-simple.py`: simple multi-dimensional scaling (MDS).
- `./scripts/postprocessing/MDS-kriging.py`: multi-dimensional scaling + Kriging (to draw lines around clusters probabilstically).

By running either of the scripts you will be prompted to enter:
1. the name of the model you want to use.
2. a target word.

This will create a directory *modelname/\_TARGETWORDS\_/word-MDS*, containing all the outputs. The relevant ones to plot semantic maps will be: 
- *word-MDS.R*: an R script to generate the semantic maps.
- *word-data.txt*: the original data.
- *word-matrix.txt*: distance matrix between source word and target words.

By running *word-MDS.R* in R (the folder *modelname/\_TARGETWORDS\_/word-MDS* can also be opened as an R project) a PDF file will be generated containing all the plots (of either the simple-MDS or the MDS+Kriging type).

**NB**: `MDS-kriging.py` relies on the R package [qlcVisualize](https://rdrr.io/github/cysouw/qlcVisualize/). If you have issues installing it, simply save the two functions we need from that package (`lmap` and `boundary`) by running the script *./scripts/postprocessing/lmap-boundary-functions.R*.

## Hierarchical clusters and NeighborNets

- *./scripts/postprocessing/splitstree.R*: hierarchical clustering and NeighborNet analysis of the languages based on a criterion *x* (default: null-constructions)

The script takes as input the output *modelNAME/_TARGETWORDS_/word-MDS/word-data.txt* of `MDS-simple.py` or `MDS-kriging.py` (which is the same as the output *word.csv* of `./extract.sh` minus the column "context").

The script will: 
1. Plot a simple hierarchical cluster.
2. Generate a Nexus (.nex) file for NeighborNet analysis, to be visualized with the [SplitsTree4](https://uni-tuebingen.de/en/fakultaeten/mathematisch-naturwissenschaftliche-fakultaet/fachbereiche/informatik/lehrstuehle/algorithms-in-bioinformatics/software/splitstree/) software.

# Pretrained models

Four pretrained models currently come with this repository: 

1. *model1-UC-P*: **U**pper case and with **P**unctuation. English is source language. All other languages (both from OPUS and PROIEL; however see Disclaimer) are targets.
2. *model2-LC-NP*: **L**ower **C**ase and **N**o **P**unctuation. English is source language. All other languages (both from OPUS and PROIEL; however see Disclaimer) are targets.
3. *model3-UC-NP*: **U**pper **C**ase and **N**o **P**unctuation. English is source language. All other languages (both from OPUS and PROIEL; however see Disclaimer) are targets.
4. *model4-LC-P*: **L**ower **C**ase and **N**o **P**unctuation. English is source language. All other languages (both from OPUS and PROIEL; however see Disclaimer) are targets.

You can directly extract target words from either of these models by running `$ ./extract.sh`. You will be prompted to enter the name of the model you want to use.

# Languages
**OT** = Old Testament

**NT** = New Testament

| ISO 639-3 | Language | Language family |  OT | NT |Notes |
|---|---|---|---|---|---|
| acu | [Achuar-Shiwiar](https://www.ethnologue.com/language/acu) | Jivaroan |  N | Y  |   |
| afr | [Afrikaans](https://www.ethnologue.com/language/afr) | Indo-European > Germanic |  Y | Y  |   |
| agr | [Awajún](https://www.ethnologue.com/language/agr) | Jivaroan |  N |  Y |   |
| ake | [Akawaio](https://www.ethnologue.com/language/ake) | Cariban |  N |  Y |   |
| sqi/alb | [Albanian](https://www.ethnologue.com/language/sqi) | Indo-European|  Y |   Y|   |
| amh | [Amharic](https://www.ethnologue.com/language/amh) | Afro-Asiatic > Semitic | Y |  N |   |
| amu | [Guerrero Amuzgo](https://www.ethnologue.com/language/amu) | Otomanguean |  N | Y  |   |
| ara | [Arabic](https://www.ethnologue.com/language/ara) | Afro-Asiatic > Semitic | Y  |  Y |   |
| hye/arm | [Armenian](https://www.ethnologue.com/language/hye) | Indo-European |  Y | Y  |   |
| baq | [Basque](https://www.ethnologue.com/language/eus) | Isolate |  N |  Y |   |
| bsn | [Barasana-Eduria](https://www.ethnologue.com/language/bsn) | Tucanoan | N  |  Y |   |
| bul | [Bulgarian](https://www.ethnologue.com/language/bul) | Indo-European > Balto-Slavic |  Y | Y  |   |
| cak | [Kaqchikel](https://www.ethnologue.com/language/cak) | Mayan | N  | Y  |   |
| ceb | [Cebuano](https://www.ethnologue.com/language/ceb) | Austronesian > Malayo-Polynesian |  Y | Y  |   |
| cha | [Chamorro](https://www.ethnologue.com/language/cha) | Austronesian > Malayo-Polynesian |  Y |  Y |  OT only consists of the Psalms |
| zho/chi | [Chinese](https://www.ethnologue.com/language/zho) | Sino-Tibetan > Sinitic | Y  |  Y |   |
| chq | [Quiotepec Chinantec](https://www.ethnologue.com/language/chq) | Otomanguean | N  |  Y|   |
| chr | [Cherokee](https://www.ethnologue.com/language/chr) | Iroquoian |  N |  Y |   |
| chu | [Church Slavonic](https://www.ethnologue.com/language/chu) | Indo-European > Balto-Slavic|  N | Y  |   |
| cjp | [Cabécar](https://www.ethnologue.com/language/cjp) | Chibchan | N  | Y  |   |
| cni | [Asháninka](https://www.ethnologue.com/language/cni) | Maipurean | N  |  Y |   |
| cop | [Coptic](https://www.ethnologue.com/language/cop) | Afro-Asiatic > Egyptian | N  | Y  |   |
| crp | [Creoles and pidgins](https://www.ethnologue.com/language/hat/24) | Creole > French-based |  Y | Y  | The original XML files have the generic 'crp' code. This is however Haitian Creole (code hat) |
| cze | [Czech](https://www.ethnologue.com/language/ces) | Indo-European > Balto-Slavic| Y  | Y  |   |
| dan | [Danish](https://www.ethnologue.com/language/dan) | Indo-European > Germanic| Y  |  Y |   |
| deu | [German](https://www.ethnologue.com/language/deu) | Indo-European > Germanic|  Y |  Y |   |
| dik | [Southwestern Dinka](https://www.ethnologue.com/language/dik) | Nilo-Saharan > Nilotic |  N |  Y |   |
| dje | [Zarma](https://www.ethnologue.com/language/dje) |  Nilo-Saharan > Songhai | Y  | Y  |   |
| dop | [Lukpa](https://www.ethnologue.com/language/dop) | Niger-Congo > Atlantic-Congo | N  | Y  |   |
| epo | [Esperanto](https://www.ethnologue.com/language/epo) | Constructed |  Y |  Y |   |
| est | [Estonian](https://www.ethnologue.com/language/est) | Uralic | Y  |  Y |   |
| ewe | [Ewe](https://www.ethnologue.com/language/ewe) | Niger-Congo > Atlantic-Congo | N  |  Y |   |
| fin | [Finnish](https://www.ethnologue.com/language/fin) | Uralic | Y  | Y  |   |
| fra | [French](https://www.ethnologue.com/language/fra) | Indo-European > Italic|  Y | Y  |   |
| gbi | [Galela](https://www.ethnologue.com/language/gbi) | West Papuan |  N | Y  |   |
| gla | [Scottish Gaelic](https://www.ethnologue.com/language/gla) | Indo-European > Celtic|  N |  Y | The only text included is the Gospel of Mark  |
| glv | [Manx](https://www.ethnologue.com/language/glv) | Indo-European > Celtic|  Y |  Y |  The only text from the OT is the Book of Esther |
| got | Gothic | Indo-European > Germanic |  N |  Y |   |
| grc | [Ancient Greek (to 1453)](https://www.ethnologue.com/language/grc) | Indo-European | N  | Y  |   |
| ell/gre | [Modern Greek (1453-)](https://www.ethnologue.com/language/ell) | Indo-European | Y  | Y  |   |
| guj | [Gujarati](https://www.ethnologue.com/language/guj) | Indo-European > Indo-Iranian | N  | Y  |   |
| heb | [Hebrew](https://www.ethnologue.com/language/heb) | Afro-Asiatic > Semitic |  Y | N |   |
| hin | [Hindi](https://www.ethnologue.com/language/hin) | Indo-European > Indo-Iranian |  Y | Y  |   |
| hrv | [Croatian](https://www.ethnologue.com/language/hrv) | Indo-European > Balto-Slavic |  Y | Y  |   |
| hun | [Hungarian](https://www.ethnologue.com/language/hun) | Uralic | Y  | Y  |   |
| ind | [Indonesian](https://www.ethnologue.com/language/ind) | Austronesian > Malayo-Polynesian |  Y | Y  |   |
| isl | [Icelandic](https://www.ethnologue.com/language/isl) | Indo-European > Germanic |  Y |  Y |   |
| ita | [Italian](https://www.ethnologue.com/language/ita) | Indo-European > Italic| Y  | Y  |   |
| jak | [Jakun](https://www.ethnologue.com/language/jak) | Austronesian > Malayo-Polynesian | N  | Y  |   |
| jap | [Japanese](https://www.ethnologue.com/language/jpn) | Japonic |  Y |  Y |   |
| jiv | [Shuar](https://www.ethnologue.com/language/jiv) | Jivaroan |  N | Y  |   |
| kab | [Kabyle-Amazigh](https://www.ethnologue.com/language/kab) | Afro-Asiatic > Berber |  N | Y  |   |
| kbh | [Camsá](https://www.ethnologue.com/language/kbh) | Isolate | N  | Y |   |
| kor | [Korean](https://www.ethnologue.com/language/kor) | Koreanic | Y  | Y  |   |
| lat | [Latin](https://www.ethnologue.com/language/lat) | Indo-European > Italic|  Y | Y  |   |
| lav | [Latvian](https://www.ethnologue.com/language/lav) | Indo-European > Balto-Slavic| N  | Y  |   |
| lit | [Lithuanian](https://www.ethnologue.com/language/lit) | Indo-European > Balto-Slavic|  Y | Y  |   |
| mal | [Malayalam](https://www.ethnologue.com/language/mal) | Dravidian | Y  |  Y |   |
| mam | [Mam](https://www.ethnologue.com/language/mam) | Mayan |  N |  Y |   |
| mao | [Maori](https://www.ethnologue.com/language/mri) | Austronesian > Malayo-Polynesian |  Y |  Y |   |
| mar | [Marathi](https://www.ethnologue.com/language/mar) | Indo-European > Indo-Iranian |  Y |  Y |   |
| mya | [Burmese](https://www.ethnologue.com/language/mya) | Sino-Tibetan > Tibeto-Burman|  Y | Y  |   |
| nep | [Nepali](https://www.ethnologue.com/language/nep) | Indo-European > Indo-Iranian |  Y | Y  |   |
| nhg | [Tetelcingo Nahuatl](https://www.ethnologue.com/language/nhg) | Uto-Aztecan |  N | Y  |   |
| nld | [Dutch](https://www.ethnologue.com/language/nld) |  Indo-European > Germanic|  Y | Y  |   |
| nor | [Norwegian](https://www.ethnologue.com/language/nor) |  Indo-European > Germanic| Y  |  Y |   |
| ojb | [Northwestern Ojibwa](https://www.ethnologue.com/language/ojb) | Algic > Algonquian |  N |  Y |   |
| pck | [Paite Chin](https://www.ethnologue.com/language/pck) | Sino-Tibetan > Tibeto-Burman | Y  |  Y |   |
| pes | [Iranian Persian](https://www.ethnologue.com/language/pes) | Indo-European > Indo-Iranian |  Y |  Y |   |
| plt | [Plateau Malagasy](https://www.ethnologue.com/language/plt) | Austronesian > Malayo-Polynesian |  Y | Y  |   |
| pol | [Polish](https://www.ethnologue.com/language/pol) | Indo-European > Balto-Slavic|  Y |   Y|   |
| por | [Portuguese](https://www.ethnologue.com/language/por) | Indo-European > Italic|  Y | Y  |   |
| pot | [Potawatomi](https://www.ethnologue.com/language/pot) | Algic > Algonquian | N  | Y  |   |
| ppk | [Uma](https://www.ethnologue.com/language/ppk) | Austronesian > Malayo-Polynesian | N  |  Y |   |
| quc | [K'iche'](https://www.ethnologue.com/language/quc) | Mayan |  N | Y  |   |
| quw | [Tena Lowland Quichua](https://www.ethnologue.com/language/quw) | Quechuan | N  | Y  |   |
| rom | [Romany](https://www.ethnologue.com/language/rom) | Indo-European > Indo-Iranian |  N |  Y |   |
| ron/rum | [Romanian](https://www.ethnologue.com/language/ron) | Indo-European > Italic|  Y | Y  |   |
| rus | [Russian](https://www.ethnologue.com/language/rus) | Indo-European > Balto-Slavic|  Y | Y  |   |
| shi | [Tachelhit](https://www.ethnologue.com/language/shi) | Afro-Asiatic > Berber | N  | Y  |   |
| slk | [Slovak](https://www.ethnologue.com/language/slk) | Indo-European > Balto-Slavic| Y  |  Y |   |
| slv | [Slovenian](https://www.ethnologue.com/language/slv) | Indo-European > Balto-Slavic |  Y |  Y |   |
| sna | [Shona](https://www.ethnologue.com/language/sna) | Niger-Congo > Atlantic-Congo | Y  | Y |   |
| som | [Somali](https://www.ethnologue.com/language/som) | Afro-Asiatic > Cushitic | Y  |   Y|   |
| spa | [Spanish](https://www.ethnologue.com/language/spa) | Indo-European > Italic |  Y |  Y |   |
| srp | [Serbian](https://www.ethnologue.com/language/srp) | Indo-European > Balto-Slavic | Y  | Y  |   |
| ssw | [Swati](https://www.ethnologue.com/language/ssw) | Niger-Congo > Atlantic-Congo |  N |  Y |   |
| swe | [Swedish](https://www.ethnologue.com/language/swe) | Indo-European > Germanic |  Y | Y  |   |
| syr | [Syriac](https://www.ethnologue.com/language/syr) | Afro-Asiatic > Semitic |  N |  Y |   |
| tel | [Telugu](https://www.ethnologue.com/language/tel) | Dravidian | Y  | Y  |   |
| tgl | [Tagalog](https://www.ethnologue.com/language/tgl) | Austronesian > Malayo-Polynesian | Y  |  Y |   |
| tha | [Thai](https://www.ethnologue.com/language/tha) | Kra-Dai > Tai | Y  |  Y |   |
| tmh | [Tamashek](https://www.ethnologue.com/language/tmh) | Afro-Asiatic > Berber  | Y  | Y  |   |
| tur | [Turkish](https://www.ethnologue.com/language/tur) | Turkic |  Y | Y  |   |
| ukr | [Ukrainian](https://www.ethnologue.com/language/ukr) | Indo-European > Balto-Slavic | N  |  Y |   |
| usp | [Uspanteco](https://www.ethnologue.com/language/usp) | Mayan |  N |  Y |   |
| wal | [Wolaytta](https://www.ethnologue.com/language/wal) | Afro-Asiatic > Omotic |  N |  Y |   |
| wol | [Wolof](https://www.ethnologue.com/language/wol) | Niger-Congo > Atlantic-Congo |  N |  Y |   |
| xho | [Xhosa](https://www.ethnologue.com/language/xho) | Niger-Congo > Atlantic-Congo | Y  |  Y |   |
| zul | [Zulu](https://www.ethnologue.com/language/zul) | Niger-Congo > Atlantic-Congo |  N |  Y |   |

# TODO
1. Include the following languages: 
a. In all models: *vie*, *kan*, *djk*, *kek*, *agr*, *mal*
b. In *model4-LC-P* only: *mar*, *mya*, *nep*, *tel*
2. Fix issue with display of some non-Latin characters in PDF output (notably all Arabic!). Note that the characters display normally in R studio (i.e. it must be an issue with both base R *pdf* and *CairoPDF*).
3. Add references for Kriging method
4. Add info on how NULLs are treated in the models
7. Add on how many NAs we have per language based on best model
8. Add what the best model is, and why.

## References
<a id="1">[1]</a> 
Junczys-Dowmunt, Marcin & Arkadiusz Szał. 2012. SyMGiza++: Symmetrized Word Alignment Models for Machine Translation. In Pascal Bouvry, Mieczyslaw A. Klopotek, Franck Leprévost, Malgorzata Marciniak, Agnieszka Mykowiecka & Henryk Rybinski (eds.), *Security and Intelligent Information Systems (SIIS)* (Lecture Notes in Computer Science 7053), 379-390. Heidelberg-Berlin: Springer.

<a id="2">[2]</a> 
Wälchli, Bernhard. 2010. Similarity Semantics and Building Probabilistic Semantic Maps from Parallel Texts. *Linguistic Discovery* 8(1). 331-371. DOI:[10.1349/PS1.1537-0852.A.356](http://dx.doi.org/10.1349/PS1.1537-0852.A.356)