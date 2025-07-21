import pandas as pd 
import re 

#ler arquivos como dataframe
topik1 = pd.read_csv("./data/TOPIK I 1847 word.csv", on_bad_lines='warn')
yukcheon = pd.read_csv("./data/한국어 학습용 어휘 목록 unmodified.csv", on_bad_lines='warn') #recomendado realizar testes com um arquivo menor 

for x in topik1['한국어']:
    word_idx = topik1.index[topik1['한국어'] == x][0] #importante para a transposição do dado
    if yukcheon['단어'].str.fullmatch(x).any(): #NÃO usar combination. match talvez, mas preferi fullmatch
        location_yukcheon = yukcheon.index[yukcheon['단어'] == x] #encontrar fullmatches entre as 2 colunas de palavras
        location_idx = location_yukcheon[0] #importante para a transposição do dado
        topik1.loc[word_idx, 'Frequency'] = yukcheon.loc[location_idx, '순위'] #transposição 
        #print(topik1.loc[word_idx, 'Frequency']) #conferir

topik1.to_csv('./results/TOPIK-I_2.csv')
print('created csv 1')

#algumas palavras tinham dígitos indicando significados diferentes e não davam fullmatch
#essa ainda não é a solução ideal, mas funciona por hora

words = yukcheon['단어']
words_nos = [word for word in words if re.search(r'[0-9]', word)] 

yukcheon['단어 Revised'] = ''

for word in words:
    word_idx = yukcheon.index[yukcheon['단어'] == word][0]
    no_nos = re.sub(r'[0-9]', '', word)

yukcheon.loc[word_idx, '단어 Revised'] = no_nos
yukcheon.to_csv('./results/frequency_revised.csv')
sixk = pd.read_csv('./results/frequency_revised.csv')
print('created csv 2')

for x in topik1['한국어']:
        word_idx = topik1.index[topik1['한국어'] == x][0]
        if sixk['단어 Revised'].str.fullmatch(x).any():
                        location_sixk = sixk.index[sixk['단어 Revised'] == x]
                        location_idx = location_sixk[0] 
                        topik1.loc[word_idx, 'Frequency'] = sixk.loc[location_idx, '순위']

topik1.to_csv('./results/TOPIK_I-frequency-Revised.csv')
print('created csv 3')

print('finished successfully')