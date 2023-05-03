from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from django.http import HttpResponse
from django.views.generic import TemplateView
import requests
# Create your views here.

class HomeView(TemplateView):
    template_name = 'home.html'


class ValidateGst(APIView):
    """# This API check GST No Active or not active"""
    def post(self, request):
        gst_no = request.data.get('gstNo')
        if gst_no:
            url = "https://appyflow.in/api/verifyGST?gstNo={}&key_secret=YOUR_SECRET_KEY_TYPE_HERE".format(gst_no)
            resp = requests.get(url=url)
            data = resp.json()
            if 'error' in data:
                return Response('Invalid GST!!', status=status.HTTP_400_BAD_REQUEST)
            elif data['taxpayerInfo']['sts'] == 'Active':
                return Response("GST validated!!", status=status.HTTP_200_OK)
        return Response("Invalid request", status=status.HTTP_400_BAD_REQUEST)