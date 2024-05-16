############################ Metoh Resolution Order #####################
# La siguiente estructura:
#
#       B     A
#       |  /     \
#       D      -- C
#      /  \  /    |
#    G     F      E
#    |   /   \    |
#    K  J     I   H
#     \ |     |  /
#          L
#
# Tiene la siguiente jerarquia:
# L > H > E > I > J > F > K > G > D > B > C > A

class A:
    def hablar(self):
        print('Hola desde A')        
        
class B:
    def hablar(self):
        print('Hola desde B')
 
class C(A):
    def hablar(self):
        print('Hola desde C')
        
class D(B,A): # El orden es importante, porque primero hereda de B y luego de A
    def hablar(self):
        print('Hola desde D')      
        
class E(C):
    def hablar(self):
        print('Hola desde E')       
        
class F(D,C):
    def hablar(self):
        print('Hola desde F')       
    
class G(D):
    def hablar(self):
        print('Hola desde G')    
    
class H(E):
    def hablar(self):
        print('Hola desde H')    
 
class I(F):
    def hablar(self):
        print('Hola desde I')     
    
class J(F):
    def hablar(self):
        print('Hola desde J')

class K(G):
    def hablar(self):
        print('Hola desde K')

class L(H,I,J,K):
    def hablar(self):
        print('Hola desde L')         
        

print(L.mro())

        



# La siguiente estructura:
#
#    ---- O
#   /    / \     
# R    Q    P
# |   / \  / \     
# V  U   T    S
# | / \ / \  / \   
# Z    Y   X    W
#   \  \  /   /
#       AZ
# Tiene la siguiente jerarquia:
# AZ > Z > Y > U > X > T > Q > V > R > W > S > P > O

class O:
    def hablar(self):
        print('Hola desde O')        
        
class P(O):
    def hablar(self):
        print('Hola desde P')
 
class Q(O):
    def hablar(self):
        print('Hola desde Q')
        
class R(O):
    def hablar(self):
        print('Hola desde R')
        
class S(P):
    def hablar(self):
        print('Hola desde S')
        
class T(Q,P):
    def hablar(self):
        print('Hola desde T')
        
class U(Q):
    def hablar(self):
        print('Hola desde U')
        
class V(R):
    def hablar(self):
        print('Hola desde V')
        
class W(S):
    def hablar(self):
        print('Hola desde W')
        
class X(T,S):
    def hablar(self):
        print('Hola desde X')
        
class Y(U,T):
    def hablar(self):
        print('Hola desde Y')
        
class Z(U,V):
    def hablar(self):
        print('Hola desde Z')
        
class AZ(Z,Y,X,W):
    def hablar(self):
        print('Hola desde AZ')
        
        
print(AZ.mro())