from .models import Product
from .serializers import ProductSerializer
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET'])#It defines the method the user is allowed to do in this route of API
def getRoutes(request):
	routes=[
	'(GET) /',
	'(GET) /products/',
	'(GET) /products/:id',
	'(DELETE) /delete/:id',
	'(POST) /post/',
	'(PUT) /put/:pk',
	]
	return Response(routes,status=200)#It returns the routes of the API

@api_view(['GET'])#It defines the method the user is allowed to do in this route of API
def ProductList(request):
    queryset = Product.objects.all()#It returns all the rooms of DB
    dataSerialized = ProductSerializer(queryset,many=True)#many=True => Saying that we want to serialize multiple objects | many=False => Saying that we want to serialize only one object 
    return Response(dataSerialized.data,status=200)#Return the JSON data

@api_view(['GET'])#It defines the method the user is allowed to do in this route of API
def ProductDetail(request,pk):
    try:#Try find the data
        queryset = Product.objects.get(id=pk)#It tries find the Product...
    except:#If it was no found
        return Response(status=400)#Return 400
    dataSerialized = ProductSerializer(queryset,many=False)#many=True => Saying that we want to serialize multiple objects | many=False => Saying that we want to serialize only one object 
    return Response(dataSerialized.data,status=200)#Return the JSON data

@api_view(['DELETE','GET'])#It defines the method the user is allowed to do in this route of API
def deleteProduct(request,pk):
	try:#Try find the data
		product = Product.objects.get(id=pk)#It returns all the rooms of DB
	except:#if it is not registered...
		return Response(status=400)#Return 400
	dataSerialized = ProductSerializer(product,many=False)#many=True => Saying that we want to serialize multiple objects | many=False => Saying that we want to serialize only one object 
	if request.method=="GET":#If the method is GET
		return Response(dataSerialized.data,status=200)#Return the JSON data
	product.delete()#Delete product
	return Response(dataSerialized.data,status=200)#Return 200
@api_view(['PUT','GET'])#It defines the method the user is allowed to do in this route of API
def putProduct(request,pk):
	if request.method=="GET":
		routes="This is the PUT route!"
		return Response(routes, status=200)#It returns the routes of the API
	try:#Try find the data
		product = Product.objects.get(id=pk)#It returns all the rooms of DB
	except:#if it is not registered...
		return Response(status=400)#Return 400
	name, price, description=request.data["name"], request.data["price"], request.data['description']
	product.name=request.data["name"]
	product.price=price
	product.description=request.data["description"]
	product.save()
	return Response(status=200)#Return 400
@api_view(['POST','GET'])#It defines the method the user is allowed to do in this route of API
def postProduct(request):
	if request.method=="GET":
		routes="This is the POST route!"
		return Response(routes, status=200)#It returns the routes of the API
	name, price, description=request.data["name"], request.data["price"], request.data['description']
	try:
		product=Product.objects.create(name=name,price=price,description=description)
		return Response(status=200)#Return 100
	except:
		return Response(status=400)#Return 400