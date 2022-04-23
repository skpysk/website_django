from django.db import models

class blogpost(models.Model):
    post_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=50)
    headzero = models.CharField(max_length=500,default="")
    cheadzero = models.CharField(max_length=500,default="")
    headone = models.CharField(max_length=500,default="")
    cheadone = models.CharField(max_length=500,default="")
    headtwo = models.CharField(max_length=500,default="")
    cheadtwo = models.CharField(max_length=500,default="")
    publish_date = models.DateField()
    thumbnail = models.ImageField(upload_to ="shop/images", default="")

    def __str__(self) -> str:  # yeh krne se udher database me product ka name ayega simple default object ne ayega
        return self.title