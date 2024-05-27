from django.shortcuts import render,get_object_or_404,redirect
from django.http import HttpResponseRedirect
from django.views.generic import TemplateView
import datetime
from dateutil import parser
from .models import AttendanceRecord,userModel,statusclass
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate,login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import logout

# Create your views here.

class Mainview(LoginRequiredMixin,TemplateView):
    login_url = "app_V2:login"
    redirect_field_name = None
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
        present_status = statusclass.objects.filter(status="present")[0]
        for name in names:
            # temp = today
            today_record = AttendanceRecord.objects.get_or_create(name_id=name.id,date=today,defaults={'name_id':name.id,'date':today,'status': present_status})
            for i in range(1,6):
                past_record = AttendanceRecord.objects.get_or_create(name_id=name.id,date=today - datetime.timedelta(days=i),defaults={'name_id':name.id,'date':today-datetime.timedelta(days=i),'status': present_status})
                future_record = AttendanceRecord.objects.get_or_create(name_id=name.id,date=today + datetime.timedelta(days=i),defaults={'name_id':name.id,'date':today+datetime.timedelta(days=i),'status': present_status})
            res = AttendanceRecord.objects.filter(name_id=name.id,date__lte=upper_range,date__gte=lower_range).order_by("date")
            past_dates,future_dates = [{"date":i.date,"status":i.status.status} for i in res if i.date < today],[{"date":i.date,"status":i.status.status} for i in res if i.date > today]
            today_status = None
            for i in res:
                if i.date == today:
                    today_status = i.status.status


            data.append({"employee":name,"today":today_status,"past_status":past_dates,"future_status":future_dates})
            

        context = {
        "past_dates":[ datetime.date.today() - datetime.timedelta(days=i) for i in range(5,0,-1)] ,
        "today":datetime.date.today(),
        "future_dates":[ datetime.date.today() + datetime.timedelta(days=i) for i in range(1,6)],
        "data":data,
        "options":options,
        "user":self.request.user,
        }
        # print(data)
        return context
    
    def editEntries(request):
        if request.method == "POST":
            name,date,status = request.POST.get("name"),request.POST.get("date"),request.POST.get("status")
            date = parser.parse(date)
            name_id = userModel.objects.get(name=name).id
            status = statusclass.objects.get(status=status)
            record = AttendanceRecord.objects.get(name=name_id,date=date)
            record.status=status
            record.save()
            return redirect("app_V2:home")
        
    


class LoginView(TemplateView):
    template_name = "login.html"
    def post(self,request):
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request,username=username,password=password)
        if user is not None:
            form = login(request,user)
            return redirect("app_V2:home")
                
            
        return render(request=request,template_name=self.template_name)


class RegisterView(TemplateView):
    template_name = "register.html"
    def post(self,request):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect("app_V2:login")   

        else:
            return render(request=request,template_name=self.template_name,context={"error":form.errors})
        

class LogoutView(TemplateView):
    def get(self,request):
        logout(request)
        return redirect("app_V2:login")

    
