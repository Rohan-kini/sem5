def add_bin(a, b):
    c = len(a)
    carry = '0'
    res = ''
    for i in range(c-1, -1, -1):
        if(a[i]=='1' and b[i]=='1' and carry=='1'):
            res = '1'+res
            carry = '1' 
        elif((a[i]=='1' and b[i]=='1' and carry=='0')or(a[i]=='1' and b[i]=='0' and carry=='1')or(a[i]=='0' and b[i]=='1' and carry=='1')):
            res = '0'+res
            carry = '1'
        elif((a[i]=='1' and b[i]=='0' and carry=='0')or(a[i]=='0' and b[i]=='1' and carry=='0')or(a[i]=='0' and b[i]=='0' and carry=='1')):
            res = '1'+res
            carry = '0'
        else:
            res = '0'+res
            carry = '0'
    
    return res
        

def two_comp(a):
    c = len(a)
    res =''
    for i in range(c):
        if(a[i] == '0'):
            res = res + '1'
        else:
            res = res + '0'
    one = '0'*(c-1)+'1'
    res = add_bin(res, one)
    return res


def right_shift(A, Q):
    q0  = Q[-1]  ##q0 mei Q ka last bhej diya chalu hogya hai shifting
    c = len(Q)
    q, a = Q[:c-1], A[:c-1]  ##q,a mei first four bits rakhe khali isliye c-1 tak liya kyuki A ka last digit agle mei jayega aur Q ka toh bhe diya hai agle mei
    q = A[-1]+q  ##bass A ka last aur bacha hua q ka chaar 
    a = A[0]+a ##a ka chaar plus freeze kiya hua..
    return a[:c], q[:c], q0


def print_iter(a, q, q0):
    print(f'Accumulator: {a}')
    print(f'MUltipier: {q}')
    print(f'Storing bit: {q0}', end='\n\n')



##start of code.......

a = int(input('Enter Multiplicand : '))
b = int(input('Enter Multiplier : '))

M, Q = bin(abs(a))[2:], bin(abs(b))[2:]

count = max(len(M), len(Q))   ##bass kaunsa jyada bada hai usko count assign kar denge..


M = M.zfill(count+1)  ##zfill matlab bhar diya bas zeros se dono same bits hone k liye...
Q = Q.zfill(count+1)

if(a <0):
    M = two_comp(M)  ##negative hai toh pehle hi 2's leke rakho

if(b < 0):
    Q = two_comp(Q)  ##negative hai toh 2's leke rakho


M_neg = two_comp(M) ##A-M ya A+M k liye lagta hi hai bhai neg M so karlo...

print(f'Multiplier: {M}\nMultiplicand: {Q}\n -Multiplier: {M_neg}', end='\n\n')


A = '0'*(count+1) ##accum mei zeros bhar diya ...

Q0 = '0'
print_iter(A, Q, Q0) ##bass a,q,q0 bhej diya print iter fn mei

for i in range(count+1):
    print(f'Iteration {i} :')
    if(Q[-1] == '0' and Q0 == '1'):  ##check kar rhe hai ek ek karke condition 01 if mei
        A = add_bin(A, M)
        A, Q, Q0 = right_shift(A, Q)

    elif(Q[-1]=='1' and Q0 == '0'): ##10 elif meim
        A = add_bin(A, M_neg)
        A, Q, Q0 = right_shift(A, Q)

    else: ##11 ya 00 hua toh else mei 
        A, Q, Q0 = right_shift(A, Q)

    print_iter(A, Q, Q0)



##khel ho chuka sab upar now result time ...
res = A+Q
print(f'The decimal answer is: {res}')
bool_check = (((a>0)and(b<0)) or ((a<0)and(b>0)))
if bool_check: # for negative number as output
    res= two_comp(res)
    ans = int(res,2)
    print(f'The result is: -{ans}')
else:
    ans = int(res,2)
    print(f'The result is: {ans}')