from rest_framework import serializers
from api.models import Project, Issue, Contributor, Comment
from authentication.serializer import UserSerializer


class ProjectListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ['id', 'title', 'type', 'description']

    def create(self, validated_data):
        project = Project.objects.create(**validated_data)
        user = self.context['request'].user
        Contributor.objects.create(user=user, project=project, permission='author', role='author')
        return project


class ContributorListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Contributor
        fields = ['id', 'user', 'permission']

    def to_representation(self, instance):
        self.fields['user'] = UserSerializer(read_only=True)
        return super().to_representation(instance)


class ProjectDetailSerializer(serializers.ModelSerializer):
    contributor = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Project
        fields = ['id', 'title', 'type', 'description', 'contributor']

    def get_contributor(self, instance):
        project_id =
        queryset = instance.contributor.filter(project=project_id)
        serializers = ContributorListSerializer(queryset, many=True)
        return serializers.data


class ContributorDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contributor
        fields = '__all__'

    def to_representation(self, instance):
        self.fields['author'] = UserSerializer(read_only=True)
        return super().to_representation(instance)


class IssueListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Issue
        fields = ['id', 'title', 'description', 'tag', 'priority', 'status', 'assignee', 'created_time']


class IssueDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Issue
        fields = '__all__'

    def to_representation(self, instance):
        self.fields['author'] = UserSerializer(read_only=True)
        return super().to_representation(instance)


class CommentListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'description', 'created_time']


class CommentDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'

    def to_representation(self, instance):
        self.fields['author'] = UserSerializer(read_only=True)
        return super().to_representation(instance)

