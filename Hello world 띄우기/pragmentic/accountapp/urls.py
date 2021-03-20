from django.urls import path

from accountapp.views import hello_world

app_name = "accountapp"

'''
"127.0.0.1:8000/account/hello_world"가 너무 기니까
나중에는 "accountapp:hello_world" (어카운트앱에 있는 헬로월드로 가라) 로 쓴다
'''


urlpatterns = [
    path('hello_world/', hello_world, name='hello_world')
]