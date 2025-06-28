"""
Dany jest ciąg liczb 𝑇 [0], …, 𝑇 [𝑛 − 1]. Mówimy, że dowolny jego podciąg jest 𝑘-spójny jeśli można
go stworzyć poprzez wybranie pewnego zakresu elementów 𝑇 [𝑖], 𝑇 [𝑖 + 1], 𝑇 [𝑖 + 2], …, 𝑇 [𝑗], a
następnie usunięciu spośród nich co najwyżej 𝑘 elementów.
Na przykład jeśli mamy ciąg 3, 1, −2, 7, 5, 10, −8, 4 to 1, 5, 10 jest jego 2-spójnym podciągiem: Można go stworzyć wybierając elementy 1, −2, 7, 5, 10 a następnie usuwając −2 i 7.
Proszę zaimplementować funkcję kstrong( T, k ), która otrzymuje na wejściu ciąg 𝑇 i zwraca
maksymalną sumę 𝑘-spójnego podciągu 𝑇 . Funkcja powinna być jak najszybsza.
"""

from egz1btesty import runtests
import heapq as hq

def kstrong( T, k):
	# Init:
	n = len(T)
	pq = []
	S = -float("inf")
	current_sum = 0

	# Main loop:
	for left in range(n):
		pq = []
		S = max(S, current_sum)
		current_sum = 0

		for right in range(left, n):
			num = T[right]
			S = max(S, current_sum)
			if(num >= 0):
				current_sum += num
				continue

			if(len(pq) < k): # we can just dump negative element
				hq.heappush(pq, -num)
				continue

			if(num > -pq[0]): # It is better to just include the number in the sum
				current_sum += num
			else: # Or we can decide do get the biggest negative number from queue and skip current item
				current_sum += -hq.heappop(pq)
				hq.heappush(pq, -num)

	S = max(S, current_sum)
	return S

runtests( kstrong, all_tests = True )
