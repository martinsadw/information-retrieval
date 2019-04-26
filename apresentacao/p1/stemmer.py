import re
import random

import Stemmer


stemmer = Stemmer.Stemmer('portuguese')

sample_size = 10

words = set()
with open('words.txt', encoding='utf8') as file:
    words = {word.rstrip() for line in file for word in line.split(' ')}

sample = random.sample(words, sample_size)
stem_sample = stemmer.stemWords(sample)

word_size = len(max(sample, key=len))

print('Amostra de palavras:')
for i in range(sample_size):
    print('%s -> %s' % (sample[i].rjust(word_size+1), stem_sample[i]))

result = set(stemmer.stemWords(words))

print('\nSem stemmização: %d palavras' % len(words))
print('Com stemmização: %d palavras' % len(result))
