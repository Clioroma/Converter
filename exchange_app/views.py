from django.shortcuts import render
from zeep import Client
# Create your views here.
def exchange(request):
    client = Client('http://www.cbr.ru/DailyInfoWebServ/DailyInfo.asmx?wsdl')
    date = client.service.GetLatestDateTime()
    result = client.service.GetCursOnDate(date)

    names = []
    value_list = result['_value_1']['_value_1']
    for i in range(len(value_list)):
        b = value_list[i]['ValuteCursOnDate']
        names.append(b['Vname'].strip())



    context = {
        'names': names
    }
    return render(request=request, template_name='exchange_app/index.html', context=context)