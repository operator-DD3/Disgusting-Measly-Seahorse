p256 = 115792089237316195423570985008687907853269984665640564039457584007913129639747
p = 2**129 - 25 #(680564733841876926926749214863536422887)

INT_BITS = 256
  
def rol(n, d): 
    return (n << d)|(n >> (INT_BITS - d)) 
  
def ror(n, d): 
    return (n >> d)|(n << (INT_BITS - d)) & 2**INT_BITS-1 #0xFFFFFFFF

def pad(input, size):
    output = ""
    for i in range(size - len(input) - 1):
        output = "0" + output
    return output + input

def poly12925(input):
    input = hex(p256) + input
    hash = p256
    a=0
    for i in range(len(input)):
        char = ord(input[i:i+1])
        a = char ** (len(input)+i)
        hash = (hash * p + a + char) % 2**256
        hash = rol(hash, (char%INT_BITS))
    hash = hex((hash ^ ror(hash,64)) % 2**128)
    return pad(hash[3:len(hash)],32)

print(poly12925("a"))
print(poly12925("b"))
print(poly12925("ab"))
print(poly12925("ac"))
print(poly12925("abc"))
print(poly12925("abd"))
print(poly12925("abcd"))
print(poly12925("abce"))
print()
print(poly12925("Hello World!"))
print(poly12925("Hello World?"))
print(poly12925("hello World!"))
print(poly12925(""))
