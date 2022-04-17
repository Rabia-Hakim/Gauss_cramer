from turtle import shape
import numpy as np
import sys

#The form of the equation
print ("The form of the equation is: Aij*Xi = Bi (A[i][i]≠ 0 for Gaussian method\n")

# Construction of the matrix A:
n = int(input('Enter the value of n: '))
A = np.zeros((n,n))

print('Enter the coefficients of the matrix A: ')
for i in range(n):
    for j in range(n):
        A[i][j] = float(input( 'a['+str(i+1)+']['+ str(j+1)+']='))

print(A)

#Definition of vector X
X=np.zeros((n,1))

# Construction of the Vector B:
B=np.zeros((n,1))
print('Enter the coefficients of the vector B: ')
for i in range(n):
    B[i][0] = float(input( 'b['+str(i+1)+']['+ str(1)+']='))
    
print(B)

det=np.linalg.det(A)
Iszero=True
#Functions
def Gauss (n,A,B): 

 for i in range(n):
    if A[i][i] == 0.0:
        sys.exit('Divide by zero detected!')
    for j in range(i+1, n):
        ratio = A[j][i]/A[i][i]
        B[j][0] = B[j][0] - ratio * B[i][0]
        for k in range(n):
            A[j][k] = A[j][k] - ratio * A[i][k]

def istrinagulaire(A):

 Istriangulaire = True
 
 for i in range(n):
    for j in range(i):
        if(A[i][j] != 0):
            Istriangulaire = False
            break
 
 if(Istriangulaire == True):
    print("\nLa matrice est une matrice triangulaire supérieure.")
 else:
    print("\nLa matrice n'est pas une matrice triangulaire supérieure.")                          

def solutionGuass(A,B,n):
 X[n-1] = B[n-1]/A[n-1][n-1]
 for i in range(n-2,-1,-1):
    X[i] = B[i][0]
    
    for j in range(i+1,n):
        X[i] = X[i] - A[i][j]*X[j]
    
    X[i] = X[i]/A[i][i]
 
 print ('The solution of the equation with Gaussian method is:\n', X)

def SolutionCramer(A,B,det):
    for i in range(n):
     D=A.copy()
     D[:,i] = B.squeeze().copy()
     X[i]= np.linalg.det(D)/det
 
    print ('The solution of the equation with cramer method is:\n', X)

#Choice of Method
for i in range (n):
  if A[i][i] ==0:
    Iszero=True   
    break 
  else:
    Iszero=False

choix=int(input('choose "1" for GAussian methode or "2" for Cramer\'s method: \n'))
if det==0:
    print("Cannot apply both methods")
else:
    if choix==1:
      if Iszero == True:
          print('A[i][i] is zero, for now, the solution will be with Cramer method\n')
          SolutionCramer(A,B,det)
      else:
          Gauss(n,A,B)
          solutionGuass(A,B,n)
      
    elif choix==2:
      SolutionCramer(A,B,det)
    else:
      print("You have to choose 1 or 2")
