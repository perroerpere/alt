import pandas as pd
import openpyxl
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import max_error
from sklearn.metrics import mean_squared_error
from sklearn.metrics import r2_score
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.linear_model import Ridge
from sklearn.tree import DecisionTreeRegressor
from sklearn.linear_model import Lasso
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import max_error



data = pd.read_excel("BatteryTestReport_28052024.xlsx")

print(data.head())

x = data.drop(["Name", "SiteID", "IP_Address", "BBU_Solution_", "RestCapasity", "loc", "ip"], axis=1)

print(data.dtypes)
print("__________________________")
print(data.isna().sum())
print("__________________________")
print(len(data))
print("__________________________")
print(data.describe())



corr = x.corr()

plt.figure(figsize = (10,8))

sns.heatmap(corr, annot=True, cmap='coolwarm', vmin=-1,vmax=1)
plt.show()




