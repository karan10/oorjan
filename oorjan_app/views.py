from django.http import Http404
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .serializers import SolarDataSerializer
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.renderers import JSONRenderer
from .models import SolarMetaData, SolarData, SolarReferenceData
import json
import ast




class JSONResponse(HttpResponse):
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)


@csrf_exempt
def solar_data_request(request):
    if request.method == 'GET':
        solar_data = SolarData.objects.all()
        serializer = SolarDataSerializer(solar_data, many=True)
        return JSONResponse(serializer.data)

    elif request.method == 'POST':

        # return JSONResponse({'error':'Invalid Installation Key'})
        # args_str = ','.join(cursor.mogrify("(%s, %s)", x) for x in email_data_list)
        # query = """
        #     INSERT INTO oorjan_app_solarreferencedata (dc_power,timestamp) VALUES """ + args_str + """; 
        #     """

        # cursor.execute(query)
        x = ast.literal_eval(request.body)
        for i in x:
            q = SolarReferenceData(dc_power=i[0], timestamp=i[1])
            q.save()

        return JSONResponse({'success':'Done'})



        post_data = json.loads(request.body)

        try:
            solar_user = SolarMetaData.objects.get(installation_key=post_data['installation_key'])
        except:
            return JSONResponse({'error':'Invalid Installation Key'})

        post_data.pop('installation_key', None)

        post_data['user_id'] = solar_user.id

        serializer = SolarDataSerializer(data=post_data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data, status=status.HTTP_201_CREATED)
        return JSONResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)