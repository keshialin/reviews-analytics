import time
import progressbar

data = []
count = 0
bar = progressbar.ProgressBar(max_value = 1000000)
with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(line)
		count += 1
		bar.update(count)
print('檔案讀取完了，總共有{}筆資料'.format(len(data)))

print(data[0])

sum_len = 0
for d in data:
	sum_len += len(d)
print('留言平均長度為{}'.format(sum_len/len(data)))

new = []
for d in data:
	if len(d) < 100:
		new.append(d)
#new = [d for d in data if len(d) < 100]
print('一共有{}留言長度小於100'.format(len(new)))
print(new[0])


good = []
for d in data:
	if 'good' in d:
		good.append(d)
print('一共有{}筆留言提到good'.format(len(good)))
print(good[0])

#文字計數
start_time = time.time()
wc = {} # word_count
for d in data:
	words = d.split()
	for word in words:
		if word in wc:
			wc[word] += 1
		else:
			wc[word] = 1 #新增新的key進字典
	
for word in wc:
	if wc[word] > 1000000:
		print(word, wc[word])
end_time = time.time()
print('花了{}秒'.format(end_time - start_time))

while True:
	word = input('請問你想查什麼字/[q]quit:')
	if word == 'q':
		break
	if word in wc:
		print('word出現過的次數為{}'.format(wc[word]))
	else: 
		print('這個字沒有出現過喔！')

print('感謝使用本查詢功能')

