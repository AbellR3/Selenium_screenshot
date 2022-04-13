from django.db import models


class Page(models.Model):
    page_title = models.CharField(max_length=600)
    page_url = models.URLField()

    def __str__(self):
        return self.page_title
    
class Element(models.Model):
    selector_name = models.CharField(max_length=100)
    page = models.ForeignKey(Page, on_delete=models.CASCADE)
    SELECTOR = (('id', 'id'), 
                ('class name', 'class name'),
                ('XPATH', 'XPATH'),
                ('tag name', 'tag name'))
    selector_type = models.CharField(max_length=50, choices = SELECTOR)
    selector_text = models.CharField(max_length=300, default=None)


    def __str__(self):
        return self.selector_name
