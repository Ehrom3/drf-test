from rest_framework import generics
from .models import Category, Dishes, Order
from .serializers import CategorySerializer, DishesSerializer, OrderSerializer
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny

# list-create ----------------------------------------
class DishesListView(generics.ListAPIView):
    queryset = Dishes.objects.all()
    serializer_class = DishesSerializer
    permission_classes = [AllowAny]

class DishesCreateView(generics.CreateAPIView):
    queryset = Dishes.objects.all()
    serializer_class = DishesSerializer
    

class OrderListCreateView(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    
class CategoryListCreateView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    
# detail-----------------------------------------------
class DishesDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Dishes.objects.all()
    serializer_class = DishesSerializer

class OrderDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    
class CategoryDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer 


    
    


