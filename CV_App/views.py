import profile
from django.shortcuts import render
from .models import Profile
from django.http import HttpResponse
from django.template import loader
import pdfkit


def input(request):
    if request.method=="POST":
        name=request.POST.get("name","")
        phone=request.POST.get("phone","")
        email=request.POST.get("email","")
        school=request.POST.get("school","")
        degree=request.POST.get("degree","")
        univercity=request.POST.get("univercity","")
        skill=request.POST.get("skill","")
        about_you=request.POST.get("about_you","")
        Previous_works=request.POST.get("Previous_works","")

        profile = Profile(name=name,phone=phone,
        email=email,school=school,
        degree=degree,univercity=univercity,
        skill=skill,about_you=about_you,Previous_works=Previous_works)
        profile.save()

    return render(request, "input.html");

def cv(request,id):
    user_profile=Profile.objects.get(id=id)
    template = loader.get_template("cv.html")
    html = template.render({'user_profile':user_profile})
    options = {
        'page-size':'Letter',
        'encoding':'UTF-8'
    }
    pdf = pdfkit.from_string(html,False,options)
    response = HttpResponse(pdf,content_type='application/pdf')
    response['Content-Disposition']='attachments'
    return response

