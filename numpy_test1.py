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
print(scores_3)             # [ 85  95  80  65 100] 
print(type(scores_3))       # numpy.ndarray


print(scores_3.shape)       # array 的形狀: 各維度中的長度 (5,) tuple, 只有一個數字 5
print(scores_3.ndim)        # 維度: 是一維還是二維陣列
print(scores_3.dtype)       # 陣列中的資料形態
print(f"索引值 0 的資料是 {scores_3[0]}")
print(f"第三筆的資料是 {scores_3[2]}")
print(f"最後一科的分數是 {scores_3[-1]}")
print("-"*40)

scores_4 = np.array([
    [80, 90, 75],
    [88, 76, 92],
    [60, 85, 70],
    [95, 91, 89],
])

print(scores_4.ndim)        # 2，二維陣列
print(scores_4.shape)       # (4, 3) 第一維中長度 4，第二維長度 3
print(scores_4.dtype)       # int64，資料型態，整數
print(scores_4[0, 0])
print(f"學生 1 的科目 A 是 {scores_4[0, 0]}")
print(f"學生 2 的科目 C 是 {scores_4[1, 2]}")
print(f"學生 4 的科目 B 是 {scores_4[3, 1]}")