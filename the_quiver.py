
import math
from fractions import Fraction as frac
import matplotlib.pyplot as graph

# SUM OF 1ST N NATURAL NUMBERS:

def sumN(x):
    #Using manual counter
    p = 0 # p is the dummy variable
    i = 0 # i is the counter
    while i <= x:
        p = p + i
        i = i + 1
    print("The sum of the first " + str(x) + " numbers is " + str(p))


# SUM OF 1ST N ODD NATURAL NUMBERS:

def OdsumN(x):
    a = 1 # a is the counter
    r = 0 
    while a < 2*x:
        r = r + a
        a += 2
    print("The sum of the first " + str(x) + " odd numbers is " + str(r))


# SUM OF 1ST N TERMS IN AN AP:

def sumAP(a,d,n):
    n = float(n)
    if n >= 1 and float(n)==int(n):
        n = int(n)    # Alotting specific data types
        a = float(a)
        d = float(d)
        c = 0 # c is the counter
        r = 0
        while c < n:
            r = r + a + c*d
            c += 1
        return r
    else:
        print("Please input valid numbers.")
        return None


# SUM OF 1ST N TERMS IN A GP:

def sumGP(a,r,n):
    n = float(n)
    if n >= 1 and float(n)==int(n):
        n = int(n)
        a = float(a)
        r = float(r)
        s = 0  # Stores sum
        for i in range(1,n+1):
            s = s + a
            a = a*r
        return s
    else:
        print("Please input valid numbers.")
        return None

# SUM OF 1ST N TERMS IN An hP:

def sumHP(a,d,n):
    n = float(n)
    if n >= 1 and float(n)==int(n):
        n = int(n)    # Alotting specific data types
        a = float(a)
        d = float(d)
        s = 0  # Stores sum
        for i in range(1,n+1):
            a = 1/a
            s = s + a
            a = 1/a
            a = a + d     
        return s
    else:
        print("Please input valid numbers.")
        return None


# FACTORIAL FUNCTION FOR NATURAL NUMBERS:

def fact(x):
    p = 1
    for i in range(1,x+1): # using Python's range function as in-built counter
        p = p*i
    return p

#### --- COMPLEX NUMBERS --- ####

class myComplex:

    def __init__(self,real,imaginary):
        self.x = real
        self.y = imaginary

    def disp(self):
        print(str(self.x)+" + "+"("+str(self.y)+")" + "i")

    def sum(self,a):
        r = self.x + a.x
        i = self.y + a.y
        return myComplex(r,i)

    def prod(self,a):
        r = self.x*a.x - self.y*a.y
        i = self.x*a.y + self.y*a.x
        return myComplex(r,i)
    
    def conjugate(self):
        self.y = -1*self.y

    def find_conjugate(self):
        r = self.x
        i = -self.y
        return myComplex(r,i)

    def modulus(self):
        mod = ((self.x)*(self.x) + (self.y)*(self.y))**(0.5)
        return mod
    
    def reciprocal(self):
        self.conjugate()
        p = self.modulus()
        self.x = self.x/(p**2)
        self.y = self.y/(p**2)
        return self

    def find_reciprocal(self):
        u = self.find_conjugate()
        p = self.modulus()
        i = u.x/p**2
        r = u.y/p**2
        return myComplex(i,r)
    
    def div(self,b):
        u = self.find_reciprocal()
        p = u.prod(b)
        p.reciprocal()
        return p

    def phase(self):
        print(math.atan(self.y/self.x),end=" ")
        print("i.e. tan inverse of "+ str(frac(self.x,self.y)))


#### --- MATRICES --- ####

# READING A TXT FILE INTO A LIST

def readtxt(file):
    f = open(file,'r')
    lst = []

    for line in f.readlines():
        lst.append([ float(val) for val in line.split(',') ])
    return lst

# GENERATING A NULL MATRIX

