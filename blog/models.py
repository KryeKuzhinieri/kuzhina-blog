from django.contrib.auth import get_user_model
from django.db import models
from django.utils.text import slugify
from django.utils.translation import gettext_lazy as _
from django.utils.translation import get_language
from kuzhinablog.settings import LANGUAGES
from ckeditor_uploader.fields import RichTextUploadingField


User = get_user_model()


class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_picture = models.ImageField(_('profile_picture'))

    def __str__(self):
        return self.user.username

    # Adds dynamic model fields for each language (i.e: description_en, description_sq, )
    def add_fields(sender, **kwargs):
        if sender.__name__ == "Author":
            for lan in LANGUAGES:
                model_name = f"description_{lan[0]}"
                fields = [f.name for f in sender._meta.fields]
                if model_name not in fields:
                    field = models.CharField(_(model_name), max_length=255, blank=True, default="")
                    field.contribute_to_class(sender, model_name)

    # It adds the dynamic fields after the class has been prepared.
    models.signals.class_prepared.connect(add_fields)

    class Meta:
        verbose_name = "Author"
        verbose_name_plural = "Authors"


class CategoryManager(models.Manager):
    def get_queryset(self):
        return super(CategoryManager, self).get_queryset().filter(language=get_language())

    @property
    def category_by_language(self):
        return super(CategoryManager, self).get_queryset().filter(categories__in=Category.objects.all())


class Category(models.Model):
    title = models.CharField(_('title'), max_length=20)
    subtitle = models.CharField(_('subtitle'), max_length=255)
    slug = models.SlugField(_('slug'), unique=True)
    thumbnail = models.ImageField(_('thumbnail'))
    language = models.CharField(_('Language'), choices=LANGUAGES, max_length=20, default=LANGUAGES[0])

    objects = CategoryManager()

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
    categories = models.ManyToManyField(Category, related_name="posts")
    featured = models.BooleanField(_('featured'))

    objects = models.Manager()
    custom_manager = CategoryManager()

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Post, self).save(*args, **kwargs)

    class Meta:
        verbose_name = "Post"
        verbose_name_plural = "Posts"
