from rest_framework import generics
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.permissions import IsAuthenticated
from .models import Category, Dishes, Order
from .serializers import CategorySerializer, DishesSerializer, OrderSerializer
from .permissions import IsChefOrReadOnly, IsAdminOrReadOnly


class DishesListView(generics.ListAPIView):
    queryset = Dishes.objects.all().order_by('id')
    serializer_class = DishesSerializer
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['name', 'description', 'category__title']
    ordering_fields = ['price', 'name', 'id']

    def get_queryset(self):
        queryset = super().get_queryset()
        category = self.request.query_params.get('category')
        min_price = self.request.query_params.get('min_price')
        max_price = self.request.query_params.get('max_price')

        if category:
            queryset = queryset.filter(category_id=category)
        if min_price:
            queryset = queryset.filter(price__gte=min_price)
        if max_price:
            queryset = queryset.filter(price__lte=max_price)
        return queryset


class DishesCreateView(generics.CreateAPIView):
    queryset = Dishes.objects.all()
    serializer_class = DishesSerializer
    permission_classes = [IsChefOrReadOnly]


class DishesDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Dishes.objects.all()
    serializer_class = DishesSerializer
    permission_classes = [IsChefOrReadOnly]


class OrderListCreateView(generics.ListCreateAPIView):
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        if user.is_staff or getattr(getattr(user, 'profile', None), 'role', '') == 'chef':
            return Order.objects.all().order_by('id')
        return Order.objects.filter(user=user).order_by('id')

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class OrderDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        if user.is_staff or getattr(getattr(user, 'profile', None), 'role', '') == 'chef':
            return Order.objects.all()
        return Order.objects.filter(user=user)


class CategoryListCreateView(generics.ListCreateAPIView):
    queryset = Category.objects.all().order_by('id')
    serializer_class = CategorySerializer
    permission_classes = [IsAdminOrReadOnly]


class CategoryDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAdminOrReadOnly]


    
    


