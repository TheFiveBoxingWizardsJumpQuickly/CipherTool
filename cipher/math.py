from .prime_number import primes

def make_primenumber():
    f = open('prime_number.py', 'w')
    txt = 'primes =['

    limit = 1000000
    max = int(limit**0.5)
    seachList = [i for i in range(2,limit+1)]
    primeNum = []
    while seachList[0] <= max:
        primeNum.append(seachList[0])
        tmp = seachList[0]
        seachList = [i for i in seachList if i % tmp != 0]
    primeNum.extend(seachList)
    
    txt += ','.join(map(str, primeNum))

    txt+=']'
    f.write(txt)
    f.close


def calc(n):
    f = ''
    factor_exp_list = []
    p_max = primes[len(primes)-1]

    if n < 0:
        f = '-1 * '
        n *= -1
    
    for i in range(len(primes)):
        p = primes[i]

        if p**2 > n:
            factor_exp_list.append([ n , 1 ])
            break

        k = 0
        while n % p == 0:
            k += 1
            n //= p

        if k > 0:
            factor_exp_list.append([ p , k ])

        if n == 1:
            break
        
        if p == p_max:
            factor_exp_list.append([ n , 1 ])
            break

    notation = ''
    if n > p_max ** 2:
        notation = '\n #' + str(n) + ' might have a factor lager than ' + str(p_max)
    elif len(factor_exp_list) == 1 and factor_exp_list[0][1] == 1 and f == '':
        notation = ' (prime)'

    for i in range(len(factor_exp_list)):
        if i > 0:
            f += ' * '

        if factor_exp_list[i][1] == 1:
            f += str(factor_exp_list[i][0])
        else:
            f += str(factor_exp_list[i][0]) + '^' + str(factor_exp_list[i][1])

    f += notation

    return f

def factorize (num):
    n = int(num)
    if n == 0:
        return '0 = 0'
    elif n == 1:
        return '1 = 1'
    elif n == -1:
        return '-1 = -1'
    else:
        return str(n) + ' = ' + calc(n)
      
# Debug
'''
if __name__ ==  '__main__':
    #make_primenumber()
    print( factorize('2'))
'''

