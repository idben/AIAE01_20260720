# 找出最高分
def get_top_student(students_data: list) -> dict:
    top_student = students_data[0]

    for student in students_data:
        if student["分數"] > top_student["分數"]:
            top_student = student
    
    return top_student

# 算出平均分數
def get_avg_score(students_data: list) -> float:
    total = 0

    for st in students_data:
        total += st["分數"]
    
    return total/len(students_data)

# 找出分數低於 80 的學生
def get_lower_score_students(students_data: list, score_limit: int) -> list:
    results = []

    for st in students_data:
        if st["分數"] < score_limit:
            results.append(st)

    return results

# 練習 3 函式回傳及格人數
# get_pass_count

def main():
    students = [
        {"姓名": "小安", "分數": 92},
        {"姓名": "小美", "分數": 85},
        {"姓名": "小華", "分數": 76},
        {"姓名": "小杰", "分數": 60},
        {"姓名": "小琳", "分數": 98},
        {"姓名": "小宇", "分數": 88},
    ]
    lower_score = 70

    avg_score = get_avg_score(students)
    print(f"平均分數是 {avg_score}")
    top_student = get_top_student(students)
    print(f"最高分的學生是 {top_student["姓名"]}，分數是 {top_student["分數"]}")
    lower_score_students = get_lower_score_students(students, lower_score)
    print(f"低於 {lower_score} 分的學生是: \n{lower_score_students}")

if __name__ == "__main__":
    main()