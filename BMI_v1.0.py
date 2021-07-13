# BMI計算程式
weight = input('你的體重是?(kg)')
height = input('你的身高是?(cm)')
weight = float(weight)
height = float(height)
height = height / 100
BMI = weight / height / height
if BMI < 18.5:
    print('你的BMI是:', BMI, '體重過輕')
elif BMI >= 18.5 and BMI < 24:
    print('你的BMI是:', BMI, '正常範圍')
elif BMI >= 24 and BMI < 27:
    print('你的BMI是:', BMI, '過重')
elif BMI >= 27 and BMI < 30:
    print('你的BMI是:', BMI, '輕度肥胖')
elif BMI >= 30 and BMI < 35:
	print('你的BMI是:', BMI, '中度肥胖')
else:
    print('重度肥胖')
if BMI >= 24:
	print('異常範圍')
