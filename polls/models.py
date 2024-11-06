import datetime
from distutils.command.upload import upload
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext as _

from io import BytesIO
from PIL import Image
from django.core.files import File

PROGRAM_CHOICES = (
    ('educator', 'Educator Program'),
    ('student', 'Student Program'),
    ('community', 'Community Program'),
    ('$martpath', '$martpath'),
    ('Economics for Empowerment Seminar', 'caset'),
    ('Educator Workshops', 'Educator Workshops'),
    ('National Economics Challenge', 'National Economics Challenge'),
    ('Personal Finance Challenge', 'Personal Finance Challenge'),
    ("The Financial Advisor's Contest", "The Financial Advisor's Contest"),
    ('Family Financial Literacy Event', 'Family Financial Literacy Event'),
    ('Educator Workshops', 'Educator Workshops')
)

def compress(image):
        im = Image.open(image)
        # create a BytesIO object
        im_io = BytesIO() 
        # save image to BytesIO object
        #im = im.resize([500,500])
        im = im.convert("RGB")
        im = im.save(im_io,'JPEG', quality=70) 
        # create a django-friendly Files object
        new_image = File(im_io, name=image.name)
        return new_image

# Create your models here.
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text

class Staff(models.Model):
    name = models.CharField(max_length=50)
    position = models.CharField(max_length=200)
    bio = models.CharField(max_length=1200)
    phone = models.CharField(max_length=20)
    email = models.CharField(max_length=50)
    photo = models.ImageField(upload_to='staff-pics', default="staff-pics/default.jpg")
    

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
            if self.photo:
                if self.photo.size > (300 * 1024):
                    # call the compress function
                    new_photo = compress(self.photo)
                    # set self.image to new_image
                    self.photo = new_photo
                   

            # save
            super().save(*args, **kwargs)

class Director(models.Model):
    name = models.CharField(max_length=50)
    position = models.CharField(max_length=200, blank=True)
    bio = models.CharField(max_length=1200, blank=True)
    phone = models.CharField(max_length=20, blank=True)
    email = models.CharField(max_length=50, blank=True)
    address = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.name

class Officer(models.Model):
    name = models.CharField(max_length=50)
    position = models.CharField(max_length=200, blank=True)
    bio = models.CharField(max_length=1200, blank=True)
    phone = models.CharField(max_length=20, blank=True)
    email = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return self.name

class Event(models.Model):
    name = models.CharField(max_length=200)
    date = models.DateField(_("Date"), default=datetime.date.today)
    end_date = models.DateField(_("End Date"), null=True, blank=True) 
    time = models.TimeField(auto_now=False, auto_now_add=False, null=True, blank=True)
    description = models.CharField(max_length=1200, blank=True)
    tags = models.CharField(max_length=200, default='')
    location = models.CharField(max_length=200, default='Virtual')
    thumb_photo = models.ImageField(upload_to='programs', default="blank.png")
    registration_url = models.CharField(max_length=1200, null=True, blank=True)
    hide_registration_button = models.BooleanField(default=False)
    program = models.CharField(max_length=1200, choices=PROGRAM_CHOICES, null=True, blank=True)
    K_12 = 'K'
    N_12 = 'N'
    S_12 = 'S'
    K_8 = 'I'
    EDUCATOR = 'E'
    GRADE_LEVEL_CHOICES = [
        (K_12, _('K-12th')),
        (N_12, _('9th-12th')),
        (S_12, _('6th-12th')),
        (K_8, _('K-8th')),
        (EDUCATOR, _('Educator'))
    ]
    grade_level = models.CharField(
        max_length=2,
        choices=GRADE_LEVEL_CHOICES,
        default=K_12,
    )

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
            if self.thumb_photo:
                if self.thumb_photo.size > (300 * 1024):
                    # call the compress function
                    new_thumb_photo = compress(self.thumb_photo)
                    # set self.image to new_image
                    self.thumb_photo = new_thumb_photo
                   

            # save
            super().save(*args, **kwargs)

class Contact(models.Model):
    email_address = models.CharField(max_length=200, blank=True, default="")
    content = models.CharField(max_length=10000, blank=True, default="")

    def __str__(self):
        return self.email_address

