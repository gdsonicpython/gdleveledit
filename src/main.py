import zlib, base64, gzip

def importlevel(s:str):
    return [s, "leveldata"]

def exportlevel(l:list):
    if l[1] != "leveldata":
        raise f"{l[1]} is not the valid type"
    if type(l[0]) != type("hello"):
        raise f"{type(l[0])} is not the correct type"
    return l[0]

def decodedata(l:list):
    if l[1] != "leveldata":
        raise f"{l[1]} is not the valid type"
    if type(l[0]) != type("hello"):
        raise f"{type(l[0])} is not the correct type"
    base64_decoded = base64.urlsafe_b64decode(l[0].encode())
    decompressed = zlib.decompress(base64_decoded, 15 | 32)
    s = [decompressed.decode(), "levelstring"]
    return s

def encodedata(l:list):
    if l[1] != "levelstring":
        raise f"{l[1]} is not the valid type"
    if type(l[0]) != type("hello"):
        raise f"{type(l[0])} is not the correct type"
    gzipped = gzip.compress(l[0].encode())
    base64_encoded = base64.urlsafe_b64encode(gzipped)
    s = base64_encoded.decode()
    s = [s, "leveldata"]
    return s

def splitgdstring(l:list):
    if l[1] != "levelstring":
        raise f"{l[1]} is not the valid type"
    if type(l[0]) != type("hello"):
        raise f"{type(l[0])} is not the correct type"
    s = l[0].split("|")
    for i in range(len(s)):
        s[i] = s[i] + "|"
    e = s[len(s)-1].split(";")
    s[len(s)-1] = e[0] + ";"
    del e[0]
    for i in range(len(e)):
        e[i] = e[i] + ";"
    del e[len(e)-1]
    s.insert(len(s), e)
    s = [s, "levelstringlist"]
    return s

def joingdstring(l:list):
    if l[1] != "levelstringlist":
        raise f"{l[1]} is not the valid type"
    if type(l[0]) != type(["hi", "hello"]):
        raise f"{type(l[0])} is not the correct type"
    temp_s = ""
    for i in range(len(l[0][len(l[0])-1])):
        temp_s = temp_s + l[0][len(l[0])-1][i]
    l[0][len(l[0])-1] = temp_s
    s = ""
    for i in range(len(l[0])):
        s = s + l[0][i]
    s = [s, "levelstring"]
    return s

def splitdata(l:list):
    if l[1] != "levelstringlist":
        raise f"{l[1]} is not the valid type"
    if type(l[0]) != type(["hi", "hello"]):
        raise f"{type(l[0])} is not the correct type"
    s = l[0][len(l[0])-1]
    d = l[0]
    del d[len(l[0])-1]
    del s[len(s)-1]
    for i in range(len(s)):
        s[i] = s[i].split(",")
        for j in range(len(s[i])-1):
            s[i][j+1] = "," + s[i][j+1]
    s = [s, d, "levelobjects"]
    return s

def joindata(l:list):
    if l[2] != "levelobjects":
        raise f"{l[1]} is not the valid type"
    if type(l[0]) != type(["hi", "hello"]):
        raise f"{type(l[0])} is not the correct type"
    if type(l[1]) != type(["hi", "hello"]):
        raise f"{type(l[1])} is not the correct type"
    s = []
    for i in range(len(l[0])):
        temp_s = ""
        for j in range(len(l[0][i])):
            temp_s = temp_s + l[0][i][j]
        l[0][i] = temp_s
        s.append(temp_s)
    s = l[1] + [s]
    s = [s, "levelstringlist"]
    return s