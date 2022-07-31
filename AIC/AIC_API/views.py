from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.response import Response
from rest_framework_api_key.models import APIKey
from rest_framework_api_key.crypto import KeyGenerator
from .models import Api
from AIC_APP.models import Yobotuser


class ChatAssistantView(APIView):

    def get(self, request, *args, **kwargs):
        if 'request' in request.data.keys():
            if request.GET.get("api",None)!=None:
                return Response({
                    "status": "Success"
                })
            else:
                return Response({
                    "status": "Please Provide Active API Key"
                })
        else:
            return Response({
                "status": "failed",
                "message": "Query is Required"
            })

    def post(self, request, *args, **kwargs):
        if "Id" in request.session.keys():
            api_key,key = APIKey.objects.create_key(name=request.session["Name"])
            print(key)
            print(APIKey.objects.get_from_key(key=key))
            ApiData = Api(Yobotuser.objects.get(id=request.session["Id"]),)
            ApiData.save()
            return Response({
                "status": "success",
                "message": f"{api_key} {key}API Key Successfully Created"
            })
        else:
            return Response({
                "status":"Failed",
                "message":"Please Login First"
            })
