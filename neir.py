import pandas as pd
import numpy as np
import tensorflow as tf
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from tensorflow import keras
from tensorflow.keras import layers


#Загрузка данных из CSV файлов
table1_data = pd.read_csv('data.csv')   #файл с параметрами
table2_data = pd.read_csv('answdata.csv')    #файл с результатом 
table_new_data = pd.read_csv('newdata.csv') #файл с данными для проверки

# Объединение данных из двух таблиц
combined_data = pd.merge(table1_data, table2_data, on="map", "data")  # Замените 'common_column' на общий столбец

combined_data = combined_data.drop('data', 'map', axis=1)  # Исключение столбца "name", который не является числовым признаком

X = np.random.rand(num_examples, num_features)
# Генерация случайных целевых переменных (результатов) в диапазоне от 0 до 1
y = np.random.rand(num_examples)

# Выбор признаков (параметры) и целевой переменной (результат)
X = data.values # признаки
y = answdata.values # целевые данные

# Разделение данных на тренировочный и тестовый наборы
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Нормализация данных
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# Создание модели нейронной сети
model = keras.Sequential([
    layers.Dense(64, activation='relu', input_shape=(X_train.shape[1],)),
    layers.Dense(32, activation='relu'),
    layers.Dense(1, activation='softmax') # Многоклассовая классификация
])

print(model.summary())

# Компиляция модели
model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

# Обучение модели
model.fit(X_train, y_train, epochs=100000, batch_size=64, validation_split=0.2)

# Оценка модели
loss = model.evaluate(X_test) # чем выше тем хуже (метрики)
accuracy = model.evaluate(y_test)
# сохраняем модель
model.save("mcs")
model_restore = tf.saved_model.load("mcs")


new_data = pd.read_csv('newdata.csv')  # Файл с новыми данными для предсказания

# Нормализация новых данных с использованием того же скалировщика, что и для обучающих данных
new_data = scaler.transform(new_data)

# Предсказание на новых данных
predictions = model.predict(new_data)

# Нормализация новых данных
X_new = scaler.transform(new_data)

# Предсказание результатов на новых данных
predictions = model.predict(X_new)
print(f'Потери: {loss}')
print(f'Точность: {accuracy}')
print(f'Прогноз результатов для новых данных: {predictions}')
