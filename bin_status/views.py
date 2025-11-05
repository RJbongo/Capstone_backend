from rest_framework import viewsets
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from .models import BinStatus
from .serializers import BinStatusSerializer

# BinStatus ViewSet
class BinStatusViewSet(viewsets.ModelViewSet):
    queryset = BinStatus.objects.all().order_by("-updated_at")
    serializer_class = BinStatusSerializer

    def get_permissions(self):
        # Allow access to list/retrieve/create
        if self.action in ['list', 'retrieve', 'create']:
            return [AllowAny()]
        return [IsAuthenticated()]

    def create(self, request, *args, **kwargs):
        # Fill missing fields with "not full" if only one bin is sent
        data = request.data.copy()
        if "bio_status" not in data:
            data["bio_status"] = "not full"
        if "non_bio_status" not in data:
            data["non_bio_status"] = "not full"

        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(serializer.data, status=201)


# Latest Bin Status View (for frontend)
@api_view(['GET'])
@permission_classes([AllowAny])
def latest_bin_status(request):
    latest_status = BinStatus.objects.last()
    if latest_status:
        data = {
            'bio_status': latest_status.bio_status,
            'non_bio_status': latest_status.non_bio_status,
        }
        return Response(data)
    return Response({"detail": "No bin status available."}, status=404)
