from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_save



class Category(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self) -> str:
        return self.name
    
@receiver(post_save, sender=Category)
def category_dummy(sender, instance, **kwargs):
    category_dummy = Cat_List(name=instance)
    category_dummy.save()

    
class Recipe(models.Model):
    category = models.ForeignKey(Category, related_name='recipe', on_delete=models.DO_NOTHING)
    title = models.CharField(max_length=20)
    description = models.TextField()

    def __str__(self) -> str:
        return self.title
    
class Cat_List(models.Model):
    name = models.OneToOneField(Category, max_length=30, on_delete=models.CASCADE)
    
    def __str__(self) -> str:
        return str(self.name)
