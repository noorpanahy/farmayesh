from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.renderers import JSONRenderer, TemplateHTMLRenderer



from Farmayesh_app.models import Registration,Resturant,Catagure,Food,OrderItem,Order,Administrator
from Farmayesh_app.serializers import RegistrationSerializer,ResturantSerializer,CatagureSerializer,FoodSerializer,OrderItemSerializer,OrderSerializer,AdministratorSerializer



@api_view(['POST'])
def apioverview(request):
    api_urls = {
        'List': '/tast-list/',
        'Detail View' : '/task-detail/<str:pk>/',
        'Create' : '/task-Create/',
        'Update' : '/task-Update/<str:pk>/',
        'Delete' : '/task-Delete/<str:pk>/'
    }

    return Response(api_urls)

# Create your views here.

@csrf_exempt
def RegistrationApi(request,id=0):
    if request.method=='GET':
        registration = Registration.objects.all()
        registration_serializer = RegistrationSerializer(registration,many=True)
        return JsonResponse(registration_serializer.data,safe=False)
    elif request.method=='POST':
        registration_data = JSONParser().parse(request)
        registration_serializer = RegistrationSerializer(data=registration_data)
        if registration_serializer.is_valid():
            registration_serializer.save()
            return JsonResponse("Added successfully!!" , safe=False)
        return JsonResponse("failed to Add.",safe=False)
    elif request.method=='PUT':
        registration_date = JSONParser().parse(request)
        registration = Registration.objects.get(CustomerID=registration_date['CustomerID'])
        registration_serializer = RegistrationSerializer(registration,data=registration_date)
        if registration_serializer.is_valid():
            registration_serializer.save()
            return JsonResponse("Updated successfully!",safe=False)
        return JsonResponse("Failed to Update,",safe=False)

    elif request.method=="DELETE":
        registration = Registration.objects.get(CustomerID=id)
        registration.delete()
        return JsonResponse("Deleted Successfully!",safe=False)

@csrf_exempt
def ResturantApi(request,id=0):
    if request.method=='GET':
        resturant = Resturant.objects.all()
        resturant_serializer = ResturantSerializer(resturant,many=True)
        return JsonResponse(resturant_serializer.data,safe=False)
    elif request.method=='POST':
        resturant_data = JSONParser().parse(request)
        resturant_serializer = ResturantSerializer(data=resturant_data)
        if resturant_serializer.is_valid():
            resturant_serializer.save()
            return JsonResponse("Added successfully!!" , safe=False)
        return JsonResponse("failed to Add.",safe=False)
    elif request.method=='PUT':
        resturant_date = JSONParser().parse(request)
        resturant = Resturant.objects.get(CustomerID=resturant_date['CustomerID'])
        resturant_serializer = ResturantSerializer(resturant,data=resturant_date)
        if resturant_serializer.is_valid():
            resturant_serializer.save()
            return JsonResponse("Updated successfully!",safe=False)
        return JsonResponse("Failed to Update,",safe=False)

@csrf_exempt
def CatagureApi(request,id=0):
    if request.method=='GET':
        catagure = Catagure.objects.all()
        catagure_serializer = CatagureSerializer(catagure,many=True)
        return JsonResponse(catagure_serializer.data,safe=False)
    elif request.method=='POST':
        catagure_data = JSONParser().parse(request)
        catagure_serializer = CatagureSerializer(data=catagure_data)
        if catagure_serializer.is_valid():
            catagure_serializer.save()
            return JsonResponse("Added successfully!!" , safe=False)
        return JsonResponse("failed to Add.",safe=False)
    elif request.method=='PUT':
        catagure_date = JSONParser().parse(request)
        catagure = Catagure.objects.get(CustomerID=catagure_date['CustomerID'])
        catagure_serializer = CatagureSerializer(catagure,data=catagure_date)
        if catagure_serializer.is_valid():
            catagure_serializer.save()
            return JsonResponse("Updated successfully!",safe=False)
        return JsonResponse("Failed to Update,",safe=False)

@csrf_exempt
def FoodApi(request,id=0):
    if request.method=='GET':
        food = Food.objects.all()
        food_serializer = FoodSerializer(food,many=True)
        return JsonResponse(food_serializer.data,safe=False)
    elif request.method=='POST':
        food_data = JSONParser().parse(request)
        food_serializer = FoodSerializer(data=Food_data)
        if food_serializer.is_valid():
            food_serializer.save()
            return JsonResponse("Added successfully!!" , safe=False)
        return JsonResponse("failed to Add.",safe=False)
    elif request.method=='PUT':
        food_date = JSONParser().parse(request)
        food = Food.objects.get(CustomerID=food_date['CustomerID'])
        food_serializer = FoodSerializer(food,data=food_date)
        if food_serializer.is_valid():
            food_serializer.save()
            return JsonResponse("Updated successfully!",safe=False)
        return JsonResponse("Failed to Update,",safe=False)

@csrf_exempt
def OrderItemApi(request,id=0):
    if request.method=='GET':
        orderItem = OrderItem.objects.all()
        orderItem_serializer = OrderItemSerializer(orderItem,many=True)
        return JsonResponse(orderItem_serializer.data,safe=False)
    elif request.method=='POST':
        orderItem_data = JSONParser().parse(request)
        orderItem_serializer = OrderItemSerializer(data=orderItem_data)
        if orderItem_serializer.is_valid():
            orderItem_serializer.save()
            return JsonResponse("Added successfully!!" , safe=False)
        return JsonResponse("failed to Add.",safe=False)
    elif request.method=='PUT':
        orderItem_date = JSONParser().parse(request)
        orderItem = OrderItem.objects.get(CustomerID=orderItem_date['CustomerID'])
        orderItem_serializer = OrderItemSerializer(orderItem,data=orderItem_date)
        if orderItem_serializer.is_valid():
            orderItem_serializer.save()
            return JsonResponse("Updated successfully!",safe=False)
        return JsonResponse("Failed to Update,",safe=False)

    elif request.method=="DELETE":
        orderItem = OrderItem.objects.get(CustomerID=id)
        orderItem.delete()
        return JsonResponse("Deleted Successfully!",safe=False)

@csrf_exempt
def OrderApi(request,id=0):
    if request.method=='GET':
        order = Order.objects.all()
        order_serializer = OrderSerializer(order,many=True)
        return JsonResponse(order_serializer.data,safe=False)
    elif request.method=='POST':
        order_data = JSONParser().parse(request)
        order_serializer = OrderSerializer(data=order_data)
        if order_serializer.is_valid():
            order_serializer.save()
            return JsonResponse("Added successfully!!" , safe=False)
        return JsonResponse("failed to Add.",safe=False)
    elif request.method=='PUT':
        order_date = JSONParser().parse(request)
        order = Order.objects.get(CustomerID=order_date['CustomerID'])
        order_serializer = OrderSerializer(order,data=order_date)
        if order_serializer.is_valid():
            order_serializer.save()
            return JsonResponse("Updated successfully!",safe=False)
        return JsonResponse("Failed to Update,",safe=False)

    elif request.method=="DELETE":
        order = Order.objects.get(CustomerID=id)
        order.delete()
        return JsonResponse("Deleted Successfully!",safe=False)

@csrf_exempt
def AdministratorApi(request,id=0):
    if request.method=='GET':
        administrator = Administrator.objects.all()
        administrator_serializer = AdministratorSerializer(administrator,many=True)
        return JsonResponse(administrator_serializer.data,safe=False)
