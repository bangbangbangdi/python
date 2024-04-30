py_score = input('请输入你的python课程成绩：')
c_score = input('请输入你的C课程成绩：')

if py_score.isdigit() and c_score.isdigit():
    py_score = int(py_score)
    c_score = int(c_score)
    if py_score>=60 or c_score>=60:
        print('合格')
    else:
        print('重修')
else:
    if not py_score.isdigit():
        print('py的成绩必须输入数字！')
    if not c_score.isdigit():
        print('c的成绩必须输入数字！')