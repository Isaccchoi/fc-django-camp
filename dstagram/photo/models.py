# Create your models here.
from io import BytesIO

from PIL import Image
from django.contrib.auth.models import User
from django.core.files.base import ContentFile
from django.db import models
from django.db.models.signals import post_delete
from django.dispatch import receiver


class Photo(models.Model):
    author = models.ForeignKey(User, related_name='photo_posts')
    text = models.TextField()
    photo = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True, default='NoImage.jpg')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-updated',)

    def __str__(self):
        return self.author.username + "-" + self.updated.strftime("%Y-%m-%d %H:%M:%S")

    def save(self, *args, **kwargs):
        is_duplicated = False

        if self.photo:
            try:
                before_obj = Photo.objects.get(id=self.id)
                if before_obj.photo == self.photo:
                    is_duplicated = True
            except:
                pass

        if not is_duplicated:
            # 색 바꿔주는 필터
            image_obj = Image.open(self.photo).convert("L")
            new_image_io = BytesIO()
            image_obj.save(new_image_io, format='JPEG')

            temp_name = self.photo.name
            self.photo.delete(save=False)

            self.photo.save(1
                temp_name,
                content=ContentFile(new_image_io.getvalue()),
                save=False
            )

        try:
            before_obj = Photo.objects.get(id=self.id)
            if before_obj.photo == self.photo or is_duplicated:
                self.photo = before_obj.photo
            else:
                before_obj.photo.delete(save=False)
        except:
            pass

        super(Photo, self).save(*args, **kwargs)


@receiver(post_delete, sender=Photo)
def post_delete(sender, instance, **kwargs):
    storage, path = instance.photo.storage, instance.photo.path
    if (path != '.') and (path != '/') and (path != 'photos/') and (path != 'photos/.'):
        storage.delete(path)
