from django.shortcuts import render

def simple_interest(request):
    si = None
    
    if request.method == "POST":
        p = float(request.POST.get("principal"))
        r = float(request.POST.get("rate"))
        t = float(request.POST.get("time"))
        
        si = (p * r * t) / 100

    return render(request, "simple_interest.html", {"si": si})
    
