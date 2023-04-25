# Word groups
Word groups is an effort to organize more than  370k english words. This projects aims to organize those words based on different categories and then stores those categorized words in a `JSON` format.

The sorting is based on different properties like
* Length of word
* First character of the word
* Both length and first character
* And hopefully many more in the future...

#### Source file
The words are located inside of `source-data/words_alpha.txt` and are delimited by `\n`. This file is obtained from [this repo](https://github.com/dwyl/english-words). This file contains 370105 words as of now. The words inside are alphabetically ordered from A to Z. 

#### Modified files
The source file are processed by using python scripts in `./python-scripts`.

