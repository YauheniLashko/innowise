from django.urls import path
from rest_framework_simplejwt.views import (TokenObtainPairView,
                                            TokenRefreshView, TokenVerifyView)

from .views import (Home, LoginUser, MessageTextView, MessageUpdateView,
                    RegisterUser, TicketAPIDestroy, TicketAPIList,
                    TicketUpdateStatusView, logout_user)

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('register/', RegisterUser.as_view(), name='signup'),
    path('login/', LoginUser.as_view(), name='login'),
    path('logout/', logout_user, name='logout'),
    path('api/v1/ticket/', TicketAPIList.as_view()),
    path('api/v1/update/status/<int:pk>/', TicketUpdateStatusView.as_view(), name='update_status'),
    path('api/v1/ticketdelete/<int:pk>/', TicketAPIDestroy.as_view()),
    path('api/v1/updatemsg/<int:pk>/', MessageUpdateView.as_view(), name='update_answer'),
    path('api/v1/ticmsg/', MessageTextView.as_view(), name="ticket_message"),
    path('api/v1/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/v1/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/v1/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
]
