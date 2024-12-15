v1=["hihi","what is code","what is vscode","zed","what is a train"]
r=0
i=[]
t=56
str_2="what is  v coee"
def main(str_):
    str_1=str_
    global a






    a=0

    s1=str_1.replace(" ",'')
    s2=str_2.replace(" ",'')



    for x in range(len(s1)):
        if len(s1) >len(s2):

            s2=s2+"_"

        if len(s1) <len(s2):

            s1=s1+"_"



        if s1[x] in s2[x] :

            a=a+1



    return round(a/len(s1)*100)



for n in range(len(v1)):
    c=main(v1[n])
    print(c)
    if c>t:

        print(v1[n])
        r=r+1
        i.append(v1[n])

# print(r)
if r >1 and r<3:
    print(f"did you mean -> '{i[0]}' or '{i[1]}'")