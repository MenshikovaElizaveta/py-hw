from Huffman import ecode, decode

def test_mixed_characters():
    with open('Hello.txt', 'r') as f:
        t = f.read()
    assert t == decode(*ecode(t))

def test__grouped_repetitions():
    with open('abc.txt', 'r') as f:
        t = f.read().strip()
    assert t == decode(*ecode(t))

def test_single_char():
    with open('a.txt', 'r') as f:
        t = f.read().strip()
    assert t == decode(*ecode(t))