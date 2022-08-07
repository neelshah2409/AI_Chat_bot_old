from rest_framework.parsers import JSONParser
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework_api_key.models import APIKey
from rest_framework import status
from .models import Api
from .serializers import ApiSerialize
from Predict.predict import predict_class, get_response
from AIC_APP.models import Yobotuser
import json
import os

#answering query via api
class ChatAssistantView(APIView):

    def get(self, request, *args, **kwargs):
        if request.GET.get("query",None)!=None:
            if request.GET.get("api",None)!=None:
                try:
                    api = Api.objects.get(api_key=request.GET.get("api"))
                    serializer = ApiSerialize(api,many=False)
                    if api.active==True:
                        id = serializer.data['user_id']
                        intents = json.loads(open(f"{os.getcwd()}{os.sep}AIC_APP{os.sep}static{os.sep}AIC_APP{os.sep}intents{os.sep}intents{id}.json").read())
                        message = request.POST.get('message', 'hey')
                        ints = predict_class(message, id)
                        res = get_response(ints, intents)
                        return Response({
                            "status":"Success",
                            "message":res
                        },status.HTTP_200_OK)

                    else:
                        return Response({
                            "status": "Failed",
                            "message": "API Key Error"
                        },status.HTTP_401_UNAUTHORIZED)
                except Exception as e:
                    print(e)
                    return Response({
                        "status": "Failed",
                        "message": "Sorry We Can't Help You"
                    },status.HTTP_404_NOT_FOUND)


            else:
                return Response({
                    "status": "Failed","message":"Please Provide Active API Key"
                },status.HTTP_400_BAD_REQUEST)


        else:
            return Response({
                "status": "failed",
                "message": "Query is Required"
            },status.HTTP_400_BAD_REQUEST)

#create your API key
class ApiKeyView(APIView):
    def get(self, request, *args, **kwargs):
        if "Id" in request.session.keys():
            apis = Api.objects.filter(user_id=request.session["Id"])
            print(apis)
            serializer = ApiSerialize(apis, many=True)
            print(serializer.data)
            return Response({"data": serializer.data})
        else:
            return Response({
                "status": "Failed",
                "message": "Please Login First"
            },status.HTTP_403_FORBIDDEN)

    def post(self, request, *args, **kwargs):
        if "Id" in request.session.keys():
            api_key, key = APIKey.objects.create_key(name=request.session["Id"])
            ApiData = Api(user_id=Yobotuser.objects.get(id=request.session["Id"]),
                          api_key_id=APIKey.objects.get_from_key(key=key), api_key=key)
            ApiData.save()
            return Response({
                "status": "success",
                "message": "API Key Successfully Created"
            },status.HTTP_201_CREATED)
        else:
            return Response({
                "status": "Failed",
                "message": "Please Login First"
            },status.HTTP_403_FORBIDDEN)

# for managing api keys: update and delete
@api_view(["PUT","DELETE","GET"])
def manageApiKeys(request, api):
    if request.method == "GET":
        if "Id" in request.session.keys():
            try:
                api = Api.objects.get(api_key=api)
                serializer = ApiSerialize(api, many=False)
                return Response({
                    "status": "Success",
                    "message": {"name":serializer.data["name"],"api_key":serializer.data["api_key"],"active":serializer.data["active"]}
                },status.HTTP_200_OK)
            except Exception as e:
                return Response({
                    "status": "Failed",
                    "message": "API Key Doesn't Exist"
                },status.HTTP_404_NOT_FOUND)
        else:
            return Response({
                "status": "Failed",
                "message": "Please Login First"
            },status.HTTP_403_FORBIDDEN)

    if request.method == "PUT":
        if "Id" in request.session.keys():
            try:
                api = Api.objects.get(api_key=api)
                data = JSONParser().parse(request)
                api.active=data.get("activate",api.active)
                api.name = data.get("name",api.name)
                api.save()
                serializer = ApiSerialize(api, many=False)
                return Response({
                    "status": "Success",
                    "message": serializer.data
                },status.HTTP_200_OK)
            except Exception as e:
                return Response({
                    "status": "Failed",
                    "message": "API Key Doesn't Exist"
                },status.HTTP_404_NOT_FOUND)
        else:
            return Response({
                "status": "Failed",
                "message": "Please Login First"
            },status.HTTP_403_FORBIDDEN)

    if request.method == "DELETE":
        if "Id" in request.session.keys():
            try:
                api = Api.objects.get(api_key=api)
                api_keys = APIKey.objects.get_from_key(key=api.api_key)
                api_keys.delete()
                return Response({
                    "status": "Success",
                    "message": "API Key Deleted Successfully"
                },status.HTTP_204_NO_CONTENT)
            except Exception as e:
                print(e)
                return Response({
                    "status": "Failed",
                    "message": "API Key Does Not Exists"
                },status.HTTP_404_NOT_FOUND)
        else:
            return Response({
                "status": "Failed",
                "message": "Please Login First"
            },status.HTTP_403_FORBIDDEN)
