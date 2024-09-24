def P(S: str, k: int) -> list[str]:
    if k == len(S):
        return [S]
    else:
        out = []
        for i in range(0, len(S)-1):
            T = S
            T[k] == T[]