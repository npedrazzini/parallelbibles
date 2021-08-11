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

NB: the chosen languages must be entered in their ISO 639-2(B) code. See [here](https://www.loc.gov/standards/iso639-2/php/code_list.php) for a list.

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

# TODO
1. Include the following languages: 
a. In all models: *vie*, *kan*, *djk*, *kek*, *acu*, *agr*, *mal*
b. In *model4-LC-P* only: *mar*, *mya*, *nep*, *tel*
2. Fix issue with display of some non-Latin characters in PDF output (notably all Arabic!). Note that the characters display normally in R studio (i.e. it must be an issue with both base R *pdf* and *CairoPDF*).

## References
<a id="1">[1]</a> 
Wälchli, Bernhard. 2010. Similarity Semantics and Building Probabilistic Semantic Maps from Parallel Texts. *Linguistic Discovery* 8(1). 331-371. DOI:[10.1349/PS1.1537-0852.A.356](http://dx.doi.org/10.1349/PS1.1537-0852.A.356)