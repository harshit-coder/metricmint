from django.db import models
from django.utils.timezone import now
from PIL import Image
from PIL import ImageFilter
import os
from django.conf import settings

# Create your models here.

RESOURCE_DIR=os.path.join(settings.MEDIA_ROOT,'images')
print(RESOURCE_DIR)

def path_and_rename(instance, filename):
    upload_to = 'images'
    ext = filename.split('.')[-1]
    fname = filename.split('.')[-2]
    filename = '{}_{}.{}'.format(fname,instance.code, ext)
    return os.path.join(upload_to, filename)



STAT_CHOICES = [
    ("by CSV", "by CSV"),
    ("by entering points", "by entering points"),
    ("by table image", "by table image"),

]

INFO_CHOICES = [
                   ("upload  image from database", "upload image from database"),
                   ("upload image from your device", "upload image from your device "),
                   ("upload link", "upload link"),

                    ]


G_CHOICES=[

    ('bar','bar'),
    ('pie','pie'),
    ('scatter','scatter'),
    ('cylinder','cylinder'),
    ('funnel3d','funnel3d'),
    ('pyramid3d','pyramid3d'),
    ('gauge','gauge'),
    ('area','area'),
    ('areaspline','areaspline'),
    ('bullet','bullet'),
    ('column','column'),
    ('columnpyramid','columnpyramid'),
    ('dependencywheel','dependencywheel'),
    ('dumbbell','dumbbell'),
    ('heatmap','heatmap'),
    ('histogram','histogram'),
    ('item','item'),
    ('line','line'),
    ('lollipop','lollipop'),
    ('networkgraph','networkgraph'),
    ('packedbubble','packedbubble'),
    ('spline','spline'),
    ('wordcloud','wordcloud'),
    ('columnrange','columnrange'),
    ('spline','spline'),
    ('streamgraph','streamgraph'),
    ("sunburst","sunburst"),
    ('tilemap','tilemap'),
    ('timeline','timeline'),
    ("treemap", "treemap"),
    ('variablepie','variablepie'),
    ('variwide','variwide'),
    ('vector','vector'),
    ('venn','venn'),
    ('xrange','xrange'),

    
]

class codes_list(models.Model):
    co =models.CharField(max_length=900,primary_key = True)

    def __str__(self):
        return str(self.co)



class country(models.Model):
    Country=models.CharField(max_length=100,default="ALL",unique = True)

    def __str__(self):
        return self.Country

class cat(models.Model):
    category = models.CharField(max_length=100,default="ALL",unique = True)

    def __str__(self):
        return self.category
    


class stat(models.Model):
    s_Category = models.ForeignKey("cat", on_delete=models.CASCADE,blank=True)
    s_subcategory=models.CharField(max_length=100,null=True,blank=True)
    graph=models.CharField(max_length=100,choices=G_CHOICES,default="bar",blank=True)
    graph_tittle=models.CharField(max_length=100,null=True,blank=True)
    x_axistittle=models.CharField(max_length=100,null=True,blank=True)
    y_axistittle=models.CharField(max_length=100,null=True,blank=True)
    s_csv=models.TextField(blank = True,null = True)
    s_head_tittle=models.CharField(max_length=50,null=True,blank=True)
    s_head_subtittle=models.CharField(max_length=100,null=True,blank=True)
    s_date=models.DateField(default=now())
    s_publisher=models.CharField(max_length=100,blank=True,null=True)
    s_count=models.ForeignKey("country", on_delete=models.CASCADE,blank=True, null=True)
    s_src1=models.URLField(max_length=200,blank=True)
    desc1=models.TextField(blank=True)
    name = models.CharField ( max_length = 100 , null = True , blank = True )
    x_pts = models.TextField ( blank = True, null = True )
    y_pts = models.TextField ( blank = True,null = True )
    y_pts1 = models.TextField(blank = True,null = True)
    y_pts2 = models.TextField ( blank = True,null = True )
    y_pts3 = models.TextField(blank = True,null = True)
    y_pts4 = models.TextField ( blank = True,null = True )
    y_pts5 = models.TextField(blank = True,null = True)
    name1 = models.CharField ( max_length = 100 , null = True , blank = True )
    name2 = models.CharField ( max_length = 100 , null = True , blank = True )
    name3 = models.CharField ( max_length = 100 , null = True , blank = True )
    name4 = models.CharField ( max_length = 100 , null = True , blank = True )
    name5 = models.CharField ( max_length = 100 , null = True , blank = True )





    def __str__(self) :
        return self.s_head_tittle




class infog(models.Model):
    i_category=models.ForeignKey("cat", on_delete=models.CASCADE,blank=True)
    i_subcategory=models.CharField(max_length=100,blank=True)
    image_tittle=models.CharField(max_length=100,blank=True,null = True)
    imageurl1=models.URLField(max_length=200,blank=True,null = True)
    i_head_tittle=models.CharField(max_length=100,blank=True)
    i_sub_tittle=models.CharField(max_length=100,blank=True)
    i_publisher=models.CharField(max_length=100,default="Ankit Kalucha")
    i_date=models.DateField(default=now())
    i_image=models.ImageField(upload_to="images/",blank=True,null = True)
    i_src1=models.URLField(max_length=200,blank=True)
    i_count=models.ForeignKey("country", on_delete=models.CASCADE,blank=True, null=True)
    image2field =models.FilePathField(path= RESOURCE_DIR,recursive=True,max_length=200,null=True)
    desc2=models.TextField(blank=True)
    def url(self):
        path = self._meta.get_field('image2field').path
        return self.image2field.replace(path, '',1)



    def save(self):
        super().save()
        img=Image.open(self.i_image.path)
        if img.height >300 or img.width >300:
            new_img =(300,300)
            img.thumbnail(new_img)
            img.save(self.i_image.path)

    def __str__(self):
        return self.i_head_tittle

class search1(models.Model):
    searches= models.CharField(max_length=1000,null=True)
    c_ountry=models.ForeignKey("country", on_delete=models.CASCADE,null=True)
    c_ategory=models.ForeignKey("cat", on_delete=models.CASCADE,null=True)
  
    

class searchenter(models.Model):
    searc= models.CharField(max_length=1000,null=True)
    d = models.DateTimeField(default= now())

    def __str__(self) :
        return self.searc
    

class Multiple_images(models.Model):
    tittle=models.CharField(max_length=200,blank=True,null=True)
    image=models.ImageField(upload_to=path_and_rename,blank=True,null=True)
    code = models.ForeignKey("codes_list", on_delete=models.CASCADE,null=True,db_column = 'co')
    date_inp= models.DateTimeField(default= now())    

    def save(self):
        super().save()
        img=Image.open(self.image.path)
        if img.height >300 or img.width >300:
            new_img =(300,300)
            img.thumbnail(new_img)
            img.save(self.image.path)

    def __str__(self):
        return str(self.code)


