# parallelbibles

## Requirements

1. Installation and dependencies: 

Clone the repository:

`$ git clone https://github.com/npedrazzini/parallelbibles`

From the root directory (./parallelbibles), build the repository by running:

`$ make`

This will download and build [SyMGIZA++](https://github.com/emjotde/symgiza-pp), and install the required dependencies.

2. XML files, which can be of two formats:
 
a. OPUS (untokenized) (https://opus.nlpl.eu/bible-uedin.php)

b. PROIEL

In this repository there are currently PROIEL XMLs for New Testament Greek, Old Church Slavonic and Gothic, but those in any languages (for which a Bible translation exists) can be downloaded from https://proiel.github.io, provided that they are not already covered by OPUS (e.g. Latin).

## Train word-alignment models

This step will: 

1. convert OPUS/PROIEL XML files to GIZA-readable CSV files
2. train a word-alignment model for each target language
3. make GIZA's outputs easily readable and queryable 

From the root directory simply run: 

`$ ./train.sh`

This will ask you:
1. to specify the input XML format (OPUS, PROIEL, or mixed)
2. to enter the desired source language
3. to enter the target languages
4. whether you want your model to strip punctuation
5. whether you want to bring everything to lowercase
6. to provide a name for your model

NB: the chosen languages must be entered in their ISO 639-2(B) code. See [here](https://www.loc.gov/standards/iso639-2/php/code_list.php) for a list.

## Extract a word and its translations

This step will:
1. extract every occurrence of a word in the source language and its translation in the target languages.
2. output a CSV file for each word. The file will contain one occurrence per line, its citation (Bible verse), context, and the translations in each target language. 

From the root directory simply run: 

`$ ./extract.sh`

This will prompt you to enter:
1. the name of the model you want to use
2. a target word

NB:
- *NULL* will indicate that the model did not find a match for the word in the target language
- *NA* will indicate that the target language did not have a Bible translations of that particular verse in the first place (e.g. some languages lack a translation for the whole Old Testament). 

# Pretrained models

Four pretrained models currently come with this repository: 

1. *model1-UC-P*: **U**pper case and with **P**unctuation. English is source language. All other languages (both from OPUS and PROIEL; however see Disclaimer) are targets.
2. *model2-LC-NP*: **L**ower **C**ase and **N**o **P**unctuation. English is source language. All other languages (both from OPUS and PROIEL; however see Disclaimer) are targets.
3. *model3-UC-NP*: **U**pper **C**ase and **N**o **P**unctuation. English is source language. All other languages (both from OPUS and PROIEL; however see Disclaimer) are targets.
4. *model4-LC-P*: **L**ower **C**ase and **N**o **P**unctuation. English is source language. All other languages (both from OPUS and PROIEL; however see Disclaimer) are targets.

You can directly extract target words from either of these models by running `$ ./extract.sh`. You will be prompted to enter the name of the model you want to use.

# Disclaimer
The following languages are not yet included: 

a. From all models: *vie*, *kan*, *djk*, *kek*, *acu*, *agr*, *mal*

b. From *model4-LC-P* only: *mar*, *mya*, *nep*, *tel*