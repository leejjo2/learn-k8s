from django.http import HttpResponse, HttpResponseServerError

def home(request):
    return HttpResponse("Test: OK")

def liveness(request):
    return HttpResponse("Test: OK")

def readiness(request):
    try:
        # Connect to database
        return HttpResponse("Test: OK")
    except Exception as e:
        return HttpResponseServerError("db: cannot connect to database.")
