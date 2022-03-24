import random
import time

# 단어 리스트
w = ["cat", "dog", "fox", "monkey", "mouse", "panda", "frog", "snake", "wolf", "java"]
n = 1
print("[타자 게임] 준비되면 Enter!")
input()    # 문제 번호
start = time.time()     # 시작 시간을 기록

q = random.choice(w)    # 단어 리스트에서 요소를 랜덤하게 뽑는다.
while n <=5:
	print("*문제", n)
	print(q)
	x = input()
	if q == x:
		print("통과!")
		n = n + 1
		q = random.choice(w)
	else:
		print("오타! 다시 도전!")

end = time.time()
et = end - start
et = format(et, ".2f")
print("타자 시간 : ", et, "초")
