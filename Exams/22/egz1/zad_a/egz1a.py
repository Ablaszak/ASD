from egz1atesty import runtests

def snow( S ):
    d = 0
    w = 0
    S.sort(reverse = True)
    while(S[d] - d > 0):
        w += S[d] - d
        d += 1
    return w

runtests( snow, all_tests = False )
