from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import CollegeEvent,Register 
from .serializers import CollegeEventsSerializer,RegisterSerializer

class CollegeEventView(APIView):
    def get(self,request):
        events = CollegeEvent.objects.all()
        serialize=CollegeEventsSerializer(events,many=True)
        return Response(serialize.data)
    
class RegisterView(APIView):
    def get(self,request):
        events = Register.objects.all()
        serialize=RegisterSerializer(events,many=True)
        return Response(serialize.data)
    def post(self,request):
        data=RegisterSerializer(data=request.data)
        if  data.is_valid():
            data.save()
            specific_event=CollegeEvent.objects.get(event_id=data.validated_data['event_id'])
            if specific_event.seats==0:
                return Response({'message':'No seats available'})
            else:
                specific_event.seats-=1
                specific_event.save()
                return Response({
                    'message':'Registered Successfully',
                    'Available seats': specific_event.seats})
        return Response({'message':'Try again'})   