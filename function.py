import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

def fit_model1(data):
    """
    param: dataset
    return: coefs of our LR model
    """
    # reads the dataset with the pandas library
    df = pd.read_csv("Ass1.csv")
    # removing the column of index
    df = df.drop("Unnamed: 0", axis=1)
    # assiging the feature columns(Voltage, External Force) to our X variable
    X = df.iloc[:,:-1]
    # assiging the Electron Velocity which is the output to our y variable
    y = df.iloc[:,-1]
    # splitting our dataset into 2 segments (train and test set)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=42)
    # initiating our linear regression model
    # and fitting it on our dataset
    reg = LinearRegression().fit(X_train, y_train)
    # returning the coeffecients of the model
    return reg.coef_
