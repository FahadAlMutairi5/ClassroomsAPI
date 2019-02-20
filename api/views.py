from rest_framework.generics import ListAPIView, DestroyAPIView, RetrieveUpdateAPIView, RetrieveAPIView , CreateAPIView
from classes.models import Classroom
from .serializers import ClassroomListSerializer ,ClassroomDetailSerializer ,ClassroomUpdateSerializer


class ClassesListView(ListAPIView):
    queryset = Classroom.objects.all()
    serializer_class = ClassroomListSerializer

# Complete me
class ClassesDetailView(RetrieveAPIView):
    queryset = Classroom.objects.all()
    serializer_class = ClassroomDetailSerializer
    lookup_field = 'id'
    lookup_url_kwarg = 'classroom_id'


# Complete me
class ClassesUpdateView(RetrieveUpdateAPIView):
    queryset = Classroom.objects.all()
    serializer_class = ClassroomUpdateSerializer
    lookup_field = 'id'
    lookup_url_kwarg = 'classroom_id'


# Complete me
class ClassesDeleteView(DestroyAPIView):
    queryset = Classroom.objects.all()
    lookup_field = 'id'
    lookup_url_kwarg = 'classroom_id'


class ClassesCreateView(CreateAPIView):
    serializer_class = ClassroomUpdateSerializer

    def perform_create(self, serializer):
        serializer.save(teacher=self.request.user)