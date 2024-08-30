from django.db import models

class Comment(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    date_of_birth = models.DateField()
    comment = models.TextField()
    reply = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comment by {self.name} on {self.created_at.strftime('%Y-%m-%d')}"
