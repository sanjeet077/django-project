from django.http import HttpResponse 
from django.shortcuts import render 

def homepage(request) :
    # data={
    #     'title' : 'home new' ,
    #     'bdata' : 'welcome to wscubetech' ,
    #     'cdata' : ['php' , 'java' , 'django'] ,
    #     'numbers' : [10,20,30,40,50] ,
    #     'student_Details' :[
    #         {'name':'pradip' , 'mobile' : 7854845648} ,
    #         {'name' :'rohit' , 'mobile' : 9965742810}
    #     ]
    # }
    # return render(request ,"index.html" , data)
    return render(request ,"index.html")

def aboutus(request) :
    return HttpResponse ("welcome to wscube tech")

def Course(request) :
    return HttpResponse ("welcome to wscubetech")

def courseDetails(request , courseid) :
    return HttpResponse(courseid)