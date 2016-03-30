import urllib

from django.http import HttpResponse
from utils import AESCipher
from django.conf import settings
import json


def iframe_view(request):
    response = HttpResponse()
    data = str(request.GET.get('data'))
    if data:
        try:
            row = AESCipher(settings.REDDIT_SECRET_KEY).decrypt(data)
            data = json.loads(row)
            result = """
            Hello %s<br/><br/>
            This is your details:<br/>
            Name: %s,<br/>
            Email: %s,<br/>
            Course: %s<br/><br/>
            Happy learning!
            """ % (data.get("username"), data.get("username"), data.get("email"), data.get("course_id"))
        except Exception as e:
            result = "<span style='color:red'>%s</span>" % e.message
    else:
        result = "Data wasn't received"
    response._headers['x-frame-options'] = ('X-Frame-Options', 'ALLOWALL')
    response.content = result

    return response
