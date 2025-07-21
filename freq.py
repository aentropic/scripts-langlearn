import pandas as pd 

topik1 = pd.read_csv("TOPIK I 1847 word.csv", on_bad_lines='warn')
yukcheon = pd.read_csv("한국어 학습용 어휘 목록 unmodified.csv")
shorter = pd.read_csv("shorter 한국어 학습용 어휘 목록 - Página1.csv")

    for x in topik1['한국어']:
        word_idx = topik1.index[topik1['한국어'] == x][0]
        if yukcheon['단어'].str.fullmatch(x).any():
                        location_yukcheon = yukcheon.index[yukcheon['단어'] == x]
                        location_idx = location_yukcheon[0] 
                        topik1.loc[word_idx, 'Frequency'] = yukcheon.loc[location_idx, '순위']
                        print(topik1.loc[word_idx, 'Frequency'])                    

topik1.to_csv('TOPIK-I_2.csv')