def null_matx(r,c): # making a null matrix
    # r is for number of rows and c for columns                
    X = []
    for i in range(r):
        Y = []
        for j in range(c):
            Y.append(0)
        X.append(Y)
    return X

# GENERATING AN IDENTITY MATRIX

def identity_matx(n):
    I = null_matx(n,n)
    for i in range(n):
        I[i][i] = 1
    return I

# GENERATING A MATRIX FROM THE LIST

def make_matx(val,r,c): # val is for the values imported from the list
    Nu = null_matx(r,c)
    for i in range(r):
        for j in range(c):                      # the string of numbers is marked as 0 1 2...
            Nu[i][j] = float(val[c*i + j])      # running through all columns of the given row
    return Nu 

# DISPLAYING THE LIST AS A MATRIX

def disp_matx(lst): # lst is the matrix input as a list
    print("The matrix representation is: ")
    for i in range(len(lst)):
        t = 0                  # using t as a counter
        while t < len(lst[0]): # running through each column per specified row
            dum = lst[i][t]    # define a dummy variable
            print(" " + str(dum)+ " ",end=" ") 
            t += 1
        print("\n")
    print("---")

# ADDING MATRICES

def add_matx(a,b):
    if len(a) == len(b) and len(a[0]) == len(b[0]): # check step for invalid operations
        X = null_matx(len(a),len(a[0]))
        for i in range(len(a)):
            for j in range(len(a[0])):
                X[i][j] = a[i][j] + b[i][j]        # individual addition
        return X
    else:
        print("Please input matrices of same order.")

# MULTIPLYING MATRICES

def prod_matx(a,b):
    X = null_matx(len(a),len(b[0])) # null matrix of order of desired output matrix
    if len(a[0]) == len(b):         # check step
        for i in range(len(a)):              # keeping row of 1st matrix fixed
            for j in range(len(b[0])):       # keeping column of 2nd matrix fixed
                for k in range(len(a[0])):   # len(a[0]) == len(b) so we run through the number of columns of A/rows of B
                    X[i][j] += a[i][k]*b[k][j]  # multiplication step
        return X
    else:
        print("Multiplication is undefined for these two matrices.")

# ROUNDING OFF UPTO kth DECIMAL PLACE

def round_matx(A,k):
    r = len(A)
    c = len(A[0])
    # A, r, c = Matrix and its dimensions
    # k = no. of decimal places to round off to.
    for i in range(r):
        for j in range(c):
            A[i][j]=float(format(A[i][j],f'.{k}f'))
    return A

# SOLUTION OF A SYSTEM OF LINEAR EQUATIONS BY GAUSS JORDAN ELIMINATION

def gauss_jordan(a, b):
    n = len(b) 
    for m in range(n): 
	# partial pivot step
        if abs(a[m][m]) < 1.0e-12: 
            for k in range(m+1, n): 
                if abs(a[k][m]) > abs(a[m][m]):
                    for j in range(m, n): 
                        a[m][j], a[k][j] = a[k][j], a[m][j] 
                    b[m], b[k] = b[k], b[m] 
                    break
	
        pivot = a[m][m] # marking the pivot
        if pivot == 0:
            print("There are infinitely many solutions to the system.")
            return
        for j in range(m, n): 
            a[m][j] /= pivot
        b[m] /= pivot
	
        for k in range(n):      # backward elimination
            if k == m or a[k][m] == 0: continue
            ratio = a[k][m]
            for j in range(m, n): 
                a[k][j] -= ratio * a[m][j]
            b[k] -= ratio * b[m]
    X = [b]
    return X

# DETERMINANT OF A MATRIX

