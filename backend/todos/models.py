from django.db import models


class Todo(models.Model):

    title = models.CharField(max_length=120)

    description = models.TextField(blank=True, null=True)

    status = models.TextField(blank=True, null=True, default='TODO')

    # methods
    def get_summary(self):
        summary = self.title + ' - ' + self.description + ' - ' + self.status
        return summary