# streamlit local
import streamlit as st
import joblib
import datetime
import pandas as pd
from sklearn.preprocessing import PolynomialFeatures
import matplotlib.dates as mdates
import matplotlib.pyplot as plt
import math
from sklearn.metrics import mean_squared_error, r2_score

st.title("400k NYSE random investments + financial ratios with Buy price in each company")
labels = ('BBY', 'BAC', 'AXP', 'KSS', 'JPM', 'PEP', 'FB', 'UBS', 'DB', 'SC',
       'GM', 'M', 'AMZN', 'TSLA', 'WMT', 'MSFT', 'HMC', 'AAPL', 'COST',
       'NVDA', 'KO', 'HOG', 'PG', 'F', 'TGT', 'GOOG', 'OR')
company=st.selectbox("Select company:", labels)

df = pd.read_csv('https://raw.githubusercontent.com/sahathat/dataSci/main/machineLearning/supervised/Regression/final_transactions_dataset.csv', sep=",")
bank_df = df[df["company"]==company].sort_values('date_BUY_fix')
X_plot = bank_df[['date_BUY_fix','Volatility_Buy','inflation','price_BUY']].copy().drop_duplicates()

X_plot['date_BUY_fix']=pd.to_datetime(X_plot['date_BUY_fix'])
X = X_plot.copy()

# convert date to int
X['date_BUY_fix']=X['date_BUY_fix'].astype('int64') // 10**9

X_select = X[['date_BUY_fix','Volatility_Buy','inflation']].copy()
Y = X[['price_BUY']].copy()

# Create Polynomial features
deg = 3
poly_features = PolynomialFeatures(degree=deg)
X_poly = poly_features.fit_transform(X_select)

# Make predictions for the same X values
file_name = f"machineLearning/supervised/Regression/models/{company}_polynomial_model.pkl"
load_model = joblib.load(file_name)
Y_train_pred = load_model.predict(X_poly)

# Plot the data points and the regression line
fig = plt.figure(figsize=(16,10))
# Create a date range
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y'))
plt.gca().xaxis.set_major_locator(mdates.YearLocator())
plt.scatter(X_plot['date_BUY_fix'] ,Y , color ='blue')
plt.plot(X_plot['date_BUY_fix'] ,Y_train_pred , label ='Regression Line', color ='red')
plt.gcf().autofmt_xdate()
plt.xlabel('date buy fix')
plt.ylabel('price buy')
plt.legend()
plt.title('Linear Regression ')
st.pyplot(fig)

# evaluation
st.write("evaluation table")
mse = mean_squared_error(Y,Y_train_pred)
rsme = math.sqrt(mse)
r2 = r2_score(Y,Y_train_pred)
evaluation = pd.DataFrame({
    "Mean Square Error": [round(mse,4)],
    "Root Mean Square Error": [round(rsme,4)],
    "R-square": [round(r2,4)]
})
st.table(evaluation)

st.header("Enter buy date fix to predict buy price")
date_buy_fix = st.date_input("date buy fix:",datetime.datetime.now())
volatility_buy = st.slider("volatility buy:",0.0,1.0,0.5,0.01)
inflation = st.slider("inflation value:",-1.0,2.0,0.0,0.01)

# Get the coefficients ( slope and intercept )
slope = load_model.coef_[0]
intercept = load_model.intercept_

try:
    buy_time = pd.DataFrame({'time': [pd.to_datetime(date_buy_fix)]})

    date_buy_fix=pd.to_datetime(buy_time['time']).astype('int64') // 10**9

    new_data = pd.DataFrame({
        'date_BUY_fix': [date_buy_fix],
        'Volatility_Buy': [volatility_buy],
        'inflation': [inflation]
    })

    # Create Polynomial features
    deg = 3
    poly_features = PolynomialFeatures(degree=deg)
    X_poly_test = poly_features.fit_transform(new_data)

except ValueError:
    st.error("Invalid input, please Input number again")
    new_data = None

# Make predictions for the same X values
Y_test_pred = load_model.predict(X_poly_test)

st.write("Buy Price with", Y_test_pred[0])