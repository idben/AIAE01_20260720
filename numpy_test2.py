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
discounts = np.array([85, 88, 70, 92])
new_prices = prices * (discounts / 100)
print(new_prices)

# 布林遮罩      # 回傳 True/False 的等長度 array
# >=80
is_high_scores = scores >= 80
print(is_high_scores)
high_scores = scores[is_high_scores] # 需要再用原始 array 對應出結果
print(high_scores)
print("-"*30)

prices_test2 = np.array([120, 80, 200, 150, 60])
discount_prices_test2 = prices_test2 * 0.8
mask1 = discount_prices_test2 >= 100
print(discount_prices_test2)
print(mask1)
ori_prices_test2 = prices_test2[mask1]
print(ori_prices_test2)
print("-"*30)

# day1 下午開始
# 一維陣列取平均/最高/最低/總和
print(f"平均分數是: {scores.mean()}")
print(f"最高分是: {scores.max()}")
print(f"最低分是: {scores.min()}")
print(f"分數的總和是: {scores.sum()}")

# 二維陣列取平均/最高/最低/總和
scores_ary = np.array([
    [80, 90, 75],
    [88, 76, 92],
    [60, 85, 70],
    [95, 91, 89],
])
# 對各維度的內容做整體的加總及平均
# 以成績單這樣的範例特性來，似乎較沒意義
print(f"平均分數是: {scores_ary.mean()}")
print(f"最高分是: {scores_ary.max()}")
print(f"最低分是: {scores_ary.min()}")
print(f"分數的總和是: {scores_ary.sum()}")

st1_avg_score = scores_ary[0].mean().round(1) # .round(1) 小數點下取一位
print(f"1 號學生的平均分數是: {st1_avg_score}")
# 使用迴圈印出上面那句

# 算出 A 科的平均分數
subject_names = ["A", "B", "C"]
a_avg_score = scores_ary[:, 0].mean()
# print(f"A 學科的平均分數是: {a_avg_score}")

for index, name in enumerate(subject_names):
    print(f"{name} 學科的平均分數是: {scores_ary[:, index].mean()}")