from django.db import models

# Create your models here.

CATEGORY_CHOICES = (
    ("Web Development", "WD"),
    ("Desktop Development", "DD")
)
class Post(models.Model):
    title = models.CharField(max_length=50, unique= True)
    content = models.TextField(max_length=10000)
    created_at = models.DateTimeField()


    published = models.BooleanField(default=True)
    email = models.EmailField(max_length=50)
    views_count = models.IntegerField(default=0)
    #Email = models.EmailField(max_length=50, null=True, blank=True)

    Category = models.CharField(choices= CATEGORY_CHOICES, max_length=50)


    def __str__(self):
        return self.title



