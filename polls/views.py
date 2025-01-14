import datetime
from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from django.http import JsonResponse
from django.core import serializers
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.staticfiles.storage import staticfiles_storage
from django.forms import model_to_dict
from pytz import timezone

from datetime import date, timedelta

from polls.forms import PetitionForm

from .models import Staff, Event, Program, News, Mission, DailyDose, Director, Officer, Donor, Contact, News, Signee

from django.core.mail import send_mail
from django.template import loader
from django.views.generic import ListView
from django.shortcuts import redirect


from django.utils.safestring import mark_safe

from django.db.models import Q
import json
import requests

from django.core.serializers.json import DjangoJSONEncoder
from django.db.models.fields.files import ImageFieldFile

def million(request):
    return redirect("https://secure.givelively.org/donate/ccee/1-million-reasons-to-love-economics")

class ExtendedEncoder(DjangoJSONEncoder):
    def default(self, o):
        if isinstance(o, ImageFieldFile):
            return str(o)
        else:
            return super().default(o)


def education_month(request):
    signees = Signee.objects.all()

    if request.method == 'POST':
        form = PetitionForm(request.POST)
        if form.is_valid() and form.cleaned_data['your_name'] not in signees:
            Signee.objects.create_signee(form.cleaned_data['your_name'], form.cleaned_data['email'])
            return HttpResponseRedirect('/econedmonth#list')
    else:
        form = PetitionForm()
    

    context = {
        'form': form,
        'signees': signees
    }
    return render(request, "polls/education_month.html", context)

def mail_contact_form(request):

    email_address = request.POST['email_address']
    content = request.POST['content']
    # send_mail(
    #     'Contact form submission',
    #     content,
    #     email_address,
    #     ['contact@ccee.org',
    #     'jcost035@fiu.edu'],
    #     fail_silently=False,
    # )
    Contact.objects.create(email_address=email_address, content=content)


    return HttpResponseRedirect('/')

def subscribe(request):
    
    email_address =  request.POST['address']
    data = {"email_address" : email_address, "first_name": "jorge", "last_name" : "costa" }
    if("@" in email_address and email_address != ''):
        json_data = json.dumps(data)
        # payload = {'json_payload': json_data, 'apikey': '65905886-48af-477f-b935-de5536f22764'}
        # r = requests.get('https://api.cc.email/v3/account/emails', data=payload)
        
        url = 'https://api.cc.email/v3/contacts'
        payload = json.dumps(data)
        headers = {'Content-Type': 'application/json', 'Authorization' : 'Bearer 3af06171-02ee-4fa9-97e9-f36f3924c254', "cache-control": "no-cache"}
        r = requests.post(url, data=payload, headers=headers)
        print(r.text)

    return HttpResponseRedirect('/')


def gala_2022(request):
    return render(request, "polls/gala-2022.html")

def gala_2024(request):
    return render(request, "polls/gala-2024.html")

def caset(request):

    # program = Program.objects.filter(name__icontains="Economics Teacher Certification")
    # event_list = Event.objects.filter(program__icontains="Economics Teacher Certification")
    
    # context = {
    #     "program": program[0],
    #     "event_list": event_list
    # }

    #return render(request, "polls/caset.html", context)
    return redirect("https://www.caset.org/economics-teacher-certification-program")

def donors(request):
    donor_list = Donor.objects.all()

    context = {
        "donor_list" : donor_list,
    }
    return render(request, "polls/donors.html", context)

def news_article(request, article_url):
    news = News.objects.filter(title__exact=article_url)
    pdf = news[0].pdf
    hide_banner = news[0].hide_banner
    articles_list = News.objects.order_by('-date')
    
    context = {
        "news": news[0],
        "first_article": articles_list[0],
        "second_article": articles_list[1],
        "third_article": articles_list[2],
        "hide_banner": hide_banner,
        "pdf": pdf
    }
    
    return render(request, "polls/article.html", context)

def dose_article(request, article_url):
    dose = DailyDose.objects.filter(topic__exact=article_url)
    dose_list = DailyDose.objects.order_by('-date')
    
    context = {
        "dose": dose[0],
        "first_dose": dose_list[0],
        "second_dose": dose_list[1],
        "third_dose": dose_list[2],
    }
    
    return render(request, "polls/daily-dose-article.html", context)

def daily_dose(request):
    return render(request, "polls/daily-dose.html")

