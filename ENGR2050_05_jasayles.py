# ENGR2050_05_jasayles.py
# Ethan Sayles
# Mar 2, 2017
import numpy as np

#Trapezoidal integral approximation
def trapproximation(F, a, b, N):                  #Function, start value, end value, step number
    delta_x = (b - a) / N                                      #Process of finding the trapezoidal approximation
    approxint = .5 * (F(a) + F(b))
    for i in range(1, N):
        approxint += F(a + i * delta_x)
    return (approxint * delta_x)
    
def simpproximation(F, a, b, N):                  #Function, start value, end value, step number
    if (N % 2 == 0):  
         N += 1
    delta_x = (b - a) / (N - 1)                               #Process of finding the Simpsons approximation
    approxint = F(a) + F(b)
    for i in range(1, N - 1, 2):
        approxint += 4 * F(a + i * delta_x)
    for i in range(2, N-1, 2):
        approxint += 2 * F(a + i * delta_x)
    return (approxint * delta_x / 3)

def central_reimann(F, a, b, N):                  #Function, start value, end value, step number
    delta_x = (b - a) / N                                     #Process of finding the central reimann sum approximation
    approxint = 0
    for i in range(1, N):
        approxint += F(a + (i - .5) * delta_x)
    return (approxint * delta_x)
    
def rel_error(Func, F, a, b, N, I):                  #integral approximation, function, start value, end value, step number
    error = np.abs(1 - Func(F, a, b, N) / I)        #Calculate the error for a given function relative to the actual integral vaule
    return (error)
#Conditional to check for test cases
if __name__ == '__main__':
    my_f = lambda x: (2 * x * np.exp(x * x) + 1)     
    print ("Exact result = ",  np.e)
    print ("   n     Trapezoidal             Trap Error               Simpson                 Simp Error                  Central Riemann               CR Error")
    for i in range(1, 11):
        print (2**i, "   ",   trapproximation(my_f, 0, 1, 2**i) , "   ", rel_error(trapproximation, my_f, 0, 1, 2**i, np.e), "   ",  simpproximation(my_f, 0, 1, 2**i), "   " , rel_error(simpproximation, my_f, 0, 1, 2**i, np.e), "   ",  central_reimann(my_f, 0, 1, 2**i), "   " , rel_error(central_reimann, my_f, 0, 1, 2**i, np.e))

    
    
    
