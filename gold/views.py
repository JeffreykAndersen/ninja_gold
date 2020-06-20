from django.shortcuts import render, redirect, HttpResponse
import random 
from datetime import datetime

def index(request):
    if 'results' not in request.session:
        request.session["results"] = []
    return render (request, "index.html")

def process(request):
    if request.method == "POST":
        if "gold_total" not in request.session:
            request.session['gold_total'] = 0
        if request.POST['gold'] == "Work the Farm":
            gold_add = round(random.random()*10+10)
            request.session['gold_total'] += gold_add
            request.session['style'] = 'more'
            request.session['results'].append(f"Yes! you just got {gold_add} gold from the farm. ({str(datetime.now())})")          
        if request.POST['gold'] == "Search the Cave":
            gold_add = round(random.random()*5+5)
            request.session['gold_total'] += gold_add
            request.session['style'] = 'more'
            request.session['results'].append(f"Yes! you just got {gold_add} gold from the caves. ({str(datetime.now())})")
        if request.POST['gold'] == "Search the House":
            gold_add = round(random.uniform(2,5))
            request.session['gold_total'] += gold_add
            request.session['style'] = 'more'
            request.session['results'].append(f"Yes! you just got {gold_add} gold from the house. ({str(datetime.now())})")
        if request.POST['gold'] == "Go to Casino":
            gold_add = round(random.uniform(-50, 50))
            request.session['gold_total'] += gold_add
            if gold_add > 0:
                request.session['results'].append(f"Yes! you just got {gold_add} gold from the casino. ({str(datetime.now())})")
                request.session['style'] = 'more'
            elif gold_add < 0:
                request.session['results'].append(f"Oh No! you lost {gold_add} gold at the casino.  ({str(datetime.now())})")
                request.session['style'] = 'less'
        if request.POST['gold'] == "Reset Game":
            request.session.flush()
        return redirect('/')
        
  