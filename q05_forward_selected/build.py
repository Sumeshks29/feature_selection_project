# %load q05_forward_selected/build.py
# Default imports
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression

data = pd.read_csv('data/house_prices_multivariate.csv')

model = LinearRegression()


# Your solution code here

def forward_selected(data,model):
    X = data.iloc[:,:-1]
    y = data.iloc[:,-1]

    Variable_1=list()
    Variable_2=list()

    a=X.columns.tolist()
    NoC=len(X.columns)
    i=0
    while(i<NoC):
        i +=1
        dict1=dict()
        for c in (a):

            if(i==1):
                X_new=pd.DataFrame(X[c])

            else:
                X_new=pd.DataFrame()
                X_new=X_fin.copy()
                X_new[c]=X[c]
            reg=model.fit(X_new,y)
            r2_score=reg.score(X_new,y)
            dict1[c]=r2_score
        v=list(dict1.values())
        k=list(dict1.keys())
        if(i!=1):
            if(np.round(max(Variable_2),5)>=np.round(max(v),5) ):
                break
        Variable_1.append(k[v.index(max(v))])
        Variable_2.append(max(v))
        (a).remove(str(k[v.index(max(v))]))
        X_fin=X[Variable_1]
    return Variable_1,Variable_2

    
forward_selected(data,model)
len(data.columns)

