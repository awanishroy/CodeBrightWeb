from django.db import models

# Class Level Model
class CbtClasses(models.Model):
    PR_CLASS_ID = models.AutoField(primary_key=True)
    PR_CLASS_NAME = models.CharField(max_length=100)
    # Timestamps
    PR_CREATED_AT = models.DateTimeField(auto_now_add=True)
    PR_MODIFIED_AT = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'cbt_classes'

# Board Model
class CbtBoard(models.Model):
    PR_BOARD_ID = models.AutoField(primary_key=True)
    PR_BOARD_NAME = models.CharField(max_length=100)
    # Timestamps
    PR_CREATED_AT = models.DateTimeField(auto_now_add=True)
    PR_MODIFIED_AT = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'cbt_board'

# Series Model (Updated)
class CbtSeries(models.Model):
    PR_SERIES_ID = models.AutoField(primary_key=True)
    PR_SERIES_NAME = models.CharField(max_length=255)
    # Relationships
    PR_BOARD = models.ForeignKey(CbtBoard, on_delete=models.SET_NULL, null=True, blank=True)
    # Many-to-Many Relationship with CbtClasses
    PR_CLASSES = models.ManyToManyField(CbtClasses, through='CbtSeriesClass', related_name='series')
    # Timestamps
    PR_CREATED_AT = models.DateTimeField(auto_now_add=True)
    PR_MODIFIED_AT = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'cbt_series'


# Pivot Table (CbtSeriesClass)
class CbtSeriesClass(models.Model):
    PR_SERIES_CLASS_ID = models.AutoField(primary_key=True)
    PR_CLASS = models.ForeignKey(CbtClasses, on_delete=models.CASCADE)
    PR_SERIES = models.ForeignKey(CbtSeries, on_delete=models.CASCADE)
    # Additional fields can be added here if needed (e.g., timestamps, metadata)
    PR_CREATED_AT = models.DateTimeField(auto_now_add=True)
    PR_MODIFIED_AT = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'cbt_series_class'
        unique_together = ('PR_CLASS', 'PR_SERIES')  # Ensures uniqueness between the class and series pair

# Author Model
class CbtAuthor(models.Model):
    PR_AUTHOR_ID = models.AutoField(primary_key=True)
    PR_AUTHOR_NAME = models.CharField(max_length=255)
    # Timestamps
    PR_CREATED_AT = models.DateTimeField(auto_now_add=True)
    PR_MODIFIED_AT = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'cbt_author'

# Edition Model
class CbtEdition(models.Model):
    PR_EDITION_ID = models.AutoField(primary_key=True)
    PR_EDITION_NAME = models.CharField(max_length=50)
    # Timestamps
    PR_CREATED_AT = models.DateTimeField(auto_now_add=True)
    PR_MODIFIED_AT = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'cbt_edition'

# Imprint Model
class CbtImprint(models.Model):
    PR_IMPRINT_ID = models.AutoField(primary_key=True)
    PR_IMPRINT_NAME = models.CharField(max_length=255)
    # Timestamps
    PR_CREATED_AT = models.DateTimeField(auto_now_add=True)
    PR_MODIFIED_AT = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'cbt_imprint'

# Book Type Model
class CbtBookType(models.Model):
    PR_BOOK_TYPE_ID = models.AutoField(primary_key=True)
    PR_BOOK_NAME = models.CharField(max_length=255)
    # Timestamps
    PR_CREATED_AT = models.DateTimeField(auto_now_add=True)
    PR_MODIFIED_AT = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'cbt_book_type'

# Main Data Model (CbtExcelData)
class CbtBookData(models.Model):
    PR_BOOK_ID = models.AutoField(primary_key=True)

    # Title Information
    PR_TITLE = models.CharField(max_length=255, null=True, blank=True)
    PR_SUB_TITLE = models.CharField(max_length=255, null=True, blank=True)

    # ISBN
    PR_ISBN = models.CharField(max_length=255, null=True, blank=True)

    # ForeignKey Relationships
    PR_SERIES = models.ForeignKey(CbtSeries, on_delete=models.SET_NULL, null=True, blank=True)
    PR_AUTHOR = models.ForeignKey(CbtAuthor, on_delete=models.SET_NULL, null=True, blank=True)
    PR_EDITION = models.ForeignKey(CbtEdition, on_delete=models.SET_NULL, null=True, blank=True)
    PR_IMPRINT = models.ForeignKey(CbtImprint, on_delete=models.SET_NULL, null=True, blank=True)

    # Classification Information
    PR_BOOK_TYPE = models.CharField(max_length=100, null=True, blank=True)
    PR_BOOK_NUMBER = models.IntegerField(null=True, blank=True)
    PR_CLASS_LEVEL = models.CharField(max_length=100, null=True, blank=True)
    PR_PRODUCT_DIVISION = models.CharField(max_length=100, null=True, blank=True)
    PR_BROAD_SUBJECT = models.CharField(max_length=255, null=True, blank=True)
    PR_DETAILED_SUBJECT = models.CharField(max_length=255, null=True, blank=True)

    # Book Details
    PR_BOOK_CODE = models.CharField(max_length=100, null=True, blank=True)
    PR_COPYRIGHT = models.CharField(max_length=50, null=True, blank=True)
    PR_DATE_OF_RELEASE = models.DateField(null=True, blank=True)
    PR_BINDING = models.CharField(max_length=50, null=True, blank=True)
    PR_LANGUAGE = models.CharField(max_length=50, null=True, blank=True)
    PR_PAGES = models.IntegerField(null=True, blank=True)
    PR_TRIM_SIZE = models.CharField(max_length=50, null=True, blank=True)
    PR_WEIGHT = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    PR_LIST_PRICE = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    PR_DISCOUNT = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)

    # Description and Additional Info
    PR_PRODUCT_DESCRIPTION = models.TextField(null=True, blank=True)
    PR_COMPANY = models.CharField(max_length=255, null=True, blank=True)

    # Timestamps
    PR_CREATED_AT = models.DateTimeField(auto_now_add=True)
    PR_MODIFIED_AT = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'cbt_book_data'
