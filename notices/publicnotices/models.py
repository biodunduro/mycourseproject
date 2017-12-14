from django.db import models
#from django.urls import reverse
from django.contrib.auth.models import User







class Medium(models.Model):
    publication_name = models.CharField(max_length = 125)
    date_published = models.DateTimeField(null=True, blank=True)


    def __str__(self):

        return self.publication_name




class Advertiser(models.Model):
    """
    Model representing an advertiser.
    """
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    company = models.CharField(max_length=500, null=True, blank=True)
    designation = models.CharField(max_length=500, null=True, blank=True)
    date_of_birth = models.DateField(null=True, blank=True)
    date_of_death = models.DateField('Died', null=True, blank=True)
    
    # def get_absolute_url(self):
    #     """
    #     Returns the url to access a particular advertiser instance.
    #     """
    #     return reverse('advertiser', args=[str(self.id)])
    

    def __str__(self):
        """
        String for representing the Model object.
        """
        return self.last_name



# class PostImage(models.Model):
#     image = models.FileField(upload_to='post/images')







class PublicNotice(models.Model):
    title = models.CharField(max_length = 255)
    body = models.TextField(max_length = 2000)
    posted_by = models.CharField(max_length=125)
    date_posted = models.DateTimeField(auto_now_add = True)
    category = models.CharField(max_length = 125)
    advertiser = models.ForeignKey('Advertiser', on_delete=models.SET_NULL, null=True)
    medium = models.ForeignKey('Medium', on_delete=models.SET_NULL, null=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, null = True)


    
    

    def __str__(self):
        return self.title


    # def get_absolute_url(self):
    #     """
    #     Returns the url to access a particular notice instance.
    #     """
    #     return reverse('publicnotice', args=[str(self.id)])

class Entry(models.Model):
    publicnotice = models.ForeignKey(PublicNotice)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)


    class Meta:
        verbose_name_plural = 'entries'

    def __str__(self):
        return self.text[:50] + "..."





# class PublicNoticeInstance(models.Model):
#     id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text="Unique ID for this particular Public Notice")
#     publicnotice = models.ForeignKey('PublicNotice', on_delete=models.SET_NULL, null=True)
#     when_published = models.DateTimeField(null=True, blank=True)
#     where_published = models.ForeignKey('Medium', on_delete=models.SET_NULL, null=True)