def find_determinant(M):
    n = len(M) # dimension of the nxn matrix
    if n != len(M[0]): # check step for square matrix
        print("Please input a square matrix.")
    else:
        tick = 0 # counter for sign after diagonalization (due to row exchanges)
	# partial pivoting step
        for k in range(n-1):
            if abs(M[k][k]) < 1.0e-5:
                for i in range(k+1, n):
                    if abs(M[i][k]) > abs(M[k][k]):
                        for j in range(k, n):
                            M[k][j], M[i][j] = M[i][j], M[k][j] # placing pivot
                            tick += 1
    # elimination step
            for i in range(k+1, n):
                if M[i][k] == 0: continue
                factor = M[i][k]/M[k][k]
                for j in range(k, n):
                    M[i][j] = M[i][j] - factor * M[k][j]
    # diagonal multiplication step
        v = 1
        for i in range(n):
            v = v*M[i][i] 
        v = v*(-1)**tick
    return v

# INVERSE OF A MATRIX BY DIAGONALIZATION USING GAUSSIAN ELIMINATION

def matx_inv(M):
    n = len(M) # dimension of the matrix
    P = [[0.0 for i in range(n)] for j in range(n)] # null matrix
    for i in range(3): # for a 3x3 matrix, the identity
        for j in range(3):
            P[j][j] = 1.0
    for i in range(n):
        M[i].extend(P[i])
    # Finding inverse through gaussian elimination
    for k in range(n):
        if abs(M[k][k]) < 1.0e-5:
            for i in range(k+1, n):
                if abs(M[i][k]) > abs(M[k][k]):
                    for j in range(k, 2*n):
                        M[k][j],M[i][j] = M[i][j], M[k][j] # placing the pivot
                    break
        pivot = M[k][k] # marking pivot
        if pivot == 0: # check step
            print("This matrix is not invertible.")
            return
        else:
            for j in range(k, 2*n): # running through columns of pivot
                M[k][j] /= pivot
            for i in range(n): # rows of subtraction
                if i == k or M[i][k] == 0: continue
                factor = M[i][k]
                for j in range(k, 2*n): # columns of subtraction
                    M[i][j] -= factor * M[k][j]
    for i in range(n): # displaying the inverse matrix
        for j in range(n, len(M[0])):
            print("{:.2f}".format(M[i][j]), end = " ") # rounding up to decimal place 2 i.e. 0.01
        print()

# TRANSPOSE OF A MATRIX

def transpose(L):
    r = len(L)
    c= len(L[0])

    Nu = null_matx(r,r)

    for i in range(r):
        for j in range(c):
            Nu[j][i] = L[i][j]
    return Nu

# FORWARD SUBSTITUTION

def sub_FOW(L,v):
    r = len(L) # Using, Ux=y and Ly=v, for Mx=v system of equations
    X = null_matx(r,1) 
    for i in range(r): # iterating through rows
        dum = 0
        for j in range(i): # iterating through columns
            dum += L[i][j]*X[j][0]  # dummy variable to use for the substitution step
        X[i][0] = (v[i][0]-dum)*(1/L[i][i])  # substitution
    return X

# BACKWARD SUBSTITUTION

def sub_BACK(U,v):
    r = len(U) 
    X = null_matx(r,1)
    for i in range(r-1,-1,-1): # reverse of the forward substitution order
        dum = 0
        for j in range(r-1,i,-1):
            dum += U[i][j]*X[j][0]
        X[i][0] = (v[i][0]-dum)*(1/U[i][i])
    return X

# DOOLITTLE'S METHOD FOR SOLVING A SYSTEM OF LINEAR EQUATIONS

def Doolittle(M):
    r = len(M)
    c = len(M[0])

    for i in range(r-1): # iterating through rows
            for j in range(c): # through columns
                dum = 0
                if i+1 <= j:
                    for k in range(i+1):
                        dum += M[i+1][k]*M[k][j]
                    M[i+1][j]=M[i+1][j]-dum
                else:
                    for k in range(j):
                        dum += M[i+1][k]*M[k][j]
                    M[i+1][j]=(M[i+1][j]-dum)/M[j][j]
    M = round_matx(M,2)
    return M

