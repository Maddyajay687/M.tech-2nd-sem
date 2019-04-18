
# coding: utf-8

# In[338]:


#Creating a matrix
def read():
    a = int(input('Enter number of rows '))
    b = int(input('Enter number of columns '))
    matrix = []
    for i in range(a):
        print('Enter row {}'.format(i+1))
        m = input()
        m = list(map(int, m.split()))
        matrix.append(m)
    return matrix


# In[339]:


def show(matrix):
    print('*'*20)
    for i in range(len(matrix)):
        for data in matrix[i]:
            print(data,end = " ")
        print()


# In[340]:


# Printing and storing transpose of a matrix
def transpose(X):
    result = [[X[j][i] for j in range(len(X))] for i in range(len(X[0]))]
    return result


# In[341]:


def multiply(A,B):
        result = []
        for i in range(len(A)):
            temp = []
            for j in range(len(B[0])):
                temp.append(0)
            result.append(temp)
        for i in range(len(A)):
            for j in range(len(B[0])):
                for k in range(len(B)):
                    result[i][j] += A[i][k] * B[k][j]
        return result


# In[342]:


def dot_product(A,B):
    prod = []
    for i in range(len(A)):
        sum = 0
        for data in range(len(A[i])):
            sum += A[data][i] * B[data][i]
        prod.append(sum)
    return prod
        


# In[343]:


def minor(m,i,j):
    return [row[:j] + row[j+1:] for row in (m[:i]+m[i+1:])]

def determinant(a):
    if(len(a) == 2):
        return a[0][0] * a[1][1] - a[0][1] * a[1][0]
    res = 0
    for c in range(len(a)):
        res += ((-1)**c)*a[0][c]*determinant(minor(a,0,c))
    return res


# In[344]:


def co_factor(A):
    fact = []
    for i in range(len(A)):
        ans = []
        for j in range(len(A)):
            print((-1)**(i+j))
            ans.append(((-1) ** (i+j)) *  determinant(minor(A,i,j)))
            print(ans)
        fact.append(ans)
    return fact


# In[345]:


def adjoint(A):
    return transpose(co_factor(A))


# In[346]:


def inverse(A):
    z = adjoint(A)
    inv = []
    for i in range(len(z)):
        new_lst = [x/determinant(A) for x in z[i]]
        inv.append(new_lst)
    return inv    

