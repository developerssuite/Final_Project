from django.contrib.auth.models import Permission, User
from django.contrib.contenttypes.fields import GenericRelation
from django.db import models
from hitcount.models import HitCount
from django.core.urlresolvers import reverse
from django.utils import timezone
from django.contrib.auth.models import User
from django_comments.moderation import CommentModerator
from django_comments_xtd.moderation import moderator
import secretballot


class Product(models.Model):
    user = models.ForeignKey(User, default=1, on_delete=models.CASCADE)
    title = models.CharField(max_length=250)
    url = models.CharField(max_length=250)
    category = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    product_logo = models.FileField()
    created_at = models.DateTimeField(auto_now_add=True)
    hit_count_generic = GenericRelation(
        HitCount, object_id_field='object_pk',
        related_query_name='hit_count_generic_relation')

    def get_absolute_url(self):
        return reverse('products:detail',
                       kwargs={'product_id': self.pk})

    def __str__(self):
        return self.title + ' - ' + str(self.id)


class NewsLetter(models.Model):
    email = models.CharField(max_length=250)

    def __str__(self):
        return self.email


class ContactUs(models.Model):
    name = models.CharField(max_length=250)
    email = models.CharField(max_length=250)
    phoneNumber = models.IntegerField()
    company = models.CharField(max_length=250)
    message = models.CharField(max_length=1000)

    def __str__(self):
        return self.name


class PublicManager(models.Manager):
    def get_queryset(self):
        return super(PublicManager, self).get_queryset() \
            .filter(publish__lte=timezone.now())


class Post(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250, unique_for_date='publish')
    body = models.TextField()
    allow_comments = models.BooleanField('allow comments', default=True)
    publish = models.DateTimeField(default=timezone.now)
    objects = PublicManager()  # Our custom manager.

    class Meta:
        ordering = ('-publish',)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('products:detail',  # have a model change here --- Commenting
                       kwargs={'year': self.publish.year,
                               'month': self.publish.strftime('%b'),
                               'day': self.publish.strftime('%d'),
                               'slug': self.slug})


class PostCommentModerator(CommentModerator):
    email_notification = True
    auto_moderate_field = 'publish'
    moderate_after = 365  # Number of days the product is old after which if someone do commenting then it will be
    # moderated


class Categories(models.Model):
    category = models.CharField(max_length=100)

    def __str__(self):
        return self.category


moderator.register(Post, PostCommentModerator)


secretballot.enable_voting_on(Product)


