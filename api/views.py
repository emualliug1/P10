from api.models import Project, Issue, Contributor, Comment
from api.serializer import ProjectListSerializer, ProjectDetailSerializer
from api.serializer import ContributorListSerializer, ContributorDetailSerializer
from api.serializer import IssueListSerializer, IssueDetailSerializer
from api.serializer import CommentListSerializer, CommentDetailSerializer
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from api.permissions import IsAuthorOrReadOnly


class MultipleSerializerMixin:
    """
    Creation d'une Mixin pour afficher la vue liste ou detail
    """

    serializer_detail_class = None
    action = None

    def get_serializer_class(self):
        if self.action == 'retrieve' and self.serializer_detail_class is not None:
            return self.serializer_detail_class
        return super().get_serializer_class()


class ProjectViewSet(MultipleSerializerMixin, ModelViewSet):
    """
    ViewSet des projets
    """

    serializer_class = ProjectListSerializer
    serializer_detail_class = ProjectDetailSerializer
    permission_classes = [IsAuthenticated]
    queryset = Project.objects.all()

    def get_queryset(self):
        return self.queryset


class ContributorViewSet(MultipleSerializerMixin, ModelViewSet):
    """
    ViewSet des contributors
    """

    serializer_class = ContributorListSerializer
    serializer_detail_class = ContributorDetailSerializer
    permission_classes = [IsAuthenticated]
    queryset = Contributor.objects.all()

    def get_queryset(self):
        project_id = self.kwargs['project_id']
        return self.queryset.filter(project=project_id)

    def perform_create(self, serializer):
        serializer.save(project=Project.objects.get(id=self.kwargs['project_id']),
                        permission='contributor'
                        )


class IssueViewSet(MultipleSerializerMixin, ModelViewSet):
    """
    ViewSet des issues
    """

    serializer_class = IssueListSerializer
    serializer_detail_class = IssueDetailSerializer
    permission_classes = [IsAuthorOrReadOnly]
    queryset = Issue.objects.all()

    def get_queryset(self):
        project_id = self.kwargs['project_id']
        return self.queryset.filter(project=project_id)

    def perform_create(self, serializer):
        serializer.save(project=Project.objects.get(id=self.kwargs['project_id']),
                        author=self.request.user
                        )


class CommentViewSet(MultipleSerializerMixin, ModelViewSet):
    """
    ViewSet des comments
    """

    serializer_class = CommentListSerializer
    serializer_detail_class = CommentDetailSerializer
    permission_classes = [IsAuthorOrReadOnly]
    queryset = Comment.objects.all()

    def get_queryset(self):
        issue_id = self.kwargs['issue_id']
        return self.queryset.filter(issue=issue_id)

    def perform_create(self, serializer):
        serializer.save(issue=Issue.objects.get(id=self.kwargs['issue_id']),
                        author=self.request.user
                        )