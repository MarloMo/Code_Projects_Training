def get_grade(s1, s2, s3):
    avg = sum([s1, s2, s3]) / 3
    if avg >= 90:
        return 'A'
    elif avg >= 80:
        return 'B'
    elif avg >= 70:
        return 'C'
    elif avg >= 60:
        return 'D'
    else:
        return 'F'


s1, s2, s3 = 90, 80, 70
print(get_grade(s1, s2, s3))