def map(request):
    return render(request, "polls/map.html")

def report(request):
    return render(request, "polls/report.html")

def report_2021(request):
    return render(request, "polls/report-2021.html")

def report_2022(request):
    return render(request, "polls/report-2022.html")

def report_2023(request):
    return render(request, "polls/report-2023.html")

def contact(request):
    return render(request, "polls/contact.html")

def donate(request):
    return render(request, "polls/donate.html")

def volunteer(request):
    return render(request, "polls/volunteer.html")

def programs(request, prog_name):

    program = Program.objects.filter(name__icontains=prog_name)
    programs_list = Program.objects.all()
    caset_model = Program()
    program_thumbs = Program.objects.exclude(name__iexact=prog_name).exclude(name__iexact='National Economics Challenge').exclude(name__iexact='Federal Reserve Institute')
    event_list = Event.objects.filter(program__icontains=prog_name)
    
    context = {
        "program": program[0],
        "faq": program[0].faq["set"],
        "first_program": program_thumbs[0],
        "second_program": program_thumbs[1],
        "third_program": program_thumbs[2],
        "event_list": event_list
    }
    
    return render(request, "polls/programs.html", context)

def gala_redirect(request):
    response = redirect('https://aesbid.co/ELP/CCEEGALA23')
    return response

def smartpath_redirect(request):
    response = redirect('/programs/$martpath')
    return response

def caset_redirect(request):
    response = redirect('/programs/Economics Teacher Certification')
    return response

def ddoe_redirect(request):
    response = redirect('/daily-dose')
    return response

def pfc_redirect(request):
    response = redirect('/programs/Personal Finance Challenge')
    return response

def nec_redirect(request):
    response = redirect('/programs/National Economics Challenge')
    return response

def adviser_redirect(request):
    response = redirect("/programs/The Adviser's Contest")
    return response

def ffle_redirect(request):
    response = redirect("/programs/Family Financial Literacy Event")
    return response

def calendar_table(request):
    return render(request, "polls/calendar-table.html")

class Calendar(ListView):
    model = Event
    context_object_name = "events"
    
    template_name = "polls/calendar.html"
    paginate_by = 5

    def get_queryset(self):
        location_query = self.request.GET.get('q')
        if location_query == None:
            location_query = ''
        tags_query = self.request.GET.get('r')
        if tags_query == None:
            tags_query = ''
        
        return Event.objects.order_by("-date").filter(
            Q(location__icontains=location_query) , Q(tags__icontains=tags_query)
        )

def event_list(request):
    
    
    events_dict = Event.objects.order_by("date")
    event_list = []

    for event in events_dict:
        additional_fields = {}
        old_date = str(event.date)
        new_date = old_date[5:7] + '/' + old_date[8:10] + '/' + old_date[0:4]
        additional_fields['formatted_date'] = new_date

        if event.end_date is not None:
            old_end_date = str(event.end_date)
            new_end_date = old_end_date[5:7] + '/' + old_end_date[8:10] + '/' + old_end_date[0:4] 
            additional_fields['formatted_end_date'] = new_end_date
        else:
            additional_fields['formatted_end_date'] = None

        

        additional_fields['thumb_url'] = event.thumb_photo.url
        event_list.append({
            **additional_fields,
            **model_to_dict(event, exclude=['date', 'thumb_photo'])
        })
        
    #paginator = Paginator(event_list, 5) #show 10 objects per page
    #page_number = request.GET.get('page')
    #events = paginator.get_page(page_number)

    context = {
        "event_list": json.dumps(event_list),
    }
    return HttpResponse(json.dumps(event_list), content_type="application/json")

def news(request):
    return render(request, "polls/news.html")

def news_list(request):
    

    news_dict = News.objects.order_by("-date")

    news_list = []

    for news in news_dict:
        additional_fields = {}
        old_date = str(news.date)
        new_date = old_date[5:7] + '/' + old_date[8:10] + '/' + old_date[0:4]
        additional_fields['formatted_date'] = new_date
        additional_fields['thumb_url'] = news.thumb_photo.url
        news_list.append({
            **additional_fields,
            **model_to_dict(news, exclude=['date', 'thumb_photo', 'banner_photo', 'pdf'])
        })

        
    # news_list = serializers.serialize('json', news_list)

    #paginator = Paginator(event_list, 5) #show 10 objects per page
    #page_number = request.GET.get('page')
    #events = paginator.get_page(page_number)

    context = {
        "news_list": json.dumps(news_list),
    }
    return HttpResponse(json.dumps(news_list), content_type="application/json")

