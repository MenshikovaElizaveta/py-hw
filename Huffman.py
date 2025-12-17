from collections import Counter
import heapq


def ecode(msg: str) -> tuple[str, dict[str, str]]:
    if not msg:
        return ("", {})
    
    freq = Counter(msg)
    heap = [[wt, [symbol, ""]] for symbol, wt in freq.items()]

    if len(heap) == 1:
        heap[0][1][1] = "0"
        alphabet = {heap[0][1][0]: "0"}
        ciphertext = "0" * heap[0][0]
        return ciphertext, alphabet
    
    while len(heap) > 1:
        lo = heapq.heappop(heap)
        hi = heapq.heappop(heap)

        for pair in lo[1:]:
            pair[1] = "0" + pair[1]

        for pair in hi[1:]:
            pair[1] = "1" + pair[1]

        heapq.heappush(heap, [lo[0] + hi[0]] + lo[1:] + hi[1:])

    alphabet = dict(heap[0][1:])
    ciphertext = "".join(alphabet[char] for char in msg)

    return (ciphertext, alphabet)


def decode(encoded: str, table: dict[str, str]) -> str:
    rev_table = {code: symbol for symbol, code in table.items()}
    decoded_msg = ""
    current_code = ""

    for bit in encoded:
        current_code += bit
        if current_code in rev_table:
            decoded_msg += rev_table[current_code]
            current_code = ""

    return decoded_msg