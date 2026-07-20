import numpy as np

students = ["小安", "小美", "小華", "小杰"]
subjects = ["國文", "英文", "數學"]

scores = np.array([
    [80, 90, 58],
    [88, 76, 92],
    [50, 85, 59],
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
print("-"*30)

# axis=0 以欄(學科)做為計算單位
subj_avgs = scores.mean(axis=0)
print(subj_avgs)
for index, subject in enumerate(subjects):
    print(f"{subject} 的平均分數是 {subj_avgs[index]:.1f}")
print("-"*30)

# 整張表的最高最低
print(f"所有人所有學科的最高分: {scores.max()}")
print(f"所有人所有學科的最低分: {scores.min()}")

faild_mask = scores < 60
passed_mask = scores >= 60
faild_scores = scores[faild_mask]
passed_scores = scores[passed_mask]
print(faild_scores)
print(passed_scores)
# pyhton 的容器通常用 len()
# NumPy 陣列元素總數通常用 .size
print(f"被當掉的人數: {faild_scores.size}")
print(f"通過的人數: {passed_scores.size}")


