def eh_palindromo(s):
    s = s.replace(" ", "").lower()
    return s == s[::-1]

if eh_palindromo(palavra):
    print(palavra, "é um palíndromo")
else:
    print(palavra ("\nnão é um palíndromo")