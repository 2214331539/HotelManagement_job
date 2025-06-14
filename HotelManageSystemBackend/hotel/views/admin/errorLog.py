from rest_framework.decorators import api_view

from hotel.handler import APIResponse
from hotel.models import ErrorLog
from hotel.serializers import ErrorLogSerializer


# 错误日志
@api_view(['GET'])
def list_api(request):
    if request.method == 'GET':
        errorLogs = ErrorLog.objects.all().order_by('-log_time')
        serializer = ErrorLogSerializer(errorLogs, many=True)
        return APIResponse(code=0, msg='查询成功', data=serializer.data)
