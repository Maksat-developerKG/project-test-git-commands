from app_shop.views import ProductViewSet, CategoryViewSet, SubCategoryViewSet
from rest_framework import routers

router = routers.SimpleRouter()

router.register('product', ProductViewSet)
router.register('category', CategoryViewSet)
router.register('sub-category', SubCategoryViewSet)

urlpatterns = []

urlpatterns += router.urls

