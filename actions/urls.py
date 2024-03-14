from django.urls import path
from actions.views import ActionsViewSet, ContextViewSet

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
    path('get_amount_unanswered_messages', ActionsViewSet.as_view({
        'get':'get_amount_unanswered_messages'
    })),
    path('context', ContextViewSet.as_view({
        'get':'get_all',
        'post':'create'
    })),
]
