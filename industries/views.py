from django.http import Http404
from industries.models import Industries
from rest_framework.views import APIView
from industries.serializer import IndustriesSerializer
from rest_framework.response import Response
from rest_framework.status import HTTP_201_CREATED, HTTP_400_BAD_REQUEST, HTTP_200_OK, HTTP_204_NO_CONTENT
from contact.response import ResponseUtils


class IndustriesCollection(APIView):
    def get(self, request, format=None):
        industries = Industries.objects.all()
        serializer = IndustriesSerializer(industries, many=True)
        response = {
            "list": {
                "data": serializer.data,
                "count": industries.count()
            }
        }
        return Response(data=response, status=HTTP_200_OK)
    
    def post(self, request, format=None):
        serializer = IndustriesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            response = ResponseUtils.format_response(serialized_data=serializer.data)
            return Response(data=response, status=HTTP_201_CREATED)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)


class IndustriesSingle(APIView):
    def get_object(self, pk):
        try:
            return Industries.objects.get(pk=pk)
        except Industries.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        industry = self.get_object(pk=pk)
        serializer = IndustriesSerializer(industry)
        response = ResponseUtils.format_response(serialized_data=serializer.data)
        return Response(data=response, status=HTTP_200_OK)

    def put(self, request, pk):
        # full update
        industry = self.get_object(pk=pk)
        serializer = IndustriesSerializer(industry, data=request.data)
        if serializer.is_valid():
            serializer.save()
            response = ResponseUtils.format_response(serialized_data=serializer.data)
            return Response(data=response, status=HTTP_200_OK)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)
    
    """ def put(self, request, pk):
        # partial update with only required fields
        industry = self.get_object(pk=pk)
        serializer = IndustriesSerializer(industry, data=request.data)
        if serializer.is_valid():
            industry.name = request.data.get("name")
            industry.save()
            response = {"data": serializer.data}
            return Response(data=response, status=HTTP_200_OK)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST) """
    
    def delete(self, request, pk):
        industry = self.get_object(pk=pk)
        industry.delete()
        return Response(status=HTTP_204_NO_CONTENT)