
def xgcd(a, b):
    x0, y0, x1, y1 = 1, 0, 0, 1
    while b != 0:
        q, a, b = a // b, b, a % b
        x0, x1 = x1, x0 - q * x1
        y0, y1 = y1, y0 - q * y1
    return a, x0, y0

def modinv(a, m):
    g, x, y = xgcd(a, m)
    if g != 1:
        return 0
    else:
        return x % m

def phi(x1, y1, x2, y2, p, a, b):
    if x1 == x2 and y1 == y2:
        return ((3 * x1 * x1 + a) * modinv(2 * y1, p)) % p
    else:
        return ((y2 - y1) * modinv(x2 - x1, p)) % p

def psi(x1, y1, x2, y2, p, a, b):
    if x1 == x2 and y1 == y2:
        return ((-3 * (x1 ** 3) - a * x1 + 2 * y1 * y1) * modinv(2 * y1, p)) %p
    else:
        return ((y1 * x2 - y2 * x1) * modinv(x2 - x1, p)) % p

def ecc_add(x1, y1, x2, y2, p, a, b):
    if x1 == -1 and y1 == -1:
        return [x2, y2]
    elif x2 == -1 and y2 == -1:
        return [x1, y1]
    elif x1 == x2 and y1 == -y2 % p:
        return [-1,-1]
    else:
        x = (phi(x1, y1, x2, y2, p, a, b) ** 2 - x1 - x2) % p
        y = (-phi(x1, y1, x2, y2, p, a, b) * x - psi(x1, y1, x2, y2, p, a, b)) % p
        return [x, y]

def ecc_add_n(g, c, n, p, a, b):
    for i in range(n):
        c = ecc_add(c[0],c[1],g[0],g[1],p,a,b)
    return c

def ecc_generate_group(g, p, a, b):
    c = g
    for i in range(40):
        x = c[0]
        y = c[1]        
        index = str(i)
        fx = str((x**3 + a*x + b) % p)
        fy = str((y**2) % p)
        print (index + ': ' + str(c) +' ' + fx + ' ' + fy)
        if c == [-1,-1]:
            break
        c = ecc_add(c[0],c[1],g[0],g[1],p,a,b)


p=29; a=1; b=7
# y^2 = x^3 + ax + b
g = [1,3]
c = [9,7]

print(ecc_add_n(g,c, 20, p,a,b))
#ecc_generate_group(g,p,a,b)