def dose_list(request, page_num=0):
    
    
    if page_num != 0:
        start = (page_num * 20) - 20
        end = (page_num * 20)
        dose_dict = DailyDose.objects.order_by("-date")[start:end]
    else:
        dose_dict = DailyDose.objects.order_by("-date")

    dose_list = []



    for dose in dose_dict:
        additional_fields = {}
        old_date = str(dose.date)
        new_date = old_date[5:7] + '/' + old_date[8:10] + '/' + old_date[0:4]
        additional_fields['formatted_date'] = new_date
        additional_fields['thumb_url'] = dose.banner_photo.url
        dose_list.append({
            **additional_fields,
            **model_to_dict(dose, exclude=['date', 'thumb_photo', 'banner_photo'])
        })


    
    # dose_list = json.dumps(news_list)
    

    #paginator = Paginator(event_list, 5) #show 10 objects per page
    #page_number = request.GET.get('page')
    #events = paginator.get_page(page_number)

    # context = {
    #     "dose_list": dose_list,
    # }
    return HttpResponse(json.dumps(dose_list, cls=ExtendedEncoder), content_type="application/json")

def dose_list_date(request, date_range):
    startdate = date.today()
    enddate = startdate + timedelta(days=date_range)
    dose_list = serializers.serialize('json', Event.objects.filter(date__range=[startdate, enddate]))

    #paginator = Paginator(event_list, 5) #show 10 objects per page
    #page_number = request.GET.get('page')
    #events = paginator.get_page(page_number)

    context = {
        "dose_list": dose_list,
    }
    return HttpResponse(dose_list, content_type="application/json")

def news_list_date(request, date_range):
    startdate = date.today() - timedelta(days=date_range)
    enddate = date.today() + timedelta(days=1)
    news_list = serializers.serialize('json', Event.objects.filter(date__range=[startdate, enddate]))
    print(startdate)
    print(enddate)

    #paginator = Paginator(event_list, 5) #show 10 objects per page
    #page_number = request.GET.get('page')
    #events = paginator.get_page(page_number)

    context = {
        "news_list": news_list,
    }
    return HttpResponse(news_list, content_type="application/json")

def event_list_date(request, date_range):
    startdate = date.today()
    enddate = startdate + timedelta(days=date_range)
    event_list = serializers.serialize('json', Event.objects.filter(date__range=[startdate, enddate]))

    #paginator = Paginator(event_list, 5) #show 10 objects per page
    #page_number = request.GET.get('page')
    #events = paginator.get_page(page_number)

    context = {
        "event_list": event_list,
    }
    return HttpResponse(event_list, content_type="application/json")
    

def student_programs(request):
    return render(request, "polls/student-programs.html")

def community_programs(request):
    return render(request, "polls/community-programs.html")

def k12_programs(request):
    name_list = ["High School Economics Teacher Certification", "federal reserve institute", "$martPath", "Educator Workshops"]
    program_list = Program.objects.filter(name__in=name_list)
    date_list = []
    for program in program_list:
        date_list.append(program.date)
    
    context = {
        "date_list" : date_list
    }
    return render(request, "polls/k12-programs.html", context)

def history_mission(request):
    return render(request, "polls/history-mission.html")

def our_team(request):
    staff_list = sorted(Staff.objects.all(), key=lambda staff: staff.name.split()[-1])
    director_list = sorted(Director.objects.all(), key=lambda staff: staff.name.split()[-1])
    officer_list = sorted(Officer.objects.all(), key=lambda staff: staff.name.split()[-1])
    context = {
        "staff_list": staff_list,
        "director_list": director_list,
        "officer_list": officer_list
    }
    return render(request, "polls/our-team.html", context)

def directors(request):
    director_list = sorted(Director.objects.all(), key=lambda staff: staff.name.split()[-1])
    context = {
        "director_list": director_list,
    }
    return render(request, "polls/directors.html", context)

def index(request):
    daily_dose = DailyDose.objects.order_by("-date")
    context = {
        "first_dose": daily_dose[0],
        "second_dose": daily_dose[1],
        "third_dose": daily_dose[2]
    }
    return render(request, "polls/index.html", context)


def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)


def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)


def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)

def financial_statements(request):
    
    return render(request, "polls/financial-statements.html")