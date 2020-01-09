#random_test
import random

start = input("請輸入開始範圍")
start = int(start)

end = input("請輸入結束範圍")
end = int(end)

count_num = 1; #紀錄PC找多久

rand_num = random.randint(start,end)

search_num = int((end+start)/2) #預設電腦的初始值

while True:
	if(search_num == rand_num) :
		print("找到囉，答案為",search_num)
		print("目前為第",count_num,"次")
		break
	elif(search_num > rand_num):
		print(search_num,"比目標值大")
		end = search_num #重新設定終點
		search_num = int((end+start)/2) #範圍縮小到start~search_num之間	
	else:
		print(search_num,"比目標值小")
		start = search_num #重新設定起點
		search_num = int((end+start)/2) #範圍縮小到search_num~end之間
		
		
	print("目前為第",count_num,"次")
	count_num = count_num+1
	#print("亂數值為",rand_num)
