from rest_framework import viewsets
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from .models import BinStatus
from .serializers import BinStatusSerializer

# BinStatus ViewSet
class BinStatusViewSet(viewsets.ModelViewSet):
    queryset = BinStatus.objects.all()
    serializer_class = BinStatusSerializer

    def get_permissions(self):
        # Allow unauthenticated access to the list and retrieve actions
        if self.action in ['list', 'retrieve', 'create']:
            return [AllowAny()]
        return [IsAuthenticated()]  # Only authenticated users can create, update, delete

# Latest Bin Status View
@api_view(['GET'])
@permission_classes([AllowAny])  # Allow unauthenticated access to this view
def latest_bin_status(request):
    try:
        # Fetch the latest BinStatus instance
        latest_status = BinStatus.objects.last()

        if latest_status:
            # Transform the bio_status and recyclable_status
            data = {
                'bio_status': 'empty' if latest_status.bio_status == 'not full' else 'full',
                'non_bio_status': 'empty' if latest_status.non_bio_status == 'not full' else 'full',
            }
            return Response(data)
        else:
            return Response({"detail": "No bin status available."}, status=404)

    except Exception as e:
        # Handle any unexpected errors
        return Response({"detail": str(e)}, status=500)