class News(models.Model):

    hide_banner = models.BooleanField(default=False, blank=True)
    title = models.CharField(max_length=200)
    date = models.DateField(_("Date"), default=datetime.date.today)
    description = models.CharField(max_length=1200, null=True, blank=True)
    tags = models.CharField(max_length=200, default='', blank=True)
    external = models.BooleanField(default=False)
    external_url = models.CharField(max_length=1200, null=True, blank=True)
    
    thumb_photo = models.ImageField(upload_to='programs', default="programs/CCEE_in_the_News.png", blank=True)
    content = models.CharField(max_length=10000, null=True, blank=True)
    banner_photo = models.ImageField(upload_to='programs', default="programs/CCEE_in_the_News.png", blank=True)
    pdf = models.FileField(upload_to='programs', blank=True)

    CCEE_NEWS = 'N'
    MEDIA_RELEASE = 'M'
    OTHER = 'O'
    GRADE_LEVEL_CHOICES = [
        (CCEE_NEWS, _('CCEE in the News')),
        (MEDIA_RELEASE, _('Media Release')),
        (OTHER, _('Other'))
    ]
    category = models.CharField(
        max_length=2,
        choices=GRADE_LEVEL_CHOICES,
        default=CCEE_NEWS,
    )

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
            if self.thumb_photo:
                if self.thumb_photo.size > (300 * 1024):
                    # call the compress function
                    new_thumb_photo = compress(self.thumb_photo)
                    # set self.image to new_image
                    self.thumb_photo = new_thumb_photo
            if self.banner_photo:
                if self.banner_photo.size > (300 * 1024):
                    new_banner_photo = compress(self.banner_photo)
                    self.banner_photo = new_banner_photo
                   

            # save
            super().save(*args, **kwargs)

class Program(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=1200, blank=True)
    dates = models.JSONField(blank=True)
    logo_path = models.ImageField(upload_to='programs', default="staff-pics/default.jpg", blank=True)
    about = models.CharField(max_length=1200)
    show_testimonial = models.BooleanField(default=True)
    testimonial = models.CharField(max_length=1200, blank=True)
    show_video = models.BooleanField(default=True)
    video_path = models.CharField(max_length=200, blank=True)
    show_faq = models.BooleanField(default=True)
    faq = models.JSONField(blank=True)
    show_html_content = models.BooleanField(default=False, null=True)
    html_content = models.CharField(max_length=10000, null=True, blank=True)
    photo_path = models.ImageField(upload_to='programs', default="staff-pics/default.jpg", blank=True)
    banner_photo = models.ImageField(upload_to='programs', default="", blank=True)
    registration_url = models.CharField(max_length=1200, blank=True)
    date = models.DateField(_("Date"), default=datetime.date.today, blank=True)
    grade_range = models.CharField(max_length=150, blank=True)


    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
            if self.logo_path:
                if self.logo_path.size > (300 * 1024):
                    # call the compress function
                    new_logo_path = compress(self.logo_path)
                    # set self.image to new_image
                    self.logo_path = new_logo_path
            if self.banner_photo:
                if self.banner_photo.size > (300 * 1024):
                    new_banner_photo = compress(self.banner_photo)
                    self.banner_photo = new_banner_photo
            if self.photo_path:
                if self.photo_path.size > (300 * 1024):
                    new_photo_path = compress(self.photo_path)
                    self.photo_path = new_photo_path
                   

            # save
            super().save(*args, **kwargs)


class Center(models.Model):
    name = models.CharField(max_length=200)
    region = models.CharField(max_length=200)
    description = models.CharField(max_length=1200)

class Mission(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=1500)

    def __str__(self):
        return self.name

