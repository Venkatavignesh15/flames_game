import streamlit as st 
a=list(st.text_input("Enter a name:").lower())
b=list(st.text_input("Enter another name:").lower())
for i in a.copy():
    if i in b:
        a.remove(i)
        b.remove(i)
count=len(a)+len(b)
s="flames"
while len(s)!=1:
    split=count%len(s)-1
    if split==-1:
        s=s[:len(s)-1]
    else:
        s=s[split+1:]+s[:split]
result={"f":"friends","l":"love","a":"affection","m":"marriage","e":"enemy","s":"siblings"}
if (st.button("check")):
    st.success(result[s])

