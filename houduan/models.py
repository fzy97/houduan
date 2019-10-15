from django.db import models

class topic_reference(models.Model):
    item1 = models.CharField(max_length=255, verbose_name='item1')
    item2 = models.CharField(max_length=255, verbose_name='item2')
    item3 = models.CharField(max_length=255, verbose_name='item3')

    class Meta:
        db_table = 'topic_reference'
        verbose_name = 'topic_reference'
        verbose_name_plural = verbose_name


class topic_model(models.Model):
    topic1 = models.CharField(max_length=255, verbose_name='topic1')

    class Meta:
        db_table = 'topic_model'
        verbose_name = 'topic_model'
        verbose_name_plural = verbose_name


class als(models.Model):
    reviewer_id = models.CharField(max_length=255, verbose_name='reviewer_id')
    listing_id1 = models.CharField(max_length=255, verbose_name='listing_id1')
    listing_id2 = models.CharField(max_length=255, verbose_name='listing_id2')
    listing_id3 = models.CharField(max_length=255, verbose_name='listing_id3')

    class Meta:
        db_table = 'als'
        verbose_name = 'als'
        verbose_name_plural = verbose_name
    def __str__(self):
        return self.reviewer_id

class simi(models.Model):
    item1 = models.CharField(max_length=255, verbose_name='item1')
    item2 = models.CharField(max_length=255, verbose_name='item2')
    item3 = models.CharField(max_length=255, verbose_name='item3')

    class Meta:
        db_table = 'simi'
        verbose_name = 'simi'
        verbose_name_plural = verbose_name

class loginuser(models.Model):
    username = models.CharField(max_length=20, verbose_name='username')
    password = models.CharField(max_length=20, verbose_name='password')

    class Meta:
        db_table = 'loginuser'
        verbose_name = 'loginuser'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.username

class listings(models.Model):

    #id = models.CharField(max_length=100, verbose_name='id')
    listing_url = models.CharField(max_length=200, verbose_name='listing_url')
    picture_url = models.CharField(max_length=200, verbose_name='picture_url')
    name = models.CharField(max_length=100, verbose_name='name')
    price = models.CharField(max_length=100, verbose_name='price')
    neighbourhood_group_cleansed = models.CharField(max_length=100, verbose_name='neighbourhood_group_cleansed')
    neighbourhood_cleansed = models.CharField(max_length=100, verbose_name='neighbourhood_cleansed')
    review_scores_rating = models.IntegerField()
    accommodates = models.IntegerField()
    room_type = models.CharField(max_length=100, verbose_name='room_type')
    host_id = models.CharField(max_length=100, verbose_name='host_id')
    host_name = models.CharField(max_length=100, verbose_name='host_name')
    availability_365 = models.CharField(max_length=100, verbose_name='availability_365')
    amenities = models.TextField(verbose_name ='amenities')
    description = models.TextField(verbose_name='description')
    bedrooms = models.CharField(max_length=100, verbose_name='bedrooms')
    bathrooms = models.CharField(max_length=100, verbose_name='bathrooms')
    last_review = models.CharField(max_length=100, verbose_name='last_review')
    minimum_nights = models.CharField(max_length=100, verbose_name='minimum_nights')
    number_of_reviews = models.CharField(max_length=100, verbose_name='number_of_reviews')
    reviews_per_month = models.CharField(max_length=100, verbose_name='reviews_per_month')
    calculated_host_listings_count = models.CharField(max_length=100, verbose_name='calculated_host_listings_count')
    price_adjust = models.IntegerField()

    class Meta:
        db_table = 'listings'
        verbose_name = 'listing'
        verbose_name_plural = verbose_name
    def __str__(self):
        return self.id