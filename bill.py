from django.urls import path
from ..views.bill import *
billURL=[
    path('viewBill/',viewBill,name="viewBill"),
    path('addBill/',addBill,name="addBill"),  
    path('updateBill/<id>',updateBill,name="updateBill"), 
    path('deleteBill/<id>',deleteBill,name="deleteBill"), 
]