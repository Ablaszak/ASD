"""
Pewien układ elektryczny ma 2𝑛 wejść ponumerowanych od 0 do 2𝑛 − 1. Wejścia należy połączyć
przewodami. Do każdego wejścia powinien dochodzić jeden przewód i każdy przewód łączy
dokładnie dwa wejścia. Oznacza to, że należy użyć w sumie 𝑛 przewodów. Zasada działania układu
wymaga, żeby przewody nie krzyżowały się, czyli jeśli połączymy przewodami wejście 𝑖 oraz wejście
𝑗 (gdzie 𝑖 < 𝑗), to żadne z wejść od 𝑖 + 1 do 𝑗 − 1 nie może być połączone z żadnym z wejść od
0 do 𝑖 − 1 ani z żadnym z wejść od 𝑗 + 1 do 2𝑛 − 1. Dodatkowo dana jest tablica 𝑇 , gdzie 𝑇 [𝑖]
to parametr mocy 𝑖-go wejścia. Kabel, który bezpiecznie łączy wejście 𝑖 z wejściem 𝑗 kosztuje 1 +
|𝑇 [𝑖] − 𝑇 [𝑗]|.
Proszę zaimplementować funkcję wired(T), która otrzymuje na wejściu listę 𝑇 z parametrami mocy
wejść, a zwraca minimalny koszt przewodów pozwalających na ich połączenie zgodnie z zasadami
"""

from egz2atesty import runtests

single = [[]]
summary = [[]]

def cost(T, l, r): # calculates minimal summary cost of all connections between l and sth <= r
	global single
	global summary

	if(l >= r): # safety feature
		return 0

	if(r-l == 1): # end recursion
		summary[l][r] = single[l][r]
		return single[l][r]

	if(summary[l][r]is not None): # should not happen tho
		return summary[l][r]

	w = float("inf")
	mid = l+1
	while(mid < r):
		current = 0
		# get left to mid
		if(summary[l][mid] is not None):
			current += summary[l][mid]
		else:
			summary[l][mid] = cost(T, l, mid)
			current += summary[l][mid]
		# get mid+1 to right:
		if(mid < r):
			if(summary[mid+1][r] is not None):
				current += summary[mid+1][r]
			else:
				summary[mid+1][r] = cost(T, mid+1, r)
				current += summary[mid+1][r]
		w = min(w, current)

		mid += 2

	# Remember to try connecting l directly to r
	w = min(w, single[l][r] + cost(T, l+1, r-1))
	summary[l][r] = w
	return w

def wired( T ):
	n = len(T)
	global single
	global summary
	# get cost of single connection between ports:
	single = [[None for _ in range(n)] for _ in range(n)]
	for r in range(n):
		for c in range(n):
			single[r][c] = abs(T[r]-T[c])

	summary = [[None for _ in range(n)] for _ in range(n)]
	for mid in range(1, n, 2):
		summary[0][mid] = cost(T, 0, mid)

	return cost(T, 0, n-1) + n//2

runtests( wired, all_tests = True )
