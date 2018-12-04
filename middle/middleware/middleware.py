from django.http import HttpResponse
from xml.etree import ElementTree
import json
import dicttoxml



def simple_middleware(get_response):

    def middleware(request):

        response = get_response(request)
        if request.GET['type'] =='json':
            return HttpResponse(response)

        elif request.GET['type'] == 'xml':
            bytes = response.content
            string = bytes.decode('ASCII')
            my_json = json.loads(string)
            resp = dicttoxml.dicttoxml(my_json)
            a = resp.decode('ASCII')
            root = ElementTree.fromstring(a)
            element = ElementTree.dump(root)
            return HttpResponse(element, content_type='application/xml')


        elif request.GET['type'] == 'str':
            string = response.content
            res = string.decode('ASCII')
            return HttpResponse(res)

        return response

    return middleware



