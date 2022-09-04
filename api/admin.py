from django.contrib import admin
from api.models import Contributor, Comment, Project, Issue


class ContributorAdmin(admin.ModelAdmin):
    list_display = ('id', 'user_id', 'project_id', 'permission')


class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'issue_id', 'description', 'author_id')


class ProjectAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'description')


class IssueAdmin(admin.ModelAdmin):
    list_display = ('id', 'project_id', 'title', 'tag', 'priority')


admin.site.register(Contributor, ContributorAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Project, ProjectAdmin)
admin.site.register(Issue, IssueAdmin)