def Doolittle_Sol(MX):
    r = len(MX)
    c = len(MX[0])
    
    # Separating A and b from the Augmented matrix
    A = null_matx(r,r)
    b = null_matx(r,1)
    for i in range(r):
        b[i][0] = MX[i][-1]
        for j in range(c-1):
            A[i][j] = MX[i][j]   # A and b are now separated
    
    A2 = A          # Creating a duplicate of A
    
    A2 = Doolittle(A2)    # Performing LU decomposition on A using doolittle()
    
    # Separating L and U
    if A2!=None:          # Decomposing A2 into L and U using Doolittle
        L = null_matx(r,r)
        U = null_matx(r,r)
        for i in range(r):
            for j in range(r):
                if j<i:
                    L[i][j] = A2[i][j]
                if j>=i:
                    U[i][j] = A2[i][j]    # Separating L and U from the L/U augmented form obtained from doolittle()
                    if j==i:
                        L[i][i] = 1       # Making diagonal elements of L to 1
        
        p = sub_FOW(L,b)        # Solving Ly=b
        q = sub_BACK(U,p)       # Finally solving Ux=y       # Using custom round function to round the matrix to 3 decimals
        return(q)
        
    else:
        print("Unsuccessfull Operation.")

# CROUT'S METHOD FOR SOLVING A SYSTEM OF LINEAR EQUATIONS

def Crout(M):

    r = len(M)
    c = len(M[0])

    for j in range(1,r):                 #choosing row number
        for i in range(c):  
            dum = 0             #choosing column number
            if i>=j:                     #Calculating u_{ij}
                for k in range(j):
                    dum += M[i][k]*M[k][j]
                M[i][j] = M[i][j]- dum     #replacing the original matrix with the calculated value
            elif i<j:                   #Calculating l_{ij}
                for k in range(i):
                    dum+=M[i][k]*M[k][j]
                M[i][j]=(M[i][j]-dum)/M[i][i]
    M = round_matx(M,2)
    return M

def Crout_Sol(MX):
    r = len(MX)
    c = len(MX[0])

    M = null_matx(r,r)
    X = null_matx(r,1)

    for i in range(r):
        X[i][0] = MX[i][-1]
        for j in range(c-1):
            M[i][j] = MX[i][j]
    
    P = Crout(M)
    

    if P == None:
        print("Unsuccessfull Operation.")
    else:
        L = null_matx(r,r)
        U = null_matx(r,r)
        for i in range(r):
            for j in range(r):
                if j <= i:
                    L[i][j] = P[i][j]
                    if j == i:
                        U[i][i] = 1
                elif j > i:
                    U[i][j] = P[i][j]

        p = sub_FOW(L,X)
        q = sub_BACK(U,p)
        
        M = round_matx(M,2)
        return(q)

# CHOLESKY DECOMPOSITION

def Cholesky(M):
    r = len(M)
    L = null_matx(r,r)
    for j in range(r):
        for i in range(j,r):
            dum = 0
            if i == j:
                for k in range(j):
                    dum = dum + (L[i][k]**2)
                L[i][j] = (M[i][j] - dum)**(1/2)
            else:
                for k in range(j):
                    dum = dum + (L[i][k]*L[j][k])
                L[i][j] = (M[i][j] - dum)/L[j][j]
    return L

def Cholesky_Sol(MX):
    r = len(MX)
    c = len(MX[0])

    M = null_matx(r,r)
    X = null_matx(r,1)

    for i in range(r):
        X[i][0] = MX[i][-1]
        for j in range(c-1):
            M[i][j] = MX[i][j]
    
    L = Cholesky(M)
    U = transpose(L)

    n = len(L)
    y = [0 for i in range(n)]
    x = [0 for i in range(n)]

    for i in range(n):
        sumj = 0
        for j in range(i):
            sumj += L[i][j]*y[j]
        y[i] = (X[i][0]-sumj)/L[i][i]

    for i in range(n-1, -1, -1):
        sumj = 0
        for j in range(i+1, n):
            sumj += U[i][j]*x[j]
        x[i] = (y[i]-sumj)/U[i][i]

    for i in range(len(x)):
        x[i]=float(format(x[i],f'.{2}f'))

    return x

