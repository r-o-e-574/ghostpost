from django.db import models
from django.utils import timezone

# Create your models here.
class BoastRoast(models.Model):
    roast_boast = ((True, 'Boast'), (False, 'Roast'))
    choices = models.BooleanField(choices=roast_boast, default=True)
    user_input = models.CharField(max_length=240, default='')
    upvotes = models.IntegerField(default=0)
    downvotes = models.IntegerField(default=0)
    time_posted = models.DateTimeField(default=timezone.now) 
    @property
    def totalvotes(self):
        return self.upvotes - self.downvotes