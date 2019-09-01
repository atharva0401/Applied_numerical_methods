#newton's forward interpolation for small numbers.
#remember that this is forward interpolation and might not work very well for points far away from first point
#author - nitin ranjan
x = []     #values of x
y = []     #values of y

dy1 =[]        #list of first difference in f(x)
dy2 = []       #list of second difference in f(x)
dy3 =[]        #not practical to list differences beyond here
m = int(input("Enter the number of datapoints available: "))     #number of datapoints available

for i in range(m):                                    
        print("\nEnter the values of x",i, "in the set: ")      
        l = eval(input())
        x.append(l)
for j in range(m):
        print("\nEnter the values of f(x",j,") in the set: ")
        k = eval(input())
        y.append(k)
print("\nThe list of all values of x mentioned: ",x)
d= x[1]-x[0]
print("\nClass length is: ",d,"\n")
print("\nThe list of corresponding f(x) given is: ",y)


ques=eval(input("Enter the value of x for which f(x) is to be determined: "))
print("\n now this becomes our problem.\n")
print("\nthe table hence is :")


#defining difference table


for j in range(1,m):
    k = y[i]-y[i-1]
    dy1.append(k)

print("The series of df(x) is: ",dy1)

for j in range(1,m-1):
    k = dy1[j]-dy1[j-1]
    dy2.append(k)

print("The series of d2f(x) is: ",dy2)

for j in range(1,m-2):
    k = dy2[j]-dy2[j-1]
    dy3.append(k)

print("The series of d3f(x) is: ",dy3)

p = (ques-x[0])/d

print("As per Newton's forward algorithm, f(x) = f(x0) + p*d1f(x) + p*(p-1)*d2f(x) + p*(p-1)*(p-2)*d2f(x) + ...\n")

ans = y[0] + p*dy1[0] + p*(p-1)*dy2[0] + p*(p-1)*(p-2)*dy2[0]

print("The value of function at x=",ques," is hence: ",ans)
 



    
