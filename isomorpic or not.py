def is_isomorphic(s,t):
    key1={}
    for i in range(len(s)):
        c1,c2=s[i],t[i]

        if c1 in key1 and key1[c1]!=c2:
            return False
        elif len(s)!=len(t):
            return False
        else:
            key1[c1]=c2
    return True
print(is_isomorphic("egg", "add"))  
print(is_isomorphic("foo", "bar"))  
print(is_isomorphic("paper", "title"))  
print(is_isomorphic("fry", "sky"))  
print(is_isomorphic("apples", "apple"))  
