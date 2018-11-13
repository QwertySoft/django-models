from django.db import models
from django.utils.timezone import now

class Reporter(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    email = models.EmailField()

    def __str__(self):
        return 'Autor: {}'.format(self.name)

class Question(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    pub_date = models.DateTimeField(blank=True, null=True, default=now)
    reporter = models.ForeignKey(Reporter, null=True, on_delete=models.CASCADE)

    class Meta:
        ordering = ['id', '-pub_date']

    def __str__(self):
        return 'Pregunta: {}'.format(self.name)

class Section(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    questions = models.ManyToManyField(Question)

    def __str__(self):
        return 'Sección: {}'.format(self.name)