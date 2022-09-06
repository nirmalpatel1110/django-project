from django.shortcuts import get_object_or_404,render,redirect
from ..models import billModel
from django.shortcuts import render
#from ..models import Category as CategoryForm
from ..forms.Bill_form import BillForm
#from ..models import Category

def viewBill(request):
    context={}
    context["Bills"]=billModel.objects.all()
    return render(request, "Bill/view.html",context)

def addBill(request):
    context={}
    form=BillForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect( "viewBill")
    context['form']=form
    return render(request,"Bill/add.html",context)

def updateBill(request,id):
    context={}
    obj=get_object_or_404(billModel,id=id)
    form=BillForm(request.POST or None,instance=obj)
    if form.is_valid():
        form.save()
        return redirect("viewBill")
    context["form"]=form
    return render(request,"Bill/edit.html",context)

def deleteBill(request,id):
    context={}
    obj=get_object_or_404(billModel,id=id)
    if request.method=="GET":
        obj.delete()
        return redirect("viewCategory")
    return render(request,"category/view.html",context)