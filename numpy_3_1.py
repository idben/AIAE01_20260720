import numpy as np

students = ["小安", "小美", "小華", "小杰"]
subjects = ["國文", "英文", "數學"]

scores = np.array([
    [80, 90, 75],
    [88, 76, 92],
    [60, 85, 70],
    [95, 91, 89],
])

print(scores)
print(scores.shape)
print(scores.dtype)
print("-"*30)

# axis=1 以列做為計算單位, 以學生為單位, 算出個人平均分數
st_avgs = scores.mean(axis=1)
print(st_avgs)
for index, student in enumerate(students):
    # .round(1) 用四捨五入取到小數點下一位
    # print(f"{student} 的平均分數是 {st_avgs[index].round(1)}")
    # .1f 是目前內容顯示到小數點下一位
    # .1f 只能套用在單一數字上
    print(f"{student} 的平均分數是 {st_avgs[index]:.1f}")
