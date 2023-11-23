# https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestClassifier.html#sklearn.ensemble.RandomForestClassifier
# https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.KNeighborsClassifier.html#sklearn-neighbors-kneighborsclassifier
# https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.train_test_split.html
import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

def read_data(pFile, pNotNull = False):
    try:
        dfAux= pd.read_csv(pFile)

        if (pNotNull == True):
            dfAux = dfAux.dropna()
    except:
        dfAux = []
        print('Não foi possível ler o arquivo. Contate o suporte.')

    return dfAux

def transform_column_object_text(pDF, pColumns = []):
    try:
        transform = LabelEncoder()
        dfAux = pDF
        for pColumn in pColumns:
            if dfAux[pColumn].dtype == 'object':
                dfAux[pColumn] = transform.fit_transform(dfAux[pColumn])
    except:
        dfAux = []
        print('Não foi possível transformar as colunas. Contate o suporte.')

    return dfAux

def importance(pColumns, pModel):
    try:
        dfAux = pd.DataFrame(index=pColumns, data=pModel.feature_importances_)
    except:
        dfAux = []
        print('Não foi possível calcular a importância das colunas. Contate suporte.')

    return dfAux * 100

def train_test_y(pDF, xDrop, xAxis, yCalc, pTestSize, pRandom, pModel, new_forecast = ''):
    try:
        dfAux = pDF
        x = dfAux.drop(xDrop, axis=xAxis)
        y = dfAux[yCalc]

        x_treino, x_teste, y_treino, y_teste = train_test_split(x, y, test_size=pTestSize, random_state=pRandom)

        if (pModel.upper() == 'KNN'):
            model_knn = KNeighborsClassifier()
            model_knn.fit(x_treino, y_treino)
            forecast_knn = model_knn.predict(x_teste.to_numpy())
            print(importance(list(x_teste.columns), model_knn))
            pReturn = accuracy_score(y_teste, forecast_knn)

        if (pModel.upper() == 'TREE'):
            model_tree = RandomForestClassifier()
            model_tree.fit(x_treino, y_treino)
            forecast_tree = model_tree.predict(x_teste)
            print(importance(list(x_teste.columns), model_tree))
            pReturn = accuracy_score(y_teste, forecast_tree)
            if new_forecast != '':
                print(model_tree.predict(new_forecast))

    except:
        pReturn = 0
        print('Não foi possível treinar o modelo. Contate suporte.')        
    
    return pReturn

# Listar nomes das colunas
#print(df.columns)

# Listar informacões dos campos
# print(df.info())

df = transform_column_object_text(read_data("clientes.csv"), ['profissao','mix_credito','comportamento_pagamento'])
#print(df.info())
npDF = transform_column_object_text(read_data("novos_clientes.csv"), ['profissao','mix_credito','comportamento_pagamento'])

print(train_test_y(df, ['score_credito', 'id_cliente'], 1, 'score_credito', 0.3, 1, 'tree'))


