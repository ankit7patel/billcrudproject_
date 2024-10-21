from django.shortcuts import render
from .models import student
from django.http import HttpResponse
from .models import Query

def home(request):
    return render (request , 'home.html')


def login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        print(email,password)
        
        user = student.objects.filter(stu_email=email)
        print(user)
        if user:
            user_data=student.objects.get(stu_email=email)
            print(user_data)
            email1=user_data.stu_email
            name1=user_data.stu_name
            contact1=user_data.stu_contact
            password1=user_data.stu_password
            print(name1,email1,contact1,password1)

            if password1==password:
                data={
                    'name':name1,
                    'email':email1,
                    'contact':contact1,
                    'password':password1
                }
                # return render(request,'dashboard.html',{'data':data})
                query_data=Query.objects.filter(email=email1) 
                return render(request ,'dashboard.html' , {'data':data , 'query_data':query_data})
 
            else:
                msg="You Entered Incorrect Password"
                return render(request,'login.html',{'msg':msg})
        else:
            msg="email not register"
            return render(request,'login.html',{'msg':msg})

    else:
        return render(request, 'login.html')


def register(request):
    if request.method=='POST':
        print(request.POST)  
        name = request.POST.get('name')
        email = request.POST.get('email')
        contact = request.POST.get('contact')
        password = request.POST.get('password')
        cpass = request.POST.get('confirm_password')
        print(name,email,contact,password,cpass)


        if password==cpass:
            user=student.objects.filter(stu_email=email)   #  database me email ni hai fr bhi empt dega 
            # user=student.objects.get(stu_email=email)     # database me email ni hai to error dega 
            # print(user)
            if user:
                user_name=student.objects.filter (stu_name=name)
                if user_name:
                    msg="email alredy exist"
                else:
                    msg="Email ID and Name already exist"    
                    return render (request, 'register.html',{'msg':msg})
            else:
                student.objects.create(
                            stu_name=name,
                            stu_email=email,
                            stu_contact=contact,
                            stu_password=password)
                msg="registration successfully "
                return render (request,'login.html',{'msg':msg}) 
        else: 
            msg="password & cpass not match"
            return render (request, 'register.html',{'msg':msg})
    else: 
        return render (request , 'register.html')
    
def dashboard(request):
    return render (request, 'dashboard.html'    )



   
def query(request):
    if request.method=="POST":
        name=request.POST['name']
        email=request.POST['email']
        query=request.POST['query']

        print(name,email,query)

        Query.objects.create(name=name,email=email,query=query)
        user_data=student.objects.get(stu_email=email)
        my_data={
            'name':user_data.stu_name,
            'email':user_data.stu_email,
            'contact':user_data.stu_contact,
            'password':user_data.stu_password
        }
        print(my_data)
        all_query=Query.objects.filter(email=email)
        return render(request, 'dashboard.html',{'key1':all_query,'data':my_data})
        print(all_query)
   
    else:
        return render(request,'dashboard.html')
    


def querydata(request,x):
    queryData=Query.objects.filter(email=x)
    print(queryData)

    user_data=student.objects.get(stu_email=x)
    my_data={
            'name':user_data.stu_name,
            'email':user_data.stu_email,
            'contact':user_data.stu_contact,
            'passwaord':user_data.stu_password
        }
    print(my_data)
    all_query=Query.objects.filter(email=x)
    return render(request, 'query.html',{'key1':all_query,'data':my_data,})


  
def edit(request,x):
    # print(x)
    querydata=Query.objects.get(id=x)
    # print(querydata)
    email=querydata.email
    name=querydata.name
    query=querydata.query

    # print(query1)

    user_data=student.objects.get(stu_email=email)
    my_data={
             'name':user_data.stu_name,
            'email':user_data.stu_email,
            'contact':user_data.stu_contact,
            'passwaord':user_data.stu_password
        }
    # print(my_data)

    all_query=Query.objects.filter(email=email)
    edit_data={
        'id':x,
        'email':email,
        'name':name,
        'query':query
    }
    return render(request, 'query.html',{'key1':all_query,'data':my_data,'key2':edit_data})

def update(request,x):
        if request.method=="POST":
            name1=request.POST['name']
            email1=request.POST['email']
            query1=request.POST['query']

            print(query1)

            querydata=Query.objects.get(id=x)
            querydata.name=name1
            querydata.email=email1
            querydata.query=query1

            querydata.save()

            user_data=student.objects.get(stu_email=email1)
            my_data={
                'name':user_data.stu_name,
                'email':user_data.stu_email,
                'contact':user_data.stu_contact,
                'passwaord':user_data.stu_password
                }
            print(my_data)
            all_query=Query.objects.filter(email=email1)
            return render(request, 'query.html', {'key1':all_query,'data':my_data})


def logout(request):
    return render(request,'home.html')


def delete(request,x,y):
    querydata=Query.objects.filter(id=x)
    if querydata:
        querydata=Query.objects.get(id=x)
        email=querydata.email

        querydata.delete()

        user_data=student.objects.get(stu_email=email)
        my_data={
            'name':user_data.stu_name,
            'email':user_data.stu_email,
            'contact':user_data.stu_contact,
            'passwaord':user_data.stu_password
        }
        print(my_data)
        all_query=Query.objects.filter(email=email)
        return render(request, 'query.html',{'key1':all_query,'data':my_data})
    else:
        user_data=student.objects.get(stu_email=y)
        my_data={
            'name':user_data.stu_name,
            'email':user_data.stu_email,
            'contact':user_data.stu_contact,
            'password':user_data.stu_password

        }
        print(my_data)
        all_query=Query.objects.filter(email=y)
        return render(request, 'query.html',{'key1':all_query,'data':my_data})