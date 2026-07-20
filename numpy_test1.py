import numpy as np

# 對串列中的數字 + 5
scores = [80, 90, 75, 60, 95]

# 原始方法
scores_1 = []

for score in scores:
    scores_1.append(score + 5)

print(scores_1)

# list 推導式方法
scores_2 = [score + 5 for score in scores]
print(scores_2)

# 使用 Numpy 的方法
# 把 list 轉成 np 的 arrau
scores_np = np.array(scores)
scores_3 = scores_np + 5
print(scores_3)
# [ 85  95  80  65 100]