# DOOLITTLE'S METHOD FOR INVERSE FINDING

def Doolittle_Inverse(M):
    n = len(M)
    I = identity_matx(n)

    B = Doolittle(M); test = find_determinant(M)

    if test == 0:
        print("Inverse does not exist.")
    else:
        L = null_matx(n,n); U = null_matx(n,n)
        for i in range(n):
            for j in range(n):
                if j<i:
                    L[i][j] = B[i][j]
                if j>=i:
                    U[i][j] = B[i][j] 
                    if j==i:
                        L[i][i] = 1
    inv = null_matx(n,n)
    
    for i in range(n):
        b = null_matx(n,1)
        for i in range(n):
            b[i][0] = M[i][i]
        y = sub_FOW(L,b)
        x = sub_BACK(U,y)
    for j in range(n):
        inv[j][i] = x[j][0]
    inv = round_matx(inv,2)
    return inv


#### --- ROOT FINDING --- ####

# BISECTION METHOD

def Bisection(a,b,e,f):

    itr = []; fx = []; err = []  # storing the no. of iterations, corresponding value of f and the half bracket length (tolerance)

    if f(a)*f(b) < 0:     # necessary condition of bracketing
        c=(a+b)/2             # Bisection of interval

        switch = True
        i=0

        print("No. of iterations (i)        "+"Successive Bisections (half bracket length)")

        while switch == True and i<15:

            print("        ", i,"                   ",abs(b-a)/2,"\n")

            if f(a)*f(c) < 0:     # Shortening the bracket
                b = c             # The condtions help determine
            elif f(c)*f(b) < 0:   # if c needs to be shifted towards
                a = c             # a or b, i.e. closer to the root
            
            c = (a+b)/2

            if abs(b-a)/2 < e:   # tolerance check
                switch = False
            i = i+1

            itr.append(i); fx.append(f(c)); err.append(abs(b-a)/2)

        print (str(c) + " is the root.")
        graph.plot(itr,fx,'-b', label = 'Root finding steps of Bisection Method.')
        graph.title("f(x_i) vs i")
        graph.xlabel("Number of iterations (i)")
        graph.ylabel("f(x_i)")
        graph.show()
        graph.plot(itr,err,'-b', label = 'Steps to convergence in Bisection Method')
        graph.title("(b-a)/2 vs i (convergence speed)")
        graph.xlabel("Number of iterations (i)")
        graph.ylabel("Successive Bisections (half bracket length)")
        graph.show()





    elif f(a)*f(b) == 0:
        if f(a) == 0:
            c = a
            print(str(a)+" is the root.")
        elif f(b) == 0:
            c = b
            print(str(b)+" is the root.")

    elif f(a)*f(b) > 0:
        print("Choose interval carefully.")
    return float(c)

# REGULA-FALSI METHOD

def RegulaFalsi(a,b,e,f):

    itr =[]; fx = []; err =[] # storing the no. of iterations, corresponding value of f and the half bracket length (tolerance)


    if f(a)*f(b) < 0: # necessary condition of bracketing

        print("No. of iterations (i)        "+"Successive Bracketing (half bracket length)")

        i=0
        while abs(b-a)/2 > e and i<14:

            c = b - (((b-a)*f(b))/(f(b)-f(a)))  # Position through slope of the line (False Position)

            print("        ", i,"                       ",abs(b-a)/2,"\n")

            if f(a)*f(c) < 0:  # again, the same process as in Bisection
                b = c
            elif f(c)*f(b) < 0:
                a = c
            
            i = i+1
            itr.append(i); fx.append(f(c)); err.append(abs(b-a)/2)

        
        print (str(c) + " is the root.")
        graph.plot(itr,fx,'-b', label = 'Root finding steps of Regula Falsi Method.')
        graph.title("f(x_i) vs i")
        graph.xlabel("Number of iterations (i)")
        graph.ylabel("f(x_i)")
        graph.show()
        graph.plot(itr,err,'-b', label = 'Steps to convergence in Regula Falsi Method')
        graph.title("(b-a)/2 vs i (convergence speed)")
        graph.xlabel("Number of iterations (i)")
        graph.ylabel("Successive Bracketing (half bracket length)")
        graph.show()


    elif f(a)*f(b) == 0:
        if f(a) == 0:
            print(str(a)+" is the root.")
        elif f(b) == 0:
            print(str(b)+" is the root.")

    elif f(a)*f(b) > 0:
        print("Choose interval carefully.")

