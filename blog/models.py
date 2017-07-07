from django.db import models
from django.utils import timezone
from django.core.urlresolvers import reverse

class Post(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    slug = models.SlugField('SLUG', unique=True, allow_unicode=True, help_text = 'title alias')
    description = models.CharField('DESCRIPTION', max_length=100, blank=True, help_text = 'description')
    text = models.TextField()
    created_date = models.DateTimeField('Create Date', auto_now_add=True)
    modify_date = models.DateTimeField('Modify Date', auto_now=True)
    published_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        verbose_name = 'post'
        verbose_name_plural = 'posts'
        db_table = 'blog_post'
        ordering = ('-modify_date',)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

    def get_absolute_post(self):
        return reverse('blog:post_detail', args=(self.slug,))

    def get_previous_post(self):
        return self.get_previous_by_modify_date()

    def get_next_post(self):
        return self.get_next_post_by_modify_date()
	
