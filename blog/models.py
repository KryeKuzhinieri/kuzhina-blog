from django.contrib.auth import get_user_model
from django.db import models
from django.utils.text import slugify
from django.utils.translation import gettext_lazy as _
from kuzhinablog.settings import LANGUAGES
from ckeditor_uploader.fields import RichTextUploadingField


User = get_user_model()


class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_picture = models.ImageField(_('profile_picture'))

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name = "Author"
        verbose_name_plural = "Authors"


class Category(models.Model):
    title = models.CharField(_('title'), max_length=20)
    subtitle = models.CharField(_('subtitle'), max_length=20)
    slug = models.SlugField(_('slug'), unique=True)
    thumbnail = models.ImageField(_('thumbnail'))
    language = models.CharField(_('Language'), choices=LANGUAGES, max_length=20, default=LANGUAGES[1])

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Category, self).save(*args, **kwargs)

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"


class Post(models.Model):
    title = models.CharField(_('title'), max_length=100)
    slug = models.SlugField(_('slug'), unique=True, max_length=100)
    overview = models.TextField(_('overview'))
    timestamp = models.DateTimeField(_('timestamp'), auto_now_add=True)
    content = RichTextUploadingField(
        _('content'),
        external_plugin_resources=[
            (
                "youtube",
                "/static/editor_plugins/ckeditor-youtube-plugin/youtube/",
                "plugin.js"
            ),
            (
                "markdown",
                "/static/editor_plugins/CKEditor-Markdown-Plugin/markdown/",
                "plugin.js"
            ),
        ],
    )
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    thumbnail = models.ImageField(_('thumbnail'))
    categories = models.ManyToManyField(Category)
    featured = models.BooleanField(_('featured'))

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Post, self).save(*args, **kwargs)

    class Meta:
        verbose_name = "Post"
        verbose_name_plural = "Posts"

