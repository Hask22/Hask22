from sklearn.linear_model import LinearRegression
import joblib


x = [[1], [2], [3], [4]]
y = [2, 4, 6, 8]


model = LinearRegression()

model.fit(x, y)

joblib.dump(model, "model.pkl")

print("Modèle sauvegardé")
