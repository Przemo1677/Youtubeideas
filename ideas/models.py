from django.db import models

# Create your models here.
IDEA_STATUS = (
    ('PENDING', 'Pending'),
    ('ACCEPTED', 'Accepted'),
    ('DONE', 'Done'),
    ('REJECTED', 'Rejected')
)


class Idea(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    youtube_url = models.URLField(null=True, blank=True)
    status = models.CharField(max_length=30, choices=IDEA_STATUS, default='PENDING')
    
    def __str__(self):
        return self.title

class Vote(models.Model):
    idea = models.ForeignKey(Idea, on_delete=models.CASCADE)
    reason = models.TextField()
    
    def __str__(self):
        return f'ID {self.id}'
    
