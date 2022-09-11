from rest_framework import serializers
from api.models import Project, Issue, Contributor, Comment
from authentication.serializer import UserSerializer


class RepresentationMixinIssue:

    def to_representation(self, instance):
        self.fields['author'] = UserSerializer(read_only=True)
        self.fields['assignee'] = UserSerializer(read_only=True)
        return super().to_representation(instance)


class ProjectListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ['id', 'title', 'type', 'description']

    def create(self, validated_data):
        project = Project.objects.create(**validated_data)
        user = self.context['request'].user
        Contributor.objects.create(user=user, project=project, permission='author', role='author')
        return project


class ProjectDetailSerializer(serializers.ModelSerializer):
    contributors = serializers.SerializerMethodField(read_only=True)
    issues = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Project
        fields = ['id', 'title', 'type', 'description', 'contributors', 'issues']

    def get_contributors(self, instance):
        queryset = instance.contributors.all()
        serializers = ContributorDetailSerializer(queryset, many=True)
        return serializers.data

    def get_issues(self, instance):
        queryset = instance.issues.all()
        serializers = IssueDetailSerializer(queryset, many=True)
        return serializers.data


class ContributorListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Contributor
        fields = ['id', 'user']

    def to_representation(self, instance):
        self.fields['user'] = UserSerializer(read_only=True)
        return super().to_representation(instance)


class ContributorDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contributor
        fields = '__all__'

    def to_representation(self, instance):
        self.fields['author'] = UserSerializer(read_only=True)
        return super().to_representation(instance)


class IssueListSerializer(RepresentationMixinIssue, serializers.ModelSerializer):
    class Meta:
        model = Issue
        fields = ['id', 'title','description', 'tag', 'priority', 'status', 'assignee', 'created_time']


class IssueDetailSerializer(RepresentationMixinIssue, serializers.ModelSerializer):
    comments = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Issue
        fields = ['id', 'title', 'author', 'description', 'tag', 'priority', 'status', 'assignee', 'created_time', 'comments']

    def get_comments(self, instance):
        queryset = instance.comments.all()
        serializers = CommentDetailSerializer(queryset, many=True)
        return serializers.data


class CommentListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'description','created_time']

    def to_representation(self, instance):
        self.fields['author'] = UserSerializer(read_only=True)
        return super().to_representation(instance)


class CommentDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'

    def to_representation(self, instance):
        self.fields['author'] = UserSerializer(read_only=True)
        return super().to_representation(instance)

