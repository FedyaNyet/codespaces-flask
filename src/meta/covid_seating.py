from typing import List
import math
# Write any import statements here

def getMaxAdditionalDinersCount(N: int, K: int, M: int, S: List[int]) -> int:
    # Write your code here
    ## This function Mutates the list S, by sorting it.
    assert(M == len(S))

    S.sort()

    if not len(S):
        return seats_available_between(-K, N+K+1, K)

    available_seats = 0
    available_seats += seats_available_between(-K, S[0], K)
    for idx, _ in enumerate(S):
        if idx < len(S)-1:
            available_seats += seats_available_between(S[idx], S[idx+1], K)
            
    available_seats += seats_available_between(S[-1], N+K+1, K)

    return available_seats


def seats_available_between(start, end, buffer):
    spaces_between =  (end - start) - 1
    ret = max([0, math.floor( (spaces_between - buffer) / (buffer +1 ) )])
    return ret