class DailyDose(models.Model):
    topic = models.CharField(max_length=200)
    date = models.DateField(_("Date"), default=datetime.date.today)
    
    tags = models.CharField(max_length=200, default='Daily Dose',  blank=True)

    banner_photo = models.ImageField(upload_to='programs', default="blank.png")
    
    key_question = models.CharField(max_length=2000, null=True)
    key_question_secondary = models.CharField(max_length=2000, null=True, blank=True)
    grade_band = models.CharField(max_length=100, null=True, blank=True)

    show_first_resource =  models.BooleanField( blank=True, default=True)
    first_resource_url = models.CharField(max_length=200, null=True, blank=True)
    first_resource_title = models.CharField(max_length=200, null=True, blank=True)
    first_resource_description = models.CharField(max_length=2000, null=True, blank=True)
    first_resource_image = models.ImageField(upload_to='programs', default="blank.png", blank=True)

    show_second_resource =  models.BooleanField( blank=True, default=True)
    second_resource_url = models.CharField(max_length=200, null=True, blank=True)
    second_resource_title = models.CharField(max_length=200, null=True, blank=True)
    second_resource_description = models.CharField(max_length=2000, null=True, blank=True)
    second_resource_image = models.ImageField(upload_to='programs', default="blank.png", blank=True)

    show_third_resource =  models.BooleanField( blank=True, default=True)
    third_resource_url = models.CharField(max_length=200, null=True, blank=True)
    third_resource_title = models.CharField(max_length=200, null=True, blank=True)
    third_resource_description = models.CharField(max_length=2000, null=True, blank=True)
    third_resource_image = models.ImageField(upload_to='programs', default="blank.png", blank=True)

    show_fourth_resource =  models.BooleanField( blank=True, default=False)
    fourth_resource_url = models.CharField(max_length=200, null=True, blank=True)
    fourth_resource_title = models.CharField(max_length=200, null=True, blank=True)
    fourth_resource_description = models.CharField(max_length=2000, null=True, blank=True)
    fourth_resource_image = models.ImageField(upload_to='programs', default="blank.png", blank=True)

    show_fifth_resource =  models.BooleanField( blank=True, default=False)
    fifth_resource_url = models.CharField(max_length=200, null=True, blank=True)
    fifth_resource_title = models.CharField(max_length=200, null=True, blank=True)
    fifth_resource_description = models.CharField(max_length=2000, null=True, blank=True)
    fifth_resource_image = models.ImageField(upload_to='programs', default="blank.png", blank=True)

    show_sixth_resource =  models.BooleanField( blank=True, default=False)
    sixth_resource_url = models.CharField(max_length=200, null=True, blank=True)
    sixth_resource_title = models.CharField(max_length=200, null=True, blank=True)
    sixth_resource_description = models.CharField(max_length=2000, null=True, blank=True)
    sixth_resource_image = models.ImageField(upload_to='programs', default="blank.png", blank=True)

    


    first_panel_is_image = models.BooleanField( default=True, blank=True)
    first_image = models.ImageField(upload_to='programs', default="blank.png", blank=True)
    

    first_video_path = models.CharField(max_length=200, null=True, blank=True)

    second_panel_is_image = models.BooleanField( default=True, blank=True)
    second_image = models.ImageField(upload_to='programs', default="blank.png", blank=True)

    second_video_path = models.CharField(max_length=200, null=True, blank=True)

    def save(self, *args, **kwargs):
            if self.banner_photo:
                if self.banner_photo.size > (300 * 1024):
                    # call the compress function
                    new_banner_photo = compress(self.banner_photo)
                    #save compressed image
                    self.banner_photo = new_banner_photo
            if self.first_resource_image:
                if self.first_resource_image.size > (300 * 1024):
                    new_first_resource = compress(self.first_resource_image)
                    self.first_resource_image = new_first_resource
            if self.second_resource_image:
                if self.second_resource_image.size > (300 * 1024):
                    new_second_resource = compress(self.second_resource_image)
                    self.second_resource_image = new_second_resource
            if self.third_resource_image:
                if self.third_resource_image.size > (300 * 1024):
                    new_third_resource = compress(self.third_resource_image)
                    self.third_resource_image = new_third_resource
            if self.fourth_resource_image:
                if self.fourth_resource_image.size > (300 * 1024):
                    new_fourth_resource = compress(self.fourth_resource_image)
                    self.fourth_resource_image = new_fourth_resource
            if self.fifth_resource_image:
                if self.fifth_resource_image.size > (300 * 1024):
                    new_fifth_resource = compress(self.fifth_resource_image)
                    self.fifth_resource_image = new_fifth_resource
            if self.sixth_resource_image:
                if self.sixth_resource_image.size > (300 * 1024):
                    new_sixth_resource = compress(self.sixth_resource_image)
                    self.sixth_resource_image = new_sixth_resource

            # save
            super().save(*args, **kwargs)
    

   

    def __str__(self):
        return self.topic

class Donor(models.Model):
    name = models.CharField(max_length=200)
    logo_path = models.ImageField(upload_to='programs', default="staff-pics/default.jpg", blank=True)

    def save(self, *args, **kwargs):
            if self.logo_path:
                if self.logo_path.size > (300 * 1024):
                    # call the compress function
                    new_logo_path = compress(self.logo_path)
                    # set self.image to new_image
                    self.logo_path = new_logo_path
                   

            # save
            super().save(*args, **kwargs)

    def __str__(self):
        return self.name

class SigneeManager(models.Manager):
    def create_signee(self, name, email):
        signee = self.create(name=name, email=email)
        return signee

class Signee(models.Model):
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200, blank=True)
    objects = SigneeManager()

