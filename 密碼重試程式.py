# 密碼重試程式
# password = "a123"
# 使用者重複輸入密碼，最多3次
# 若正確，印"登入成功"
# 若不正確，印"密碼錯誤，還有_次機會"

pwd = "a123"
ipt_num = 3
while True:
	ipt_pwd = input("請輸入密碼:")

	if ipt_pwd == pwd :
		print("密碼正確")
		break
	else :
		print("密碼不正確，還有",ipt_num,"次")
		ipt_num = ipt_num -1
		if ipt_num < 0 :
			ipt_num = 3
			print("密碼已輸入超過3次錯誤")
			break

