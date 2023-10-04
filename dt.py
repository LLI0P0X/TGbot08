import numpy as np
import pandas as pd
pd.options.mode.chained_assignment = None

def UPD(group, link, id):
    id=str(id)
    #link='https://webservices.mirea.ru/upload/iblock/a19/7gqs3ytknabacms4oo2z838m3mnbz225/IKTST_1_k_vesna_22_23.xlsx'
    #group='БФБО-04-22'

    df=pd.DataFrame
    df=pd.read_excel(link)
    df.columns=map(str,range(len(df.columns)))

    for q in range(5,len(df.columns),5):
        if df.iloc[0][str(q)]==group:
            Nc=q
            break
    tdf=df.iloc[2:][map(str,range(5))]
    df=df.iloc[2:][map(str,range(Nc-4,Nc+4))]
    df.columns=('Unnamed: '+str(x) for x in range(1,9))

    df.drop(labels = range(86,107),axis = 0, inplace = True)
    df.drop(labels = range(0),axis = 0, inplace = True)

    for q in range(5):
        df['Unnamed: '+str(q)]=tdf[str(q)]
    df.to_csv('chats/'+id+'/dt_full.csv', index=False)
    df=pd.read_csv('chats/'+id+'/dt_full.csv')

    for q in range(len(df['Unnamed: 1'])):
        if str(df.iloc[q]['Unnamed: 1']) == 'nan':
            df['Unnamed: 1'][q]=df.iloc[q-1]['Unnamed: 1']
        else:
            df['Unnamed: 1'][q]=str(df.iloc[q]['Unnamed: 1']).replace('.0','')

    for q in range(len(df['Unnamed: 3'])):
        if str(df.iloc[q]['Unnamed: 3']) == 'nan':
            df['Unnamed: 3'][q]=df.iloc[q-1]['Unnamed: 3']
        else:
            df['Unnamed: 3'][q]=df.iloc[q]['Unnamed: 3'].replace('-',':')

    for q in range(len(df['Unnamed: 2'])):
        if str(df.iloc[q]['Unnamed: 2']) == 'nan':
            df['Unnamed: 2'][q]=df.iloc[q-1]['Unnamed: 2']
        else:
            df['Unnamed: 2'][q]=df.iloc[q]['Unnamed: 2'].replace('-',':')+"-"+df.iloc[q]['Unnamed: 3']
    df.pop('Unnamed: 3')
    df.pop('Unnamed: 4')

    for q in range(len(df['Unnamed: 1'])):
        for w in [1,2,5,6,7]:
            if str(df.iloc[q]['Unnamed: '+str(w)]).count('\n')!=0:
                df['Unnamed: '+str(w)][q] = df.iloc[q]['Unnamed: '+str(w)][:str(df.iloc[q]['Unnamed: '+str(w)]).find('\n')]

    df.to_csv('chats/'+id+'/dt_full.csv', index=False, header=False)
