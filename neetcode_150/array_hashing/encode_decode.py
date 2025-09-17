def encoder(strs):
    encode = ""
    for st in strs:
        encode = encode + str(len(st)) + "#" + st
    return encode

def decode(strs):
    decoded = []
    i = 0
    while i < len(strs):
        j = strs.index("#", i)
        length = int(strs[i:j])
        i = j + 1
        decoded.append(strs[i:i+length])
        i += length
    return decoded
    


strs = ["I", "love", "neetcode"]
cod = "1#I4#love8#neetcode"
print(encoder(strs))
print(decode(cod))

