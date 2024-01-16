from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import hospital,receiver,donor,Request
from django.contrib.auth import authenticate,login as auth_login

# Create your views here.



def index(request):
    return render(request,'index.html')

def hospitalindex(request):
    return render(request,'hospital.html')

def userindex(request):
    return render(request,'reciever.html')

def login(request):
    return render(request,'login.html')


def hospitalreg(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        location = request.POST.get('location')
        password = request.POST.get('password')

        if hospital.objects.filter(Email_id=email).exists():
            return render(request,'hospitalreg.html',{'message':'Email already exists'})
        if hospital.objects.filter(phone_no=phone).exists():
            return render(request,'hospitalreg.html',{'message':'Contact already exists'})
        
        data = hospital.objects.create(Hospital_name=name,Email_id=email,phone_no=phone,location=location,password=password)
        data.save()
        return redirect(logins)
    else:
        return render(request,'hospitalreg.html')

def recieverreg(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        address = request.POST.get('address')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        hospitalname = request.POST.get('hospitalname')
        password = request.POST.get('password')

        if receiver.objects.filter(Email_id=email).exists():
            return render(request,'recieverreg.html',{'message':'Email already exists'})
        if receiver.objects.filter(phone_no=phone).exists():
            return render(request,'recieverreg.html',{'message':'Contact already exists'})
        
        data = receiver.objects.create(name=name,Address=address,Email_id=email,phone_no=phone,hospital_name=hospitalname,password=password)
        data.save()
        return redirect(logins)
    else:
        return render(request,'recieverreg.html')




def logins(request):
    email = request.POST.get('email')
    password = request.POST.get('password')
    context={'message':'Invalid User Credentials'}

    admin_user = authenticate(request,username=email,password=password)
    if admin_user is not None and admin_user.is_staff:
        auth_login(request,admin_user)
        return redirect('admin:index')
    
    if hospital.objects.filter(Email_id=email,password=password).exists():
        userdetail=hospital.objects.get(Email_id=request.POST['email'], password=password)
        if userdetail.password == request.POST['password'] and userdetail.status=='accepted':
            request.session['hid'] = userdetail.id
          

            return render(request,'hospital.html')
        else:
            return render(request,'login.html',context)
        
    elif receiver.objects.filter(Email_id=email,password=password).exists():
        userdetail=receiver.objects.get(Email_id=request.POST['email'], password=password)
        if userdetail.password == request.POST['password'] and userdetail.status=='accepted':
            request.session['uid'] = userdetail.id


            return render(request,'reciever.html')
        else:
            return render(request,'login.html',context)
        
    else:
        return render(request, 'login.html', {'status': 'Invalid Username or Password'})




def logout(request):
    session_keys = list(request.session.keys())
    for key in session_keys:
      del request.session[key]
    return redirect(index)







#reciever.......................................................

def userprofile(request):
    tem=request.session['uid']
    data=receiver.objects.get(id=tem)
    return render(request,'userprofile.html',{'result':data})



def updat(request,id):
    data=receiver.objects.get(id=id)
    return render(request,'userprofileedit.html',{'result':data})


def updates(request,id):
    user =receiver.objects.get(id=id)
    if request.method=="POST":
        user.name=request.POST.get('name')
        user.Address = request.POST.get('address')
        user.phone_no=request.POST.get('phone')
        user.Email_id=request.POST.get('email') 
        user.hospital_name=request.POST.get('hospitalname') 
        user.save()
        return redirect(userprofile)
    

def addrequest(request):
    if request.method == 'POST':
        id = request.session['uid']
        user = receiver.objects.get(id=id)
        organname = request.POST.get('organname')
        certificate = request.FILES['certificate']
        context = {'message':'successfully requested'}
        data = Request.objects.create(reciver_id=user,organ_name=organname,certificate=certificate)
        data.save()
        return render(request,'addrequest.html',context)
    else:
        return render(request,'addrequest.html')


def requestedlist(request):
    id = request.session['uid']
    user = receiver.objects.get(id=id)
    data = Request.objects.filter(reciver_id=user)
    return render(request,'requestedlist.html',{'data':data})


#hospital.......................................................
    

def hospitalprofile(request):
    tem=request.session['hid']
    data=hospital.objects.get(id=tem)
    return render(request,'hospitalprofile.html',{'result':data})


def hospitalupdat(request,id):
    data=hospital.objects.get(id=id)
    return render(request,'hospitalprofileedit.html',{'result':data})


def hospitalupdates(request,id):
    users =hospital.objects.get(id=id)
    if request.method=="POST":
        users.Hospital_name=request.POST.get('name')
        users.location = request.POST.get('location')
        users.phone_no=request.POST.get('phone')
        users.Email_id=request.POST.get('email') 
        users.save()
        return redirect(hospitalprofile)


def donorpage(request):
    data=request.session['hid']
    data1=donor.objects.filter(hospital_id=data)
    return render(request,'Donor.html',{'data1':data1})


def adddonors(request):
    if request.method == 'POST':
        id=request.session['hid']
        name = request.POST.get('name')
        doctername = request.POST.get('doctername')
        organname = request.POST.get('organname')
        gender = request.POST.get('gender')
        age = request.POST.get('age')
        bloodgroup = request.POST.get('bloodgroup')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        address = request.POST.get('address')
        photo = request.FILES.get('photo')
        idproof = request.FILES.get('idproof')
        data1 = hospital.objects.get(id=id)
        data = donor.objects.create(hospital_id=data1,name=name,doctername=doctername,Organ_name=organname,gender=gender,age=age,bloodgroup=bloodgroup,address=address,email=email,phone=phone,photo=photo,idproof=idproof)
        data.save()
        return redirect(donorpage)
    else:
        return render(request,'add Donor.html')
    


def donordetails(request,id):
    data=donor.objects.get(id=id)
    return render(request,'donordetails.html',{'result':data})


def donoredit(request,id):
    data=donor.objects.get(id=id)
    return render(request,'donoredit.html',{'result':data})


def donoredits(request,id):
    data = donor.objects.get(id=id)
    if request.method == 'POST':
        data.name = request.POST.get('name')
        data.doctername = request.POST.get('doctername')
        data.Organ_name = request.POST.get('organname')
        data.age = request.POST.get('age')
        data.bloodgroup = request.POST.get('bloodgroup')
        data.phone = request.POST.get('phone')
        data.email = request.POST.get('email')
        data.address = request.POST.get('address')
        if 'photo' in request.FILES:
            data.photo = request.FILES['photo']
        if 'idproof' in request.FILES:
            data.idproof = request.FILES['idproof']
        data.save()
        return redirect(donorpage)



def donordelete(request,id):
    data = donor.objects.get(id=id)
    data.delete()
    return redirect(donorpage)


def viewrequest(request):
    a = request.session['hid']
    hospit = hospital.objects.get(id=a)
    data = Request.objects.all()
    # print(data.certificate)
    hos = Request.objects.filter(hospital_id=a)
    dat=Request.objects.exclude(hospital_id=a).exclude(status='Accepted').exclude(status='Assigned')

    all_requests = list(hos) + list(dat)
    result = donor.objects.filter(hospital_id=hospit)

    return render(request,'viewrequest.html',{'data':all_requests,'result':result})


def requestaccept(request, id):
    a = request.session['hid']
    hos = hospital.objects.get(id=a)
    data = Request.objects.get(id=id)
    if request.method == 'POST':
        action = request.POST.get('action') 
        if action == 'Accept':
            data.status = 'Accepted'
        data.hospital_id = hos 
        data.save()
        return redirect(viewrequest)
    return redirect(viewrequest) 


def donortoreceiver(request):
    data=donor.objects.get(id=id)
    return render(request,'viewrequest.html',{'result':data})


def adddonor(request,id):
    data = Request.objects.get(id=id)
    donors = donor.objects.filter(hospital_id=data.hospital_id)
    if request.method == 'POST':
        donorid = request.POST.get('donorid')
        result = donor.objects.get(id=donorid)
        data.donor_id = result
        data.status = "Assigned"
        data.save()
        return redirect(viewrequest)
    return render(request,'assigndonor.html',{'data':data,'data1':donors})


def history(request):
    id=request.session['hid']
    hos = hospital.objects.get(id=id)
    data = Request.objects.filter(hospital_id=hos,status='Assigned')
    return render(request,'donotionhistory.html',{'data':data})

