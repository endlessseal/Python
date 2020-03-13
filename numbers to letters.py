import sys

ONES=[
    "",         "one",      "two",      "three",        "four", 
    "five",     "six",      "seven",    "eight",        "nine",
    "ten",      "eleven",   "twelve",   "thirteen",     "fourteen",
    "fifteen",  "sixteen",  "seventeen","eighteen",     "nineteen",
]
TENS=[
    "zero",     "ten",      "twenty",   "thirty",       "forty",
    "fifty",    "sixty",    "seventy",  "eighty",       "ninety",
]

def to_s_h(i):
    if(i<20):
        return(ONES[i])
    return(TENS[i/10] + ONES[i%10]) 

def to_s_t(i):
    if(i<100):
        return(to_s_h(i))
    return(ONES[i/100] + "hundred" + to_s_h(i%100))

def to_s_m(i):
    if(i<1000):
        return(to_s_t(i))
    return(to_s_t(i/1000) + "thousand" + to_s_t(i%1000))

def to_s_b(i):
    if(i<1000000):
        return(to_s_m(i))
    return(to_s_m(i/1000000) + "million" + to_s_m(i%1000000))


def try_string(s,t):
    global letters_to_go,word_sum
    l=len(s)
    letters_to_go -= l
    word_sum += t
    if(letters_to_go == 0):
        print "solved: " + s
        print "sum is: " + str(word_sum)
        sys.exit(0)
    elif(letters_to_go < 0):
        print "failed: " + s + " " + str(letters_to_go)
        sys.exit(-1)

def solve(depth,prefix,prefix_num):
    global millions,thousands,ones,letters_to_go,onelen,thousandlen,word_sum
    src=[ millions,thousands,ones ][depth]
    for x in src:
        num=prefix + x[2]
        nn=prefix_num+x[1]
        try_string(num,nn)
        if(x[0] == 0):
            continue
        if(x[0] == 1):
            stl=(len(num) * 999) + onelen
            ss=(nn*999) + onesum
        else:
            stl=(len(num) * 999999) + thousandlen + onelen*999
            ss=(nn*999999) + thousandsum
        if(stl < letters_to_go):
            letters_to_go -= stl
            word_sum += ss
        else:
            solve(depth+1,num,nn)


ones=[]
thousands=[]
millions=[]
onelen=0
thousandlen=0
onesum=(999*1000)/2
thousandsum=(999999*1000000)/2



for x in range(1,1000):
    s=to_s_b(x)
    l=len(s)
    ones.append( (0,x,s) )
    onelen += l
    thousands.append( (0,x,s) )
    thousands.append( (1,x*1000,s + "thousand") )
    thousandlen += l + (l+len("thousand"))*1000
    millions.append( (0,x,s) )
    millions.append( (1,x*1000,s + "thousand") )
    millions.append( (2,x*1000000,s + "million") )
print(len(millions))
ones.sort(key=lambda x: x[2])
thousands.sort(key=lambda x: x[2])
millions.sort(key=lambda x: x[2])

letters_to_go=51000000000
word_sum=0

solve(0,"",0)