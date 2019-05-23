"""
Code Challenge
  Name: 
    Vocabulary
  Filename: 
    Vocabulary.py
  Problem Statement:
    Novel = james_joyce_ulysses.txt
    The claim is that James Joyce used in his novel more words than any other author. 
    Actually his vocabulary is above and beyond all other authors, 
    maybe even Shakespeare.
    
    1. Find the total number of words in the novel
    2. many words occur multiple time:["the", "while", "good", "bad", "ireland", "irish"]
    3. Quality of a novel is the number of different words.
       Find the number of different words used
    4. look at the other novels and find the total words and unique words for comparison
       novels = ['sons_and_lovers_lawrence.txt',
          'metamorphosis_kafka.txt',
          'the_way_of_all_flash_butler.txt',
          'robinson_crusoe_defoe.txt',
          'to_the_lighthouse_woolf.txt',
          'james_joyce_ulysses.txt',
          'moby_dick_melville.txt']

    5. Special Words in Ulysses novel by comparing with others, 
       words which are only used in Ulysses, store it in a file

    6. Common Words - Find the words which occur in every book.

  Hint: 
     Use Dictionary, Sets, Regex, File Handling
     re.findall(r"\b[\w-]+\b", ulysses_txt)
     
"""

import re
fp = open('james_joyce_ulysses.txt', 'r')
ulysses_txt = fp.read()
all_words = re.findall(r"\b[\w-]+\b", ulysses_txt)
unique_words = set(re.findall(r"\b[\w-]+\b", ulysses_txt))
tot_unique_words = len(unique_words)
tot_all_words = len(all_words)
fp.close()

print('unique_words = {0}, tot_unique_words = {1}, tot_all_words = {2}'.format(unique_words,tot_unique_words,tot_all_words))
novels = ['sons_and_lovers_lawrence.txt',
          'metamorphosis_kafka.txt',
          'the_way_of_all_flash_butler.txt',
          'robinson_crusoe_defoe.txt',
          'to_the_lighthouse_woolf.txt',
          'moby_dick_melville.txt']

special = set()
common = set()
true = {}
true['james_joyce_ulysses.txt'] = unique_words

for novel in novels:
    new = open(novel,'r')
    new_read = new.read()
    new_unique_words = set(re.findall(r"\b[\w-]+\b", ulysses_txt))
    print('new_unique_words = ',new_unique_words)
    new.close()
    for word in unique_words:
        if word not in new_unique_words:
            special.add(word)
    true[new] = len(new_unique_words)
    common.update(unique_words.intersection(new_unique_words)
