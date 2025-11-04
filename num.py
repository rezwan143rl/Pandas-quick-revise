import numpy as np

# numpy attributes
a= np.array([1,2,4],dtype='int32') #1d array
# print(f"datatype is: {a.dtype}")
# print(f"size is: {a.size}")
# print(f"shape is: {a.shape}")
# print(f"dimention is: {a.ndim}")
# print(f"itemsize is: {a.itemsize}")
# print(a)
b=np.array([[1,2,3,4,3,2,1,2],[2,1,4,1,1,5,6,8]],dtype='float16')
# print(f"datatype is: {b.dtype}")
# print(f"size is: {b.size}")
# print(f"shape is: {b.shape}")
# print(f"dimention is: {b.ndim}")
# print(f"itemsize is: {b.itemsize}")
#print(b)
c=np.array([[[1,2,3,4],[2,1,4,1],[1,4,5,6]],[[1,2,3,5],[1,1,11,1],[12,1,1,2]]],dtype='int8')
# print(f"datatype is: {c.dtype}")
# print(f"size is: {c.size}")
# print(f"shape is: {c.shape}")
# print(f"dimention is: {c.ndim}")
# print(f"itemsize is: {c.itemsize}")
# print(c)

##slicing [start:stop:step] *******
#2d
# print(b[0,1])
# print(b[0, :])#print rows using slicing
# print(b[:,2])#print columns using slicing
# print(b[0,2:-1:2])#print specific using slicing here 2 is increment
# b[1,3]=10
# print(b)
# #b[:,2]=5#change columnwise
# b[:,:]=1.01 #change all
# #b[1,:]=0#change row wise
# print(b)
# #3d
# print(c)

# c[0,:,1]=[19,17,23]#explicit 
# c[1,0,:]=0
# c[1,1,:]=11

# print(c)

#boolean mask

# arr = np.array([10, 15, 20, 25, 30, 35])
# mask=arr>20 #returns boolean value true if value is greater 20/x]
# print(arr)
# mask1=arr%10==0
# arr[mask1]=-1
# print(arr)

# #np built in methods
# a=np.zeros((3,2,2))#fill all with 0
# b=np.ones((2,3,4))#fill all with 1
# c=np.full((4,5),75,dtype='int16')#fill all value with given number(shape,value,dtype)
# d=np.full_like(a,4,dtype='int8') # array of size,shape like "a" with value 4
# e=np.random.rand(4,3) #random rand(shape)
# f=np.random.random_sample(a.shape)# random sample as a
# print(f)
# g=np.random.randint(3,7,size=(5,5))# random integer from value 3 to 6(7excluded) in shape 5 by 5
# print(g)
# h=np.identity(5) #identity matrice
# print(h)
# j=np.array([[1,2,4,3]]) 
# i= np.repeat(j,3,axis=0)#repeat an array 3 times in axis column
# print(i)
# ##excercise
# k=np.ones((5,5))
# l=np.zeros((3,3))
# l[1,1]=9
# k[1:-1,1:-1]=l
# print(k)
#copying
a1=np.array([1,2,3,4],dtype='float32')
b1=np.array([9,6,-1,12],dtype='float32')
#b1=a  #here a changes meaning its not a copy rather just same pointer
# b1=a.copy()
# b1[0]=100
# print(a)
##artihmatic
#a1+=2 #adds 2 to all
#a1-=2
#a1=a1**2 #power
#a1*=2
#a1/=2
#c1=a1+b1
#c1=a1-b1
#c1=a1*b1
#c1=a1/b1

# #trigonometric

# c1=np.sin(a1)
# a1[1]=np.sin(a1[1]) # sin cos tan of all values/specefic 
# print(c1)
# print(a1)

#linear algebra

#matric multiplication

# d1=np.array([[1,12,11,4],[2,3,20,2],[1,20,3,14],[2,3,1,2]])
# print(d1)
# e1=np.array([[5,4],[1,22],[12,15],[1,8]])
# h1=np.array([[5,4],[1,22]])
#print(h1)
# f1=np.matmul(d1,e1) #matrice multiplication

##linear algebra part
#https://numpy.org/doc/stable/reference/routines.linalg.html
# g1=np.linalg.det(h1) # determinent
# print(g1)
# i1=np.linalg.inv(d1) #if determinent zero then there is no inverse
# print(i1)
##statistics
# a3=[[1,2,4],[9,1,6]]
# print(np.min(a3,axis=0)) #minimum column wise if axis 1 then row wise
# print(np.max(a3)) #maximum 
# b3=[[1,2,4],[9,3,6]]
# print(np.sum(b3)) #sum of all
# print(np.sum(b3,axis=0)) #sum of all column wise
# print(np.sum(b3,axis=1)) #sum of all row wise

## reorganising array

# c3=np.array([[1,12,11,4],[2,3,20,2],[1,20,3,14],[2,3,1,2]])
# print(c3.reshape(2,2,2,2)) # reshapes the array but must be same size