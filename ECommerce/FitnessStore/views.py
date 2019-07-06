from django.shortcuts import render, HttpResponse, redirect
from FitnessStore.models import Person, custinfo, strengthprod
from FitnessStore.forms import PersonForm, custregister

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
        #p = Person.objects.get(id=id)
        #if(p==None):
        p = Person(id,pnames,plocation)
        p.save()
        '''else:
            return HttpResponse("Id Already Exist, Please try another one")
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


def custRegister(request):
    if(request.method=="GET"):
        return render(request,"usersignin.html",{})
    else:
        cid = request.POST['cid']
        cfname = request.POST["cfname"]
        clname = request.POST["clname"]
        cmail = request.POST["cmail"]
        cpass = request.POST["cpass"]
        cdob = request.POST["cdob"]
        ccontact = request.POST["ccontact"]
        cgender = request.POST["cgender"]
        cust = custinfo(cid,cfname,clname,cmail,cpass,cdob,ccontact,cgender)
        cust.save()
        return redirect(showCust)

def showCust(request):
    custs = custinfo.objects.all()
    return render(request, "custList.html", {"custs":custs})

###############################Equipments#########################################

def strengthProd(request):
    strenprod = strengthprod.objects.all()
    return render(request, "strengthproducts.html", {"stren":strenprod})


