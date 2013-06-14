# Create your views here.

from django.http import HttpResponse
from django.core import serializers

from experiments.models import Test

def index(request):
  return HttpResponse("Hello Chenil")

def tests(request):
    output = serializers.serialize("json", Test.objects.all())
    return HttpResponse(output, mimetype="application/json")