from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def cur(request):
    if request.method=="POST":
        C=request.POST=['CUR']
        N=request.POST=['NA']
        T=request.POST=['TN']
        print(C)
        print(N)
        print(T)

        return HttpResponse('cousre details submit successfully')

    return render(request,'course.html')


def stu(request):
    if request.method=="POST":
        I=request.POST['ID']
        N=request.POST['NA']
        A=request.POST['AD']
        P=request.POST['PN']
        print(I)
        print(N)
        print(A)
        print(P)
        
        return HttpResponse('student details submit successfully')

    return render(request,'student.html')
