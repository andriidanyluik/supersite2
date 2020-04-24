from django.conf import settings
from django.db import models
from django.utils import timezone


class Post_Admin(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title


class Post_Program(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title




class Comment_ad(models.Model):
	article = models.ForeignKey(Post_Admin, on_delete = models.CASCADE)
	author_name = models.CharField("ім'я автора", max_length = 50)
	comment_text = models.CharField('текст коментаря', max_length = 200)

	def __str__(self):
		return self.author_name

	class Meta:
		verbose_name = 'Коментар'
		verbose_name_plural = 'Коментарі'





class Comment_pg(models.Model):
	article = models.ForeignKey(Post_Program, on_delete = models.CASCADE)
	author_name = models.CharField("ім'я автора", max_length = 50)
	comment_text = models.CharField('текст коментаря', max_length = 200)

	def __str__(self):
		return self.author_name

	class Meta:
		verbose_name = 'Коментар'
		verbose_name_plural = 'Коментарі'