from django.shortcuts import get_object_or_404
from rest_framework import status
from django.http import JsonResponse
from .models import ABLine
from .serializers import ABLineSerializer
from rest_framework.decorators import api_view


@api_view(['GET'])
def abline_list(request):
    ablines = ABLine.objects.all()
    serializer = ABLineSerializer(ablines, many=True)
    return JsonResponse(serializer.data, safe=False)


@api_view(['GET'])
def abline_detail(request, pk):
    abline = get_object_or_404(ABLine, pk=pk)
    serializer = ABLineSerializer(abline)
    return JsonResponse(serializer.data)


@api_view(['POST'])
def abline_create(request):
    serializer = ABLineSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
    return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def abline_update(request, pk):
    abline = get_object_or_404(ABLine, pk=pk)
    serializer = ABLineSerializer(abline, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return JsonResponse(serializer.data)
    return JsonResponse(serializer.errors, status=400)


@api_view(['GET'])
def abline_delete(request, pk):
    abline = get_object_or_404(ABLine, pk=pk)
    abline.delete()
    return JsonResponse({'message': 'ABLine deleted successfully!'}, status=204)
