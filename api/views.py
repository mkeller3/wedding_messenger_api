from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from .serializers import *
from .helpers import *
from django.db.models import Q
from functools import reduce
import json

class account(APIView):
    permission_classes = (IsAuthenticated),

    def get(self, request):
        try:
            account_id = accountData.objects.get(username=request.user.username).account_id
        except accountData.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        accountDetails = accountData.objects.filter(account_id=account_id,username=request.user.username)
        serializer = accountDataSerializer(accountDetails, many=True)
        return Response(serializer.data)


    def post(self, request):    
        newAccountId = id_generator()
        serializer = accountDataSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(username=request.user.username,account_id=newAccountId)
        sendTextMessage(
            request.data['phone_number'],
            'Hi, welcome to Wedding Messenger We are so exicted to have the chance to help you with your wedding!',
            'https://media.giphy.com/media/5vef4sn8zhnlC/giphy.gif'
        )
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def put(self, request):
        try:
            accountDetails = accountData.objects.get(account_id=request.data['account_id'],username=request.user.username)
        except accountData.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = accountDataSerializer(accountDetails, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(account_id=accountDetails.account_id,username=request.user.username)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def delete(self, request):
        try:
            accountDetails = accountData.objects.get(account_id=request.data['account_id'],username=request.user.username)
        except accountData.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        accountDetails.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class guest(APIView):
    permission_classes = (IsAuthenticated),

    def get(self, request):
        try:
            account_id = accountData.objects.get(username=request.user.username).account_id
        except accountData.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND) 
        try:
            guestDetails = guestData.objects.get(id=request.GET['id'],account_id=account_id)
        except guestData.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND) 
        guestDetails = guestData.objects.filter(id=request.GET['id'],account_id=account_id)
        serializer = guestDataSerializer(guestDetails, many=True)
        return Response(serializer.data)


    def post(self, request):   
        try:
            account_id = accountData.objects.get(account_id=request.data['account_id'],username=request.user.username).account_id
        except accountData.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND) 
        if guestData.objects.filter(account_id=account_id, phone_number=request.data['phone_number']):
             return Response({"error":f"This phone number is already used for this account."}, status=status.HTTP_400_BAD_REQUEST)
        serializer = guestDataSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(account_id=account_id)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def put(self, request):
        try:
             account_id = accountData.objects.get(username=request.user.username).account_id
        except accountData.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND) 
        try:
            guestDetails = guestData.objects.get(id=request.data['id'],account_id=account_id)
        except guestData.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        if request.data['phone_number'] != guestDetails.phone_number:
            if guestData.objects.filter(account_id=account_id, phone_number=request.data['phone_number']):
                return Response({"error":f"This phone number is already used for this account."}, status=status.HTTP_400_BAD_REQUEST)
        serializer = guestDataSerializer(guestDetails, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(account_id=account_id)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def delete(self, request):
        try:
             account_id = accountData.objects.get(username=request.user.username).account_id
        except accountData.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND) 
        try:
            guestDetails = guestData.objects.get(id=request.GET['id'],account_id=account_id)
        except guestData.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        guestDetails.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class guests(APIView):
    permission_classes = (IsAuthenticated),

    def get(self, request):
        try:
            account_id = accountData.objects.get(username=request.user.username).account_id
        except accountData.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND) 
        try:
            guestDetails = guestData.objects.filter(account_id=account_id)
        except guestData.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND) 
        serializer = guestDataSerializer(guestDetails, many=True)
        return Response(serializer.data)

class group(APIView):
    permission_classes = (IsAuthenticated),

    def get(self, request):
        try:
            account_id = accountData.objects.get(username=request.user.username).account_id
        except accountData.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND) 
        groupDetails = groupData.objects.filter(id=request.GET['id'],account_id=account_id)
        serializer = groupDataSerializer(groupDetails, many=True)
        return Response(serializer.data)


    def post(self, request):    
        try:
            account_id = accountData.objects.get(username=request.user.username).account_id
        except accountData.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND) 
        if groupData.objects.filter(account_id=account_id, group_name=request.data['group_name']):
            return Response({"error":f"This group name is already used for this account."}, status=status.HTTP_400_BAD_REQUEST)
        serializer = groupDataSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(account_id=account_id)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def put(self, request):
        try:
            account_id = accountData.objects.get(username=request.user.username).account_id
        except accountData.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND) 
        try:
            groupDetails = groupData.objects.get(id=request.data['id'])
        except groupData.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        if request.data['group_name'] != groupDetails.group_name:
            if groupData.objects.filter(account_id=account_id, group_name=request.data['group_name']):
                return Response({"error":f"This group name is already used for this account."}, status=status.HTTP_400_BAD_REQUEST)
        serializer = groupDataSerializer(groupDetails, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(account_id=account_id)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def delete(self, request):
        try:
             account_id = accountData.objects.get(username=request.user.username).account_id
        except accountData.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND) 
        try:
            groupDetails = groupData.objects.get(id=request.GET['id'],account_id=account_id)
        except groupData.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        groupDetails.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class groups(APIView): 
    permission_classes = (IsAuthenticated),

    def get(self, request):
        try:
            account_id = accountData.objects.get(username=request.user.username).account_id
        except accountData.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND) 
        try:
            groupDetails = groupData.objects.filter(account_id=account_id)
        except guestData.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND) 
        serializer = groupDataSerializer(groupDetails, many=True)
        return Response(serializer.data)

