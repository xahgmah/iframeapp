from django.http import HttpResponse
from utils import DESCipher
from django.conf import settings
import json

def iframe_view(request):
    response = HttpResponse()
    data = request.META.get("QUERY_STRING")
    if data:
        try:
            ac = DESCipher(settings.REDDIT_SECRET_KEY)
            row = ac.decrypt(data[5:])
            data = json.loads(row)
            result = """
            Hellow %s<br/>
            This is your details:<br/>
            name: %s,<br/>
            email: %s,<br/>
            course: %s<br/>
            Happy learning!
            """ % (data.get("username"),data.get("username"),data.get("email"),data.get("course_id"))
        except Exception as e:
            result = "<span style='color:red'>%s</span>" % e.message
    else:
        result = "Data wasn't received"
    response._headers['x-frame-options'] = ('X-Frame-Options', 'ALLOWALL')
    response.content = result

    return response
