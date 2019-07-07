from django.shortcuts import render, HttpResponse, redirect, HttpResponseRedirect
from FitnessStore.models import Person, custinfo, strengthprod
from FitnessStore.forms import PersonForm, custregister
from django.contrib import messages

def demo(request):
    return render(request, "index.html", {})

def ShowPersons(request):
    persons = Person.objects.all()
    return render(request, "Persons.html", {"persons": persons})

def delPerson(request,id):
    p = Person.objects.filter(id=id)
    p.delete()
    return redirect(ShowPersons)

def AddPerson(request):
    if(request.method=="GET"):
        return render(request,"addPerson.html",{})
    else:
        id = request.POST["pid"]
        pnames = request.POST["pname"]
        plocation = request.POST["ploc"]
        p = Person.objects.get(id=id)
        if(p==None):
            p = Person(id,pnames,plocation)
            p.save()
        else:
            return HttpResponse("Id Exists!")
            #return render(request, "addPerson.html", {"err":err})
            #return HttpResponseRedirect("/FitnessStore/addPerson/")
            #return redirect(AddPerson)'''
        return redirect(ShowPersons)

def editPerson(request, id):
    p = Person.objects.get(id=id)
    if (request.method == "GET"):
        return render(request, "editperson.html", {"p":p})
    else:
        p.pname = request.POST["pname"]
        p.plocation = request.POST["ploc"]
        p.save()
        return redirect(ShowPersons)

def userLogin(request):
    u = custinfo.objects.filter(cmail=cmail)
    p = custinfo.objects.filter(cpass=cpass)
    cid = request.POST['cmail']
    cpass = request.POST['cpass']
    if(cid == u and cpass == p):
        return redirect(demo)
    else:
        return HttpResponse("Wrong Credentials")

###############################Customer Sections#############################################

def custRegister(request):
    form = custregister(request.POST)
    if(request.method=="GET"):
        return render(request,"custregister.html",{})

    if(form.is_valid):
        form.save()
        cfname = request.POST["cfname"]
        cmail = request.POST["cmail"]
        cpass = request.POST["cpass"]
        ccontact = request.POST["ccontact"]
        form = custinfo(cfname,cmail,cpass,ccontact)
    return redirect(showCust)

def login(request):
    return render(request,"userlogin.html",{})

def loginvalidate(request):
    if(request.method=="POST"):
        uname = request.POST.get("uname")
        pwd = request.POST.get("pwd")        
        result = custinfo.objects.filter(cmail=uname,cpass=pwd)
        if(result != None):
            request.session["cmail"]=uname
            return redirect(demo)
        else:
            return redirect(login)

def showCust(request):
    custs = custinfo.objects.all()
    return render(request, "custList.html", {"custs":custs})

###############################Equipments#########################################

def strengthProd(request):
    strenprod = strengthprod.objects.all()
    return render(request, "strengthproducts.html", {"stren":strenprod})


################################Cart#############################################
def addtocart(request,id):  
    #Cart.objects.all().delete()     
    user = custinfo.objects.get(uname=request.session["uname"])
    #query returns 1 record
    prod = strengthProd.objects.get(id=id)    
    data = Cart.objects.filter(user=user,prod=prod)
    #Item is not present in cart
    if(data.count()==0):
        mycart = Cart()    
        mycart.user = user
        mycart.prod = prod
        mycart.save()
    return redirect(strengthProd)

def showcart(request):
    user = custinfo.objects.get(uname=request.session["uname"])
    cart_items = Cart.objects.filter(user=user.id)
    prods = []    
    total = 0
    for c in cart_items:
        c1 = strengthprod.objects.get(id=c.strengthprod.id)
        total = total + c1.stprodprice
        prods.append(c1)
    
    request.session["total"] = total
    print(request.session["total"])
    return render(request,"cart.html",{"emps" : prods,"total":total})

