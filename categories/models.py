from django.db import models


class Categories(models.Model):
    """Database Model for products categories.

    This model represents a product category in the database.
    Each category has a unique name, and opcional description,
    a unique slug for the url and an opcional associated image.

    Fields:
        - name_category (CharField): Unique name of the category.
        Max length = 30.
        - description (CharField): Optional description of the category. 
        Max length = 255.
        - slug (CharField): Unique slug for the category URL.
        Max length = 100.
        - image (ImageField): Optional image associated with
        the category. Stored in 'photos/categories'.

    """
    name_category = models.CharField(max_length=30, unique=True)
    description = models.CharField(max_length=255, blank=True)
    slug = models.CharField(max_length=100, unique=True)
    image = models.ImageField(upload_to='photos/categories', blank=True)

    class Meta:
        verbose_name_plural = 'categories'

    def __str__(self):
        """Returns a human-readable representation of the Categories object,
        which in this case is the name of the category. """
        return self.name_category
