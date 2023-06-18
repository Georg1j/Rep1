'''def strcounter(s): # O(M*N)
    for sym in set(s):
        counter = 0
        for sub_sym in s:
            if sub_sym == sym:
                    counter += 1
        print(sym, counter)

strcounter('abcaa')

def strcounter(s): # O(N**2)
    for sym in s:
        counter = 0
        for sub_sym in s:
            if sub_sym == sym:
                    counter += 1
        print(sym, counter)

strcounter('abcaa')'''

def strcounter(s): # O(N)
    syms_counter = {}
    for sym in s:
        syms_counter[sym] = syms_counter.get(sym, 0) + 1
    for sym, count in syms_counter.items():
        print(sym, count)



strcounter('aaaaaadddddfggg')