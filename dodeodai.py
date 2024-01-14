import sys
sys.set_int_max_str_digits(0) #đặt lại giới hạn string

# Chia để trị xử lý lũy thừa lớn
def luythua(n,s):
    if s==1:
        return n
    elif s%2==0:
        return (luythua(n,s//2)**2)%(10**9+7)
    else: return (luythua(n,s//2)**2*n)%(10**9+7)


def solution(a,u,k):
    #Lập mảng quy hoạch động
    for i in range(1,len(a)):
        a[i]*=a[i-1]
    #Dùng vòng lặp để chạy qua tất cả Truy vấn
    res=[]
    for i in range(len(u)):
        if u[i]==1 and k[i]!=1: res.append((a[u[i]+k[i]-2])%(10**9+7))
        elif k[i]==1 and u[i]==1: res.append((a[0])%(10**9+7))
        elif k[i]==1 and u[i]!=1: res.append((a[u[i]+k[i]-2]*luythua(a[u[i]+k[i]-3],10**9+5))%(10**9+7))
        else: res.append((a[u[i]+k[i]-2]*luythua(a[u[i]-2],10**9+5))%(10**9+7))
    return res

#đọc file và ghi ra file

with open('dodeodai.inp', mode='r') as file_in:
    file_input=file_in.read().split('\n')
    a = list(map(int, file_input[1].split()))
    u = [int(file_input[i].split()[0]) for i in range(3,len(file_input))]
    k = [int(file_input[i].split()[1]) for i in range(3, len(file_input))]
with open('dodeodai.out', mode='w') as file_out:
    file_out.write('\n'.join(list(map(str,solution(a,u,k)))))
