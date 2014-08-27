from sklearn import linear_model
import numpy as np

# Load data
f = open("ticker.log", "r")
data = np.loadtxt(f)
ticker_x_train=np.array([[x[0]] for x in data])
ticker_y_train=np.array([x[1] for x in data])
#print('Fitting ' + str(len(ticker_y_train)) + ' training examples')

# Train model
regr = linear_model.LinearRegression()
regr.fit(ticker_x_train, ticker_y_train)

# Predict Result
print(float(regr.predict(np.array([[8000000000]]))))

