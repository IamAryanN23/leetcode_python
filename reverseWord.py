def reverseWords(s: str) -> str:
    ls = s.split()
    ls.reverse()
    return ' '.join(ls)


print (reverseWords("This is Hello world"))