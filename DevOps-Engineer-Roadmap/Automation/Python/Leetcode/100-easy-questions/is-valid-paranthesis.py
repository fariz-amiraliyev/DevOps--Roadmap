def valid(s):
    st=[]
    for x in range(len(s)):
        if s[x] == "(" or s[x] =="{" or s[x] =="[":
            st.append(x)
        elif len(st) <=0:
            return False
        else:
            lx=st.pop()
            if s[x] == ")" and s[lx]!="(":
                return False
            if s[x] == "]" and s[lx]!="[":
                return False
            if s[x] == "}" and s[lx]!="{":
                return False
        if len(st)==0:
            return True
    return False


#example case:
 s = "()[]{}"
s
valid(s)
True
