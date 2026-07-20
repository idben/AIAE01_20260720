import numpy as np

scores = np.array([80, 90, 75, 60, 95])
scores1 = scores + 5                # 對 numpy array 中的所有內容一起加 5
print(scores1)

prices = np.array([100, 200, 150, 80])
prices2 = prices * 0.9              # 通通打九折後的金額
print(prices2)
prices3 = prices - 20               # 通通折 20 元後的金額
print(prices3)

# 讓兩組 array 互相做運算，以索引值對照
prices = np.array([100, 100, 100, 100])
# discount = np.array([85, 88, 70, 92, 64]) # 長度不對等時會 ValueError
discount = np.array([85, 88, 70, 92])
new_prices = prices * (discount / 100)
print(new_prices)