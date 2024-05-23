from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from django.views.generic import TemplateView
import datetime
from .models import AttendanceRecord,userModel

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
        for name in names:
            res = AttendanceRecord.objects.filter(name_id=name.id,date__lte=upper_range,date__gte=lower_range).order_by("date")
            past_dates,future_dates = [i.status.status for i in res if i.date < today],[i.status.status for i in res if i.date > today]
            print("past dates",past_dates)
            print("future dates",future_dates)
            data.append({"employee":name,"today":today,"past_status":past_dates,"future_status":future_dates})
            
        print(names)
        context = {
        "past_dates":[ datetime.date.today() - datetime.timedelta(days=i) for i in range(1,6)] ,
        "today":datetime.date.today(),
        "future_dates":[ datetime.date.today() + datetime.timedelta(days=i) for i in range(1,6)],
        "data":data
        }
        print(data)
        return context
    

    # def editEntries(request):


    