class alert(APIView):
    permission_classes = (IsAuthenticated),

    def get(self, request):
        try:
            account_id = accountData.objects.get(username=request.user.username).account_id
        except accountData.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND) 
        alertDetails = alertData.objects.filter(id=request.GET['id'], account_id=account_id)
        serializer = alertDataSerializer(alertDetails, many=True)
        return Response(serializer.data)


    def post(self, request): 
        try:
            account_id = accountData.objects.get(username=request.user.username).account_id
        except accountData.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND) 
        serializer = alertDataSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        if request.data['alert_type'] == 'live':
            if request.data['group_message'] == 'True':
                for groupId in json.loads(request.data['group_ids']):
                    try:
                        groupData.objects.get(account_id=account_id, pk=groupId)
                    except groupData.DoesNotExist:
                        return Response({"error":f"This group does not exist for this account."}, status=status.HTTP_400_BAD_REQUEST)
                    groupInformation = groupData.objects.get(account_id=account_id, pk=groupId)
                    guest_ids = []
                    for guestInformation in groupInformation.guests:
                        guest_ids.append(guestInformation)
                    guests = guestData.objects.filter(id__in=guest_ids).values()
                    for guestInformation in guests:
                        message = request.data['message']
                        message = message.replace('{first_name}', guestInformation['first_name']).replace('{last_name}', guestInformation['last_name']).replace('{full_name}', guestInformation['full_name']).replace('{full_address}', guestInformation['full_address']).replace('{drive_distance}', str(guestInformation['drive_distance']))
                        print(f'Group Message: {message}')
                        # sendTextMessage(
                        #     guestInformation['phone_number'],
                        #     request.data['message']
                        # )
            else:
                guests = guestData.objects.filter(account_id=account_id).values()
                for guestInformation in guests:
                    message = request.data['message']
                    message = message.replace('{first_name}', guestInformation['first_name']).replace('{last_name}', guestInformation['last_name']).replace('{full_name}', guestInformation['full_name']).replace('{full_address}', guestInformation['full_address']).replace('{drive_distance}', str(guestInformation['drive_distance']))
                    print(f'All Guest Message: {message}')
                    # sendTextMessage(
                    #     guestInformation['phone_number'],
                    #     request.data['message']
                    # )   
        elif request.data['alert_type'] == 'scheduled': 
            if request.data['group_message'] == 'True':
                for groupId in json.loads(request.data['group_ids']):
                    try:
                        groupData.objects.get(account_id=account_id, pk=groupId)
                    except groupData.DoesNotExist:
                        return Response({"error":f"This group does not exist for this account."}, status=status.HTTP_400_BAD_REQUEST)
        serializer.save()               
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def put(self, request):
        try:
            account_id = accountData.objects.get(username=request.user.username).account_id
        except accountData.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND) 
        try:
            alertDetails = alertData.objects.get(id=request.data['id'], account_id=account_id)
        except alertData.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = alertDataSerializer(alertDetails, data=request.data)
        serializer.is_valid(raise_exception=True)
        if request.data['group_message'] == 'True':
            for groupId in json.loads(request.data['group_ids']):
                try:
                    groupData.objects.get(account_id=account_id, pk=groupId)
                except groupData.DoesNotExist:
                    return Response({"error":f"This group does not exist for this account."}, status=status.HTTP_400_BAD_REQUEST)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def delete(self, request):
        try:
            account_id = accountData.objects.get(username=request.user.username).account_id
        except accountData.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        try:
            alertDetails = alertData.objects.get(id=request.GET['id'], account_id=account_id)
        except alertData.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        alertDetails.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class alerts(APIView):
    permission_classes = (IsAuthenticated),

    def get(self, request):
        try:
            account_id = accountData.objects.get(username=request.user.username).account_id
        except accountData.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND) 
        try:
            alertDetails = alertData.objects.filter(account_id=account_id)
        except alertData.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND) 
        serializer = alertDataSerializer(alertDetails, many=True)
        return Response(serializer.data)

class sendText(APIView):

    def post(self, request):    
        serializer = trialNumberDataSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        sendTextMessage(
            request.data['phone_number'],
            'Hi, welcome to Wedding Messenger We would love to help you with your special day. Click the following link to register. https://wedsec.com/register/',
            'https://media.giphy.com/media/10wwy1cJ8j2aD6/giphy.gif'
        )
        return Response(status=status.HTTP_200_OK)

class mapData(APIView):
    permission_classes = (IsAuthenticated),

    def get(self, request):
        try:
            account_id = accountData.objects.get(username=request.user.username).account_id
        except accountData.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND) 
        try:
            guestDetails = guestData.objects.filter(account_id=account_id)
        except guestData.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND) 

        mapJson = {
            'type': 'FeatureCollection',
            'features': []
        }

        for guestInformation in guestDetails:
            mapJson['features'].append({
                "type": "Feature",
                "geometry": {
                    "type": "Point",
                    "coordinates": [float(guestInformation.longitude), float(guestInformation.latitude)]
                },
                "properties": {
                    "name": guestInformation.full_name
                }
            })

        return Response(mapJson,status=status.HTTP_200_OK)