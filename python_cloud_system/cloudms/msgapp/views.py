import os

from django.shortcuts import render

# Create your views here.
from datetime import datetime
from django.http import HttpResponse, JsonResponse, FileResponse


# Create your views here.
def msgproc(request):
    datalist = []
    if request.method == "POST":
        userA = request.POST.get("userA", None)
        userB = request.POST.get("userB", None)
        msg = request.POST.get("msg", None)
        time = datetime.now()
        with open('msgdata.txt', 'a+') as f:
            f.write("{}--{}--{}--{}--\n".format(userB, userA, \
                                                msg, time.strftime("%Y-%m-%d %H:%M:%S")))
    if request.method == "GET":
        userC = request.GET.get("userC", None)
        if userC != None:
            with open("msgdata.txt", "r") as f:
                cnt = 0
                for line in f:
                    linedata = line.split('--')
                    if linedata[0] == userC:
                        cnt = cnt + 1
                        d = {"userA": linedata[1], "msg": linedata[2] \
                            , "time": linedata[3]}
                        datalist.append(d)
                    if cnt >= 10:
                        break
    return render(request, "MsgSingleWeb.html", {"data": datalist})


def homeproc(request):
    responce = HttpResponse()
    responce.write("<h1>这是首页，具体功能请访问<a href='./msggate'>这里</a></h1>")
    responce.write("<h1>这是第二行</h1>")
    return responce

def homeproc1(request):
    responce = JsonResponse({'key1': 'value1'})
    return responce

def homeproc2(request):
    cwd = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    response = FileResponse(open(cwd + '/msgapp/templates/PyLogo.png', "rb"))
    response['Content-Type'] = 'application/octet-stream'
    response['Content-Disposition'] = 'attachment;filename="pylogo.png"'
    return response