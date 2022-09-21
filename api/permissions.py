from rest_framework.permissions import BasePermission
from api.models import Project, Contributor, Issue, Comment
from django.shortcuts import get_object_or_404


def in_project(user, project):
    """Vérifie si l'utilisateur fait partie du projet"""
    for contributor in Contributor.objects.filter(project_id=project):
        if user == contributor.user:
            return True
    return False


class ProjectPermission(BasePermission):
    """
     Permission de classe Projet :

     Liste :
     Seul les utilisateurs authentifier peuvent accéder à cette vue.

     Détails :
     Seul l'auteur du projet peut modifier ou supprimer le projet.
     """

    message = "Vous n'avez pas la permission d'effectuer cette action"

    def has_permission(self, request, view):
        return request.user and request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        liste = ['list', 'retrieve', 'create']
        details = ['update', 'destroy']

        if view.action in liste:
            return in_project(request.user, obj)
        elif view.action in details:
            return request.user == obj.author


class IssuePermission(BasePermission):
    """
    Permission de classe Issue :
    Liste :
    Seul les contributeurs authentifier peuvent accéder à cette vue
    et peuvent créer des issues au projet.
    Détails :
    Seul l'auteur de l'issue peut la modifier ou la supprimer.
    """

    message = "Vous n'avez pas la permission d'effectuer cette action"

    def has_object_permission(self, request, view, obj):
        project = get_object_or_404(Project, pk=view.kwargs['project_pk'])
        liste = ['list', 'retrieve', 'create']
        details = ['create', 'destroy']

        if view.action in liste:
            return in_project(request.user, project)
        if view.action in details:
            return request.user == obj.author


class CommentPermission(BasePermission):
    """
    Permission de classe Comment :
    Liste :
    Seul les contributeurs authentifier peuvent accéder à cette vue
    et peuvent créer des commentaires d'une issue.
    Détails :
    Seul l'auteur du commentaire peut le modifier ou le supprimer.
    """

    message = "Vous n'avez pas la permission d'effectuer cette action"

    def has_object_permission(self, request, view, obj):
        project = get_object_or_404(Project, pk=view.kwargs['project_pk'])
        liste = ['list', 'retrieve', 'create']
        details = ['update', 'destroy']

        if view.action in liste:
            return in_project(request.user, project)
        if view.action in details:
            return request.user == obj.author


class ContributorPermission(BasePermission):
    """
    Permission de classe Contributor :
    Liste :
    Seul les contributeurs peuvent accéder à cette vue.
    Détails :
    Seul l'auteur du projet peut ajouter ou supprimer des contributeurs.
    """

    message = "Vous n'avez pas la permission d'effectuer cette action"

    def has_object_permission(self, request, view, obj):
        project = get_object_or_404(Project, pk=view.kwargs['project_pk'])
        liste = ['list', 'retrieve']
        details = ['create', 'destroy']

        if view.action in liste:
            return in_project(request.user, project)
        if view.action in details:
            return request.user == project.author
