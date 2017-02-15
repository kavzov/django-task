from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from fields.models import Field
import json


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


def fields(request):
	return render(request, 'fields/index.html')


@csrf_exempt            # error without it: "Forbidden (CSRF cookie not set.): /fields/script"
def script(request):
    # read the data from form
    data = json.dumps(request.POST)

    # write to bd
    dbfield = Field(field_data=data)
    dbfield.save()

    return HttpResponse()


def cleardb(request):
    Field.objects.all().delete()
    return HttpResponse()


def output(request):
    data = Field.objects.order_by('id')
    fields = {}
    for jsondata in data:
        dictdata = json.loads(str(jsondata))
        fields.update(dictdata)
    json_fields = json.dumps(fields, sort_keys=True, indent=4)

    if data:
        return render(request, 'fields/output.html', {'data': json_fields})
    else:
        msg = "Nothing to output"
        return render(request, 'fields/output.html', {'data': msg})
