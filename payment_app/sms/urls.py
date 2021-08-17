from django.urls import path
from . import views



urlpatterns = [
    path('', views.index , name="index" ),
    path('kyc', views.home, name="home"),
    path('upload/<int:id>/<str:type>', views.upload, name="upload"),
    path('display/<int:email>', views.display, name="display"),
    path('softApproved', views.softApproved, name="softApproved"),
    path('check/<int:id>', views.check, name="check"),
    path('reupload/<int:id>/<str:type>', views.reupload, name="reupload"),
    path('otp/<int:id>', views.otp, name="otp"),
    path('checkotp/<int:id>/<int:no>', views.checkotp, name="checkotp"),
    path('list', views.list, name="list"),
    path('accounts/logout', views.logout, name="logout"),
    path('statCheck/<int:id>', views.statCheck, name="statCheck"),
    path('statUpload/<int:id>', views.statUpload, name="statUpload"),
    path('statUploadCheck/<int:id>', views.statUploadCheck, name="statUploadCheck"),
    path('api/all', views.customerList.as_view(), name="customerList"),
    path('api/statements/<int:id>', views.statementsView.as_view(), name="statementsView"),
    path('test/', views.test, name="test"),

]

