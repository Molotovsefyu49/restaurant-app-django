from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.MenuList.as_view(), name='home'),
    path('item/<int:pk>/', views.MenuItemDetail.as_view(), name="menu_item")
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
