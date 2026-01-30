from django.contrib import admin
from django.urls import path
from assessment.views import home, test_detail
from assessment.views import my_results


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home),
    path('test/<int:test_id>/', test_detail),
    path("results/", my_results),

]
