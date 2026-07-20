from main_scores import get_avg_score

def test_get_avg_score(test_scores: list, expected) -> bool:
    actual = get_avg_score(test_scores)
    # expected = 80.0

    print(f"預期平均: {expected}")
    print(f"實際平均: {actual}")

    if expected == actual:
        print("成功")
        return True

    print("失敗")
    return False

def test1():
    # 測試流程 1
    test_scores = [
        {"姓名": "a", "分數": 90},
        {"姓名": "b", "分數": 80},
        {"姓名": "c", "分數": 70},
    ]
    result1 = test_get_avg_score(test_scores, 80.0)

    test_scores2 = [
        {"姓名": "a", "分數": 100},
        {"姓名": "b", "分數": 90},
        {"姓名": "c", "分數": 80},
    ]
    result2 = test_get_avg_score(test_scores2, 90.0)

    if result1 and result2:
        print("測試全部通過")
    else:
        print("測試失敗")

test1()