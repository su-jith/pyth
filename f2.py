f=open('E:\sujith\myfile.txt','r')
l=f.read().split()
lo=len(max(l,key=len))
result=[i for i in l if(len(i)==lo)]
print(result)
