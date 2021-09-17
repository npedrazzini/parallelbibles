# parallelbibles

Word-alignment models for Bible translations in 100+ historical and contemporary languages


## Requirements

1. Installation and dependencies: 

Download or clone the repository:

`$ git clone https://github.com/npedrazzini/parallelbibles`

From the root directory (./parallelbibles), build the repository:

`$ make`

This will download and build [SyMGIZA++](https://github.com/emjotde/symgiza-pp), and install all the required dependencies.

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

> These scripts are an adaptation of the code by [[1]](#1).

- `./scripts/MDS-simple.py`: simple multi-dimensional scaling (MDS).
- `./scripts/MDS-kriging.py`: multi-dimensional scaling + Kriging (to draw lines around clusters probabilstically).

By running either of the scripts you will be prompted to enter:
1. the name of the model you want to use.
2. a target word.

This will create a directory *modelname/\_TARGETWORDS\_/word-MDS*, containing all the outputs. The relevant ones to plot semantic maps will be: 
- *word-MDS.R*: an R script to generate the semantic maps.
- *word-data.txt*: the original data.
- *word-matrix.txt*: distance matrix between source word and target words.

By running *word-MDS.R* in R (the folder *modelname/\_TARGETWORDS\_/word-MDS* can also be opened as an R project) a PDF file will be generated containing all the plots (of either the simple-MDS or the MDS+Kriging type).

# Pretrained models

Four pretrained models currently come with this repository: 

1. *model1-UC-P*: **U**pper case and with **P**unctuation. English is source language. All other languages (both from OPUS and PROIEL; however see Disclaimer) are targets.
2. *model2-LC-NP*: **L**ower **C**ase and **N**o **P**unctuation. English is source language. All other languages (both from OPUS and PROIEL; however see Disclaimer) are targets.
3. *model3-UC-NP*: **U**pper **C**ase and **N**o **P**unctuation. English is source language. All other languages (both from OPUS and PROIEL; however see Disclaimer) are targets.
4. *model4-LC-P*: **L**ower **C**ase and **N**o **P**unctuation. English is source language. All other languages (both from OPUS and PROIEL; however see Disclaimer) are targets.

You can directly extract target words from either of these models by running `$ ./extract.sh`. You will be prompted to enter the name of the model you want to use.

# Languages
| ISO 639-3 | Language | Language family | Notes |
|---|---|---|---|
| acu | [Achuar-Shiwiar](https://www.ethnologue.com/language/acu) | Jivaroan |  |
| afr | [Afrikaans](https://www.ethnologue.com/language/afr) | Indo-European > Germanic |  |
| agr | [Awajún](https://www.ethnologue.com/language/agr) | Jivaroan |  |
| ake | [Akawaio](https://www.ethnologue.com/language/ake) | Cariban |  |
| sqi/alb | [Albanian](https://www.ethnologue.com/language/sqi) | Indo-European|  |
| amh | [Amharic](https://www.ethnologue.com/language/amh) | Afro-Asiatic > Semitic |  |
| amu | [Guerrero Amuzgo](https://www.ethnologue.com/language/amu) | Otomanguean |  |
| ara | [Arabic](https://www.ethnologue.com/language/ara) | Afro-Asiatic > Semitic |  |
| hye/arm | [Armenian](https://www.ethnologue.com/language/hye) | Indo-European |  |
| baq | [Basque](https://www.ethnologue.com/language/eus) | Isolate |  |
| bsn | [Barasana-Eduria](https://www.ethnologue.com/language/bsn) | Tucanoan |  |
| bul | [Bulgarian](https://www.ethnologue.com/language/bul) | Indo-European > Balto-Slavic |  |
| cak | [Kaqchikel](https://www.ethnologue.com/language/cak) | Mayan |  |
| ceb | [Cebuano](https://www.ethnologue.com/language/ceb) | Austronesian > Malayo-Polynesian |  |
| cha | [Chamorro](https://www.ethnologue.com/language/cha) | Austronesian > Malayo-Polynesian |  |
| zho/chi | [Chinese](https://www.ethnologue.com/language/zho) | Sino-Tibetan > Sinitic |  |
| chq | [Quiotepec Chinantec](https://www.ethnologue.com/language/chq) | Otomanguean |  |
| chr | [Cherokee](https://www.ethnologue.com/language/chr) | Iroquoian |  |
| chu | [Church Slavonic](https://www.ethnologue.com/language/chu) | Indo-European > Balto-Slavic|  |
| cjp | [Cabécar](https://www.ethnologue.com/language/cjp) | Chibchan |  |
| cni | [Asháninka](https://www.ethnologue.com/language/cni) | Maipurean |  |
| cop | [Coptic](https://www.ethnologue.com/language/cop) | Afro-Asiatic > Egyptian |  |
| crp | [Creoles and pidgins](https://www.ethnologue.com/language/hat/24) | Creole > French-based | The original XML files have the generic 'crp' code. This is however Haitian Creole (code hat) |
| cze | [Czech](https://www.ethnologue.com/language/ces) | Indo-European > Balto-Slavic|  |
| dan | [Danish](https://www.ethnologue.com/language/dan) | Indo-European > Germanic|  |
| deu | [German](https://www.ethnologue.com/language/deu) | Indo-European > Germanic|  |
| dik | [Southwestern Dinka](https://www.ethnologue.com/language/dik) | Nilo-Saharan > Nilotic |  |
| dje | [Zarma](https://www.ethnologue.com/language/dje) |  Nilo-Saharan > Songhai |  |
| dop | [Lukpa](https://www.ethnologue.com/language/dop) | Niger-Congo > Atlantic-Congo |  |
| epo | [Esperanto](https://www.ethnologue.com/language/epo) | Constructed |  |
| est | [Estonian](https://www.ethnologue.com/language/est) | Uralic |  |
| ewe | [Ewe](https://www.ethnologue.com/language/ewe) | Niger-Congo > Atlantic-Congo |  |
| fin | [Finnish](https://www.ethnologue.com/language/fin) | Uralic |  |
| fra | [French](https://www.ethnologue.com/language/fra) | Indo-European > Italic|  |
| gbi | [Galela](https://www.ethnologue.com/language/gbi) | West Papuan |  |
| gla | [Scottish Gaelic](https://www.ethnologue.com/language/gla) | Indo-European > Celtic|  |
| glv | [Manx](https://www.ethnologue.com/language/glv) | Indo-European > Celtic|  |
| got | [Gothic]() | Indo-European > Germanic |  |
| grc | [Ancient Greek (to 1453)](https://www.ethnologue.com/language/grc) | Indo-European |  |
| ell/gre | [Modern Greek (1453-)](https://www.ethnologue.com/language/ell) | Indo-European |  |
| guj | [Gujarati](https://www.ethnologue.com/language/guj) | Indo-European > Indo-Iranian |  |
| heb | [Hebrew](https://www.ethnologue.com/language/heb) | Afro-Asiatic > Semitic |  |
| hin | [Hindi](https://www.ethnologue.com/language/hin) | Indo-European > Indo-Iranian |  |
| hrv | [Croatian](https://www.ethnologue.com/language/hrv) | Indo-European > Balto-Slavic |  |
| hun | [Hungarian](https://www.ethnologue.com/language/hun) | Uralic |  |
| ind | [Indonesian](https://www.ethnologue.com/language/ind) | Austronesian > Malayo-Polynesian |  |
| isl | [Icelandic](https://www.ethnologue.com/language/isl) | Indo-European > Germanic |  |
| ita | [Italian](https://www.ethnologue.com/language/ita) | Indo-European > Italic|  |
| jak | [Jakun](https://www.ethnologue.com/language/jak) | Austronesian > Malayo-Polynesian |  |
| jap | [Japanese](https://www.ethnologue.com/language/jpn) | Japonic |  |
| jiv | [Shuar](https://www.ethnologue.com/language/jiv) | Jivaroan |  |
| kab | [Kabyle-Amazigh](https://www.ethnologue.com/language/kab) | Afro-Asiatic > Berber |  |
| kbh | [Camsá](https://www.ethnologue.com/language/kbh) | Isolate |  |
| kor | [Korean](https://www.ethnologue.com/language/kor) | Koreanic |  |
| lat | [Latin](https://www.ethnologue.com/language/lat) | Indo-European > Italic|  |
| lav | [Latvian](https://www.ethnologue.com/language/lav) | Indo-European > Balto-Slavic|  |
| lit | [Lithuanian](https://www.ethnologue.com/language/lit) | Indo-European > Balto-Slavic|  |
| mal | [Malayalam](https://www.ethnologue.com/language/mal) | Dravidian |  |
| mam | [Mam](https://www.ethnologue.com/language/mam) | Mayan |  |
| mao | [Maori](https://www.ethnologue.com/language/mri) | Austronesian > Malayo-Polynesian |  |
| mar | [Marathi](https://www.ethnologue.com/language/mar) | Indo-European > Indo-Iranian |  |
| mya | [Burmese](https://www.ethnologue.com/language/mya) | Sino-Tibetan > Tibeto-Burman|  |
| nep | [Nepali](https://www.ethnologue.com/language/nep) | Indo-European > Indo-Iranian |  |
| nhg | [Tetelcingo Nahuatl](https://www.ethnologue.com/language/nhg) | Uto-Aztecan |  |
| nld | [Dutch](https://www.ethnologue.com/language/nld) |  Indo-European > Germanic|  |
| nor | [Norwegian](https://www.ethnologue.com/language/nor) |  Indo-European > Germanic|  |
| ojb | [Northwestern Ojibwa](https://www.ethnologue.com/language/ojb) | Algic > Algonquian |  |
| pck | [Paite Chin](https://www.ethnologue.com/language/pck) | Sino-Tibetan > Tibeto-Burman |  |
| pes | [Iranian Persian](https://www.ethnologue.com/language/pes) | Indo-European > Indo-Iranian |  |
| plt | [Plateau Malagasy](https://www.ethnologue.com/language/plt) | Austronesian > Malayo-Polynesian |  |
| pol | [Polish](https://www.ethnologue.com/language/pol) | Indo-European > Balto-Slavic|  |
| por | [Portuguese](https://www.ethnologue.com/language/por) | Indo-European > Italic|  |
| pot | [Potawatomi](https://www.ethnologue.com/language/pot) | Algic > Algonquian |  |
| ppk | [Uma](https://www.ethnologue.com/language/ppk) | Austronesian > Malayo-Polynesian |  |
| quc | [K'iche'](https://www.ethnologue.com/language/quc) | Mayan |  |
| quw | [Tena Lowland Quichua](https://www.ethnologue.com/language/quw) | Quechuan |  |
| rom | [Romany](https://www.ethnologue.com/language/rom) | Indo-European > Indo-Iranian |  |
| ron/rum | [Romanian](https://www.ethnologue.com/language/ron) | Indo-European > Italic|  |
| rus | [Russian](https://www.ethnologue.com/language/rus) | Indo-European > Balto-Slavic|  |
| shi | [Tachelhit](https://www.ethnologue.com/language/shi) | Afro-Asiatic > Berber |  |
| slk | [Slovak](https://www.ethnologue.com/language/slk) | Indo-European > Balto-Slavic|  |
| slv | [Slovenian](https://www.ethnologue.com/language/slv) | Indo-European > Balto-Slavic |  |
| sna | [Shona](https://www.ethnologue.com/language/sna) | Niger-Congo > Atlantic-Congo |  |
| som | [Somali](https://www.ethnologue.com/language/som) | Afro-Asiatic > Cushitic |  |
| spa | [Spanish](https://www.ethnologue.com/language/spa) | Indo-European > Italic |  |
| srp | [Serbian](https://www.ethnologue.com/language/srp) | Indo-European > Balto-Slavic |  |
| ssw | [Swati](https://www.ethnologue.com/language/ssw) | Niger-Congo > Atlantic-Congo |  |
| swe | [Swedish](https://www.ethnologue.com/language/swe) | Indo-European > Germanic |  |
| syr | [Syriac](https://www.ethnologue.com/language/syr) | Afro-Asiatic > Semitic |  |
| tel | [Telugu](https://www.ethnologue.com/language/tel) | Dravidian |  |
| tgl | [Tagalog](https://www.ethnologue.com/language/tgl) | Austronesian > Malayo-Polynesian |  |
| tha | [Thai](https://www.ethnologue.com/language/tha) | Kra-Dai > Tai |  |
| tmh | [Tamashek](https://www.ethnologue.com/language/tmh) | Afro-Asiatic > Berber  |  |
| tur | [Turkish](https://www.ethnologue.com/language/tur) | Turkic |  |
| ukr | [Ukrainian](https://www.ethnologue.com/language/ukr) | Indo-European > Balto-Slavic |  |
| usp | [Uspanteco](https://www.ethnologue.com/language/usp) | Mayan |  |
| wal | [Wolaytta](https://www.ethnologue.com/language/wal) | Afro-Asiatic > Omotic |  |
| wol | [Wolof](https://www.ethnologue.com/language/wol) | Niger-Congo > Atlantic-Congo |  |
| xho | [Xhosa](https://www.ethnologue.com/language/xho) | Niger-Congo > Atlantic-Congo |  |
| zul | [Zulu](https://www.ethnologue.com/language/zul) | Niger-Congo > Atlantic-Congo |  |

# TODO
1. Include the following languages: 
a. In all models: *vie*, *kan*, *djk*, *kek*, *agr*, *mal*
b. In *model4-LC-P* only: *mar*, *mya*, *nep*, *tel*
2. Fix issue with display of some non-Latin characters in PDF output (notably all Arabic!). Note that the characters display normally in R studio (i.e. it must be an issue with both base R *pdf* and *CairoPDF*).

## References
<a id="1">[1]</a> 
Wälchli, Bernhard. 2010. Similarity Semantics and Building Probabilistic Semantic Maps from Parallel Texts. *Linguistic Discovery* 8(1). 331-371. DOI:[10.1349/PS1.1537-0852.A.356](http://dx.doi.org/10.1349/PS1.1537-0852.A.356)