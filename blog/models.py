from django.db import models
from django.contrib.auth.models import User
import  os
# Create your models here.
def user_directory_path(instance, filename):
    # File will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return 'user_{0}/{1}'.format(instance.created_by.id, filename)

class PostsModel(models.Model):
    created_by = models.ForeignKey(to=User, on_delete=models.CASCADE, default="")
    posted_date = models.DateField(auto_now=True)
    title = models.CharField(max_length=50)
    content = models.CharField(max_length=1000)
    image = models.ImageField(upload_to=user_directory_path, null=True, blank=True)

    def delete(self, *args, **kwargs):
        if self.image:
            if os.path.isfile(self.image.path):
                os.remove(self.image.path)
        super().delete(*args, **kwargs)

    def __str__(self):
        return "{}:{}:{}".format(self.title, self.created_by, self.posted_date)
