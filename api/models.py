from django.db import models
from authentication.models import User


class Project(models.Model):
    TYPE_CHOICES = (
        ('backend', 'Back-end'),
        ('frontend', 'Front-end'),
        ('ios', 'iOS'),
        ('android', 'Android'),
    )
    title = models.CharField(max_length=100)
    type = models.CharField(max_length=15, choices=TYPE_CHOICES)
    description = models.TextField(max_length=1000)

    def __str__(self):
        return self.title


class Contributor(models.Model):
    PERMISSION_CHOICES = (
        ('contributor', 'Contributor'),
        ('author', 'Author'),
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    permission = models.CharField(max_length=15, choices=PERMISSION_CHOICES)
    role = models.CharField(max_length=100)

    def __str__(self):
        return self.user.username


class Issue(models.Model):
    PRIORITY_CHOICES = (
        ('faible', 'Faible'),
        ('moyenne', 'Moyenne'),
        ('haute', 'Haute'),
    )
    TAG_CHOICES = (
        ('bug', 'Bug'),
        ('amelioration', 'Amelioration'),
        ('tâche', 'Tâche'),
    )
    STATUS_CHOICES = (
        ('a faire', 'A faire'),
        ('en cours', 'En cours'),
        ('terminé', 'Terminé'),
    )

    title = models.CharField(max_length=100)
    description = models.TextField(max_length=1000)
    tag = models.CharField(max_length=15, choices=TAG_CHOICES)
    priority = models.CharField(max_length=15, choices=PRIORITY_CHOICES)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    status = models.CharField(max_length=15, choices=STATUS_CHOICES)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='author_issue', null=True, blank=True)
    assignee = models.ForeignKey(User, on_delete=models.CASCADE, related_name='assignee', null=True, blank=True)
    created_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Comment(models.Model):
    description = models.TextField(max_length=1000)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='author_comment', null=True, blank=True)
    issue = models.ForeignKey(Issue, on_delete=models.CASCADE, null=True, blank=True)
    created_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.description
