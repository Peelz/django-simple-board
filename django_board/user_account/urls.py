from django.urls import path, include

urlpatterns = [
    path('/', include('user_account.urls'))
]
