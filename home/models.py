from django.db import models
from accounts.models import User
from django.urls import reverse


class Post(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='posts')
    body = models.TextField()
    slug = models.SlugField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return f'{self.slug} - {self.updated}'

    def get_absolute_url(self):
        return reverse('home:post_detail', args=(self.id, self.slug))

    def likes_count(self):
        return self.plike.count()


class Comment(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='ucomments')
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name='pcomments')
    reply = models.ForeignKey(
        'self', on_delete=models.CASCADE, related_name='rcomments', blank=True, null=True)
    is_reply = models.BooleanField(default=False)
    body = models.TextField(max_length=400)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user} commented {self.body[:30]}'


class Like(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='ulike')
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name='plike')

    def __str__(self):
        return f'{self.user} liked {self.post.slug}'
