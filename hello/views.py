from django.shortcuts import render
from hello.models import Shop


# 控制
# Create your views here
# views 调用model
#
def hello(request):
    # select * from shop
    shop = Shop.objects.all().first()
    # model层和template桥梁
    # template
    context = {'shop': shop}
    return render(request, 'users.html', context)
