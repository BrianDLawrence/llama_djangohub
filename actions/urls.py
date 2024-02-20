from django.urls import path
from actions.views import ActionsViewSet

urlpatterns = [
    path('actions', ActionsViewSet.as_view({
        'get':'get_all',
        'post':'create'
    })),
    path('actions/<str:pk>', ActionsViewSet.as_view({
        'get':'retrieve',
        'put':'update',
        'delete':'destroy'
    })),
    path('send/<str:pk>', ActionsViewSet.as_view({
        'post':'send'
    })),
]
