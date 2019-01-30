data = []
count = 0 
with open('reviews.txt','r')as f:
	for line in f: 
		data.append(line)
		count += 1
		if count % 1000 == 0: #除1000等於零
			print(len(data))
print('讀取完畢',len(data),'筆資料')	

sum_length = 0	
for d in data:
	sum_length += len(d)     
print('平均留言長度為',sum_length/len(data))

new = []
for d in data:#d是字串,data是清單
     if len(d)<100:
     	new.append(d)
print('一共有',len(new),'筆留言小於一百字') 
print(new[2])       