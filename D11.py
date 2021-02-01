import pandas as pd

q_df = pd.DataFrame([['male', 'teacher'], 
              ['male', 'engineer'],
              ['female', None],
              ['female', 'engineer']],columns=['Sex','Profession'])

#D11#1
q_df=q_df.fillna('others')
print(q_df)

from sklearn.preprocessing import LabelEncoder
q_df['Profession_label'] = LabelEncoder().fit_transform(q_df['Profession'].values)
print(q_df)

#使用順序性編排職業類別，方便做統計與索引