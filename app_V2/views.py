from django.shortcuts import render,get_object_or_404,redirect
from django.http import HttpResponse
from django.views.generic import TemplateView
import datetime
from .models import AttendanceRecord,userModel,statusclass

# Create your views here.

class Mainview(TemplateView):
    template_name="home.html"
    # extra_context = {
    #     "past_dates":[ datetime.date.today() - datetime.timedelta(days=i) for i in range(1,6)] ,
    #     "today":datetime.date.today(),
    #     "future_dates":[ datetime.date.today() + datetime.timedelta(days=i) for i in range(1,6)],
    #     "data":[
    #         {"employee":"vinay","past_status":[True,False,True,False,True],"today":False,"future_status":[None,None,None,None,None]},
    #         {"employee":"mayur","past_status":[True,False,True,False,True],"today":False,"future_status":[True,False,True,False,True]},
    #         {"employee":"vinay","past_status":[True,False,True,False,True],"today":False,"future_status":[True,False,True,False,True]},
    #         {"employee":"mayur","past_status":[True,False,True,False,True],"today":False,"future_status":[True,False,True,False,True]},
    #     ]
    # }
    def get_context_data(self,**kwargs):
        today = datetime.date.today()
        lower_range,upper_range = today - datetime.timedelta(days=5),today + datetime.timedelta(days=5)
        # data = AttendanceRecord.objects.filter(date__lte=upper_range,date__gte=lower_range).values()
        names = userModel.objects.all().distinct()
        data = []
        options = statusclass.objects.all().distinct()
        for name in names:
            res = AttendanceRecord.objects.filter(name_id=name.id,date__lte=upper_range,date__gte=lower_range).order_by("date")
            past_dates,future_dates = [{"date":i.date,"status":i.status.status} for i in res if i.date < today],[{"date":i.date,"status":i.status.status} for i in res if i.date > today]
            # print("past dates",past_dates)
            # print("future dates",future_dates)
            today_status = None
            for i in res:
                if i.date == today:
                    today_status = i.status.status

            data.append({"employee":name,"today":today_status,"past_status":past_dates,"future_status":future_dates})
            
        # print(names)
        context = {
        "past_dates":[ datetime.date.today() - datetime.timedelta(days=i) for i in range(5,0,-1)] ,
        "today":datetime.date.today(),
        "future_dates":[ datetime.date.today() + datetime.timedelta(days=i) for i in range(1,6)],
        "data":data,
        "options":options
        }
        # print(data)
        return context
    

    def editEntries(request):
        if request.method == "POST":
            name,date,status = request.POST.get("name"),request.POST.get("date"),request.POST.get("status")
            record = AttendanceRecord.objects.get(name=name,date=date)
            print(record) 
            return redirect("app_V2:home")


    