# NEWTON-RAPHSON METHOD

def Diff(x,f):        # first derivative of a function
    h = 1/1000
    y = 0.5*(f(x+h) - f(x-h))/h
    return y



def NewtonRaphson(x_o,e,f):  

    i = 0 # iterations
    x = 1 # reference marker

    while abs(x-x_o) > e and i < 20:
        x = x_o
        x_o = x_o - (f(x_o)/Diff(x_o,f))  # Formula of the Mean value Theorem

        if f(x_o) == 0:
            print(str(x_o) + " is the root.")
        i += 1
    print("The root is: " + str(x_o))
    return x_o

# LAGUERRE METHOD FOR POLYNOMIALS

def f(x, c,n):       # creating the polynomial of degree n and coefficients c
    j = 0
    for i in range(1,n+1):
        j += c[i-1]*x**(n-i)
    return j 
    
def D1f(x, c, n, f):     # first derivative of the polynomial function
    h = 1/1000
    y = (f(x+h,c,n) - f(x-h,c,n))/(2*h) 
    return y

def D2f(x, c, n, f):     # second derivative of the polynomial function
    h = 1/1000
    y = (D1f(x+h,c,n,f)-D1f(x-h,c,n,f))/(2*h) 
    return y

def Lag(a_o, e, c, n, f):        # laguerre's method
    i = 0 ; a = 0             # i stores the iterations, a is our guess
    while abs(a_o-a) > e and i <= 12:
        a = a_o
        y1 = D1f(a_o, c, n, f)/f(a_o, c, n)       # up upto 2nd term in Taylor expansion
        y2 = y1**2 - (D2f(a_o, c, n, f)/f(a_o, c, n))  # up upto 3rd term in Taylor expansion
        if abs(y1 + math.sqrt((n-1)*(n*y2-y1**2))) > abs(y1 - math.sqrt((n-1)*(n*y2-y1**2))):  # conditions for Lagurre's method
            k = n/(y1 + math.sqrt((n-1)*(n*y2-y1**2)))
        elif abs(y1 - math.sqrt((n-1)*(n*y2-y1**2))) > abs(y1 + math.sqrt((n-1)*(n*y2-y1**2))):
            k = n/(y1 - math.sqrt((n-1)*(n*y2-y1**2))) 
        else:
            if f(a_o, c, n)==0:
                print('One of the roots obtained:',round(a_o,6))
        a_o -= k       # new trial
        i += 1          
    return a_o

def syn_div(a_o, c):      #synthetic division 
    if abs(c[0]) != 1:            
        for value in c:
                value = value/c[0]          # dividing the coefficients to get coefficient of highest degree as 1
    for k in range(0, len(c)-1):
            c[k+1] = a_o*c[k] + c[k+1]      # separating the values
    return c
 

def Roots_Laguerre(e, guess, c,):            # display function for roots
    n = len(c) 
    roots = []
    for index in range(n, 1, -1):
        guess = Lag(guess, e, c, index, f)     # performing laguerre
        if index > 0:
            c = syn_div(guess,c)        # performing Synthetic division.
        roots.append(round(guess, 4))
    print("The roots of the polynomial are:",roots)