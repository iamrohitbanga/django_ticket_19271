from django.db import models

class BaseGroup(models.Model):
    name = models.CharField("Group Name", max_length=50)
    def __unicode__(self):
        return self.name
    class Meta:
        abstract = True

class BaseModel(models.Model):
    my_id = models.CharField("My Unique Id", max_length=50)
    name = models.CharField("Name", max_length=30)

    def __unicode__(self):
        return self.my_id

    class Meta:
        abstract = True

class MyGroup(BaseGroup):
    class Meta:
        verbose_name = "My Group"
        verbose_name_plural = "My Groups"

class MyModel(BaseModel):
    group = models.ForeignKey(MyGroup, related_name="mymodels")
    class Meta:
        verbose_name = "My Model"
        verbose_name_plural = "My Models"
    
