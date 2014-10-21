from django.db import models

# Create your models here.

class base_project(models.Model):
    """
    Base module for all the classes in project app.
    """
    title = models.CharField(max_length=200, blank=False, null=False)
    description = models.CharField(max_length=200)
    creation_date = models.DateTimeField('date published')
    modified_date = models.DateTimeField('date published')
    creation_by = models.CharField(max_length=200)
    modified_by = models.CharField(max_length=200)
    state = models.IntegerField(blank=False, null=False, default=0)


class Company(base_project):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')


class BusinessUnit(base_project):
    question = models.ForeignKey('Company')
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')


class Project(base_project):
    question = models.ForeignKey('BusinessUnit')
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')


class Milestone(base_project):
    question = models.ForeignKey(Project)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)


class Task(base_project):
    question = models.ForeignKey('Milestone')
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    starts_after = models.ForeignKey('Task')