# BMI計算程式
weight = input('你的體重是?(kg)')
weight = float(weight)
high = input('你的身高是?(cm)')
high = float(high)
BMI = weight / (high * high / 10000)
BMI = float(BMI)
if BMI < 18.5:
    print('體重過輕', BMI)
elif BMI >= 18.5 and BMI < 24:
    print('正常範圍', BMI)
elif BMI >= 24 and BMI < 27:
    print('過重', BMI)
elif BMI >= 27 and BMI < 30:
    print('輕度肥胖', BMI)
elif BMI >= 30 and BMI < 35:
	print('中度肥胖', BMI)
else:
    print('重度肥胖', BMI)
if BMI >= 24:
	print('異常範圍')
