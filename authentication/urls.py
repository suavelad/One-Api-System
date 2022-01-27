from django.urls import path
from .apis import  UserViewSet,CreateUserView,LoginView
        # UpdatePasswordView,OTPVerificationView,ResetPasswordEmailView,ConfirmResetTokenView,\
        # ResetPasswordView,GetInvitedMembersView,InviteMemberViewSet,GetUserView
from rest_framework.routers import DefaultRouter
 
router = DefaultRouter()


router.register('users',UserViewSet, 'users')

urlpatterns = router.urls

urlpatterns += [
    path('create/user/', CreateUserView.as_view(), name="create-member"),
    path('login/',LoginView.as_view(), name='login'),
    # path('change/password/',UpdatePasswordView.as_view(), name='change-password'),
    # path('confirm/otp/',OTPVerificationView.as_view(), name='confirm-otp'),
    # path('reset-password/code/',ResetPasswordEmailView.as_view(), name='reset-password-link'),
    # path('reset-password/verify-code/',ConfirmResetTokenView.as_view(), name='reset-password-verify-code'),
    # path('reset-password/',ResetPasswordView.as_view(), name='reset-password'),
    
    
    
    
    
]