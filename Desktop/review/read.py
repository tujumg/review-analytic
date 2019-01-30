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