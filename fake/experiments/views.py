# Create your views here.

from django.http import HttpResponse
from django.utils import simplejson

from experiments.models import Test

def index(request):
  return HttpResponse("Hello Chenil")

def tests(request):
  output = simplejson.dumps( { 'tests': [{
    'description': o.description, 
    'location': o.location,
    'prod_left': o.prod_left,
    'prod_right': o.prod_right,
    'created_date': o.created_date.__str__(),
    'start_date': o.start_date.__str__(),
    'stop_date': o.stop_date.__str__(),
    'weight_left': str(o.weight_left) + ' g',
    'weight_right': str(o.weight_right) + ' g',
    'history': o.history,
  } for o in Test.objects.all()]}, "tests" )
  return HttpResponse(output, mimetype="application/json")