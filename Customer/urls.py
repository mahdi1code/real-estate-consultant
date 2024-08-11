from django.urls import path

from . import views


urlpatterns = [
    path('',views.Gotocontact,name=""),
    path('gotoindex',views.gotoindex,name="ویلا"),
    path('gotoProperties',views.gotoProperties,name="خرید ملک"),
    path('Register',views.Register,name="ثبت نام و اضافه شدن"),
    path('Gotepropertydetails',views.Gotepropertydetails,name="صفحه کاربران ثبت شده"),
    path('EditUser/<int:id>',views.EditUser,name="ویرایش کاربران"),
    path('SaveEditUser',views.SaveEditUser,name="ثبت ویرایش کاربران"),
    path('DeleteUser/<int:id>',views.DeleteUser,name="حذف کاربران"),
    path('Savecustomermessage',views.Savecustomermessage,name="ثبت پیام مشتریان"),
    path('Editcustomermessage/<int:id>',views.Editcustomermessage,name=" ویرایش پیام مشتریان"),
    path('SaveEditcustomermessage',views.SaveEditcustomermessage,name="ثبت ویرایش پیام مشتریان"),
    path('Deletecustomermessage/<int:id>',views.Deletecustomermessage,name="حذف پیام مشتری"),
    path('CheckRegister',views.CheckRegister,name="چک کردن ثبت شدن کابر"),
    path('GotoLoginPage',views.GotoLoginPage,name="ورود به صفحه"),
    path('Checkout',views.Checkout,name="چک کردن ورود کاربر"),
    path('Logoutuser',views.Logoutuser,name="خارج کردن کاربر"),
]
