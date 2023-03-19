from django.shortcuts import render

# Create your views here.
from django.shortcuts import render,redirect
from django.utils import timezone
from .forms import ExtractionForm
from .models import ExtractedData
from selenium import webdriver
from django.views.decorators.csrf import csrf_exempt


def extract_data(url,xpath):
    driver = webdriver.Chrome()
    driver.get(url)
    element = driver.find_element("xpath",xpath)
    data = element.text
    driver.quit()
    return data

def all_Details(request):
    app = ExtractedData.objects.all()
    return render(request, 'Webpage/app.html',
                  {'app':app})

def savedata(request):
    if request.method=="POST":
        site = request.POST.get('site')
        xpath = request.POST.get('xpath')
        data = request.POST.get('data')
        creation_time = request.POST.get('creation_time')
        en = ExtractedData(site=site,xpath=xpath,data=data,creation_time=creation_time)
        en.save()
    print(en)
    return render(request, 'Webpage/form.html')

# def my_view(request):
#     if request.method=="POST":
#         formdata = ExtractionForm(request.POST)
#         if formdata.is_valid():
#             formdata.save()
#             return redirect('ok')
#     else:
#         formdata = ExtractionForm()
#     return render(request,'Webpage/form.html',{'form': formdata})

# @ csrf_exempt
def extract(request):
    if request.method == 'POST':
        form = ExtractionForm(request.POST)
        if form.is_valid():
            site = form.cleaned_data['site']
            xpath = form.cleaned_data['xpath']
            data = extract_data(site, xpath)
            extracted_data = ExtractedData(site=site, xpath=xpath, data=data)
            extracted_data.save()
            return render(request, 'Webpage/app.html', {'data': data})
    else:
        form = ExtractionForm()
    return render(request, 'Webpage/form.html', {'form': form})
