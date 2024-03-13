print('成绩分级')

a=input('请输入你的成绩:')
a= int(a)
if a<60 and a>=0 :
	print('D（不及格）')
elif a>=60 and a<70 :
	print('C（中等）')
elif a>=70 and a<80:
	print('B（良好）')
elif a>=80 and a<90:
	print('A（优秀）')
elif a>=90 and a<=100:
	print('A+（完美，你真是太棒啦）')
else:
	print('无效输入，请输入0-100内数字')
