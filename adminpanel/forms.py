from stats.models import *
from django import forms
from django.forms import ClearableFileInput,ModelChoiceField
from django.forms import ModelForm
from adminpanel.views import *


class new_country(forms.ModelForm):
    class Meta:
        model = country
        fields = ("__all__")
        labels = {'Country':"ENTER COUNTRY NAME:-"}
        Country=forms.CharField(max_length=900,required=True)
        widgets={'Country':forms.TextInput(attrs={'class':'form-control','placeholder':'country'})

}


class add_cat(forms.ModelForm):
    class Meta:
        model = cat
        fields =('__all__')
        labels = {'category':"ENTER CATEGORY NAME:-"}
        category = forms.CharField(max_length=900,required = True)
        widgets ={ 'category':forms.TextInput(attrs={'class':'form-control','placeholder':'category'})
}


class mutiple_imagesselectform(forms.ModelForm):
    class Meta:
        model = Multiple_images
        fields = ['tittle','image','code']
        labels = {'tittle':"ENTER BOOK TITTLE:-",'image':"UPLOAD IMAGES:-",'code':"ENTER  UNIQUE CODE:-"}
        tittle = forms.CharField(max_length=900, required=True),
        image = forms.ImageField(max_length=900,required=True),
        code=   forms.ModelChoiceField(queryset = codes_list.objects.values_list('co',flat=True),required = True)
        widgets= { 'tittle':forms.TextInput(attrs={'class':'form-control','placeholder':'book tittle'}),
                    'image':forms.ClearableFileInput(attrs={'class':'','multiple':True,'placeholer':'choose files',}),
                    'code':forms.Select(attrs={'class':'browser-default custom select','placeholder':'code'})


}


class statfile_form(forms.ModelForm):
    class Meta:
        model= stat
        fields =['graph_tittle','s_Category','s_subcategory','graph','x_axistittle','y_axistittle','s_csv','s_head_tittle','s_head_subtittle','s_count','s_count','s_src1','desc1','s_publisher']
        labels ={'graph_tittle':"ENTER GRAPH NAME:-",'s_publisher':"ENTER PUBLISHER NAME:-",'desc1':"ENTER KEYWORDS:-",'s_src1':"ENTER SOURCE LINK 1:-",'s_count':"CHOOSE COUNTRY:-",'s_head_subtittle':"ENTER SUBTITTLE:-",'s_Category':"CHOOSE CATEGORY:-",'s_subcategory':"ENTER SUBCATEGORY:-",'graph':"CHOOSE GRAPH TYPE:-",'x_axistittle':"ENTER X AXIS TITTLE:-",'y_axistittle':"ENTER Y AXIS TITTLE:-",'s_csv':"CHOOSE FILE:-" ,'s_head_tittle':"ENTER HEADING:-"}
       
        s_category=forms.ModelChoiceField(queryset=cat.objects.all(),required=True),
        s_subcategory=forms.CharField(max_length=900,required=False),
        graph =forms.ChoiceField(choices=G_CHOICES,required=True),
        x_axistittle=forms.CharField(max_length=900,required=False),
        y_axistittle=forms.CharField(max_length=900,required=False),
        s_csv=forms.CharField(required = True)
        s_head_tittle=forms.CharField(max_length=900,required=False),
        s_head_subtittle=forms.CharField(max_length=900,required=False),
        s_count=forms.ModelChoiceField(queryset=country.objects.all(),required=False),
        s_src1= forms.URLField(required=False),
        desc1=forms.CharField(required=False),
        s_publisher=forms.CharField(max_length=900,required=False),
        graph_tittle=forms.CharField(max_length=900, required=False)

        widgets ={
        's_category':forms.Select(attrs={'class':'browser-default custom select','placeholder':"ALL"}),
        's_subcategory':forms.TextInput(attrs={'class':'form-control','placeholder':'Subcategory'}),
        'graph' :forms.Select(attrs={'class':"browser-default custom-select",'placeholder':'bar'}),
        'x_axistittle':forms.TextInput(attrs={'class':'form-control','placeholder':'X_axis tittle'}),
        'y_axistittle':forms.TextInput(attrs={'class':'form-control','placeholder':'Y_axis tittle'}),
        's_csv':forms.Textarea(attrs = {'class':'exampleFormControlTextarea4','placeholder':"copy your csv data"}),
        's_head_tittle':forms.TextInput(attrs={'class':'form-control','placeholder':'heading'}),
        's_head_subtittle':forms.TextInput(attrs={'class':'form-control','placeholder':'subtittle'}),
        's_count':forms.Select(attrs={'class':'browser-default custom select','placeholder':"ALL"}),
        's_src1':forms.URLInput(attrs={'class':'form-control','placeholder':'https://maps.google.com/'}),
        'desc1':forms.Textarea(attrs = {'class':'exampleFormControlTextarea4','placeholder':"keyword1 keyword2 (don't use comma or any symbol)"}),
        's_publisher':forms.TextInput(attrs={'class':'form-control','placeholder':'publisher'}),
        'graph_tittle':forms.TextInput(attrs={'class':'form-control','placeholder':'graph tittle'}),


}
                  


class statpoint_form(forms.ModelForm):
    class Meta:
        model= stat
        fields =['graph_tittle','s_Category','s_subcategory','graph','x_axistittle','y_axistittle','s_head_tittle','s_head_subtittle','s_count','s_count','s_src1','desc1','s_publisher','name','name1','name2','name3','name4','name5','x_pts','y_pts','y_pts1','y_pts2','y_pts3','y_pts4','y_pts5']
        labels ={'name': "ENTER Y-SET NAME:-", 'x_pts':"ENTER X-AXIS POINTS:-" ,'y_pts': "ENTER Y-AXIS POINTS:-",'graph_tittle':"ENTER GRAPH NAME:-",'s_publisher':"ENTER PUBLISHER NAME:-",'desc1':"ENTER KEYWORDS:-",'s_src1':"ENTER SOURCE LINK 1:-",'s_count':"CHOOSE COUNTRY:-",'s_head_subtittle':"ENTER SUBTITTLE:-",'s_Category':"CHOOSE CATEGORY:-",'s_subcategory':"ENTER SUBCATEGORY:-",'graph':"CHOOSE GRAPH TYPE:-",'x_axistittle':"ENTER X AXIS TITTLE:-",'y_axistittle':"ENTER Y AXIS TITTLE:-",'s_head_tittle':"ENTER HEADING:-" ,'y_pts1': "ENTER Y-AXIS POINTS:-",'y_pts2': "ENTER Y-AXIS POINTS:-" ,'y_pts3': "ENTER Y-AXIS POINTS:-",'y_pts4': "ENTER Y-AXIS POINTS:-",'y_pts5': "ENTER Y-AXIS POINTS:-",'name1': "ENTER Y-SET NAME:-",'name2': "ENTER Y-SET NAME:-",'name3': "ENTER Y-SET NAME:-",'name4': "ENTER Y-SET NAME:-",'name5': "ENTER Y-SET NAME:-",}
        s_category=forms.ModelChoiceField(queryset=cat.objects.all(),required=True),
        s_subcategory=forms.CharField(max_length=900,required=False),
        graph =forms.ChoiceField(choices=G_CHOICES,required=True),
        x_axistittle=forms.CharField(max_length=900,required=False),
        y_axistittle=forms.CharField(max_length=900,required=False),
        s_head_tittle=forms.CharField(max_length=900,required=False),
        s_head_subtittle=forms.CharField(max_length=900,required=False),
        s_count=forms.ModelChoiceField(queryset=country.objects.all(),required=False),
        s_src1= forms.URLField(required=False),
        desc1=forms.CharField(required=False),
        s_publisher=forms.CharField(max_length=900,required=False),
        graph_tittle=forms.CharField(max_length=900, required=False)
        name =forms.CharField(max_length=900,widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Eg: Fruits'}),required=True),
        x_pts=forms.CharField(required=True),
        y_pts=forms.CharField(required=True)
        name1 =forms.CharField(max_length=900,widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Eg: Fruits'}),required=True),
        y_pts1=forms.CharField(required=True)
        name2 =forms.CharField(max_length=900,widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Eg: Fruits'}),required=True),
        y_pts2=forms.CharField(required=True)
        name3 =forms.CharField(max_length=900,widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Eg: Fruits'}),required=True),
        y_pts3=forms.CharField(required=True)
        name4 =forms.CharField(max_length=900,widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Eg: Fruits'}),required=True),
        y_pts4=forms.CharField(required=True)
        name5 =forms.CharField(max_length=900,widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Eg: Fruits'}),required=True),
        y_pts5=forms.CharField(required=True)

        widgets ={
        's_category':forms.Select(attrs={'class':'browser-default custom select','placeholder':"ALL"}),
        's_subcategory':forms.TextInput(attrs={'class':'form-control','placeholder':'Subcategory'}),
        'graph' :forms.Select(attrs={'class':"browser-default custom-select",'placeholder':'bar'}),
        'x_axistittle':forms.TextInput(attrs={'class':'form-control','placeholder':'X_axis tittle'}),
        'y_axistittle':forms.TextInput(attrs={'class':'form-control','placeholder':'Y_axis tittle'}),
        's_head_tittle':forms.TextInput(attrs={'class':'form-control','placeholder':'heading'}),
        's_head_subtittle':forms.TextInput(attrs={'class':'form-control','placeholder':'subtittle'}),
        's_count':forms.Select(attrs={'class':'browser-default custom select','placeholder':"ALL"}),
        's_src1':forms.URLInput(attrs={'class':'form-control','placeholder':'https://maps.google.com/'}),
        'desc1':forms.Textarea(attrs = {'class':'exampleFormControlTextarea4','placeholder':"keyword1 keyword2 (don't use comma or any symbol)"}),
        's_publisher':forms.TextInput(attrs={'class':'form-control','placeholder':'publisher'}),
        'graph_tittle':forms.TextInput(attrs={'class':'form-control','placeholder':'graph tittle'}),
        'name':forms.TextInput(attrs={'class':'form-control','placeholder':'Eg: Fruits'}),
        'x_pts':forms.Textarea(attrs = {'class':'exampleFormControlTextarea4','placeholder':"x1 (press enter) x2 (press enter) x3"}),
        'y_pts':forms.Textarea(attrs = {'class':'exampleFormControlTextarea4','placeholder':"y1 (press enter) y2 (press enter) y3"}),
        'name1':forms.TextInput(attrs={'class':'form-control','placeholder':'Eg: Fruits'}),
        'y_pts1':forms.Textarea(attrs = {'class':'exampleFormControlTextarea4','placeholder':"y1 (press enter) y2 (press enter) y3"}),

        'name2':forms.TextInput(attrs={'class':'form-control','placeholder':'Eg: Fruits'}),
        'y_pts2':forms.Textarea(attrs = {'class':'exampleFormControlTextarea4','placeholder':"y1 (press enter) y2 (press enter) y3"}),

        'name3':forms.TextInput(attrs={'class':'form-control','placeholder':'Eg: Fruits'}),
        'y_pts3':forms.Textarea(attrs = {'class':'exampleFormControlTextarea4','placeholder':"y1 (press enter) y2 (press enter) y3"}),

        'name4':forms.TextInput(attrs={'class':'form-control','placeholder':'Eg: Fruits'}),
        'y_pts4':forms.Textarea(attrs = {'class':'exampleFormControlTextarea4','placeholder':"y1 (press enter) y2 (press enter) y3"}),

        'name5':forms.TextInput(attrs={'class':'form-control','placeholder':'Eg: Fruits'}),
        'y_pts5':forms.Textarea(attrs = {'class':'exampleFormControlTextarea4','placeholder':"y1 (press enter) y2 (press enter) y3"}),




}
      






class infodevice_form(forms.ModelForm):
    class Meta:
        model= infog
        fields = ['i_category','i_subcategory','i_head_tittle','i_sub_tittle','i_count','i_src1','desc2','i_publisher','image_tittle','i_image']
        labels= {'i_sub_tittle' :  "ENTER SUBTITTLE:-" ,'i_category' :  "CHOOSE CATEGORY:-", 'i_subcategory' :"ENTER SUBCATEGORY:-"  ,'i_head_tittle' :"ENTER HEADING:-"  ,'i_count' :  "CHOOSE COUNTRY:-"  ,'i_src1' :  "ENTER SOURCE LINK 1:-",'desc2' :  "ENTER KEYWORDS:-"  ,'i_publisher' :  "ENTER PUBLISHER NAME:-" , 'image_tittle' :  "ENTER IMAGE NAME:-",'i_image' :"CHOOSE FILE:-" }

        i_category = forms.ModelChoiceField(queryset = cat.objects.all(),required=True),
        i_subcategory = forms.CharField(max_length=900,required=False),
        i_head_tittle = forms.CharField(max_length=900,required=False),
        i_head_subtittle = forms.CharField(max_length=900,required=False),
        i_count = forms.ModelChoiceField(queryset = country.objects.all(),required=False),
        i_src1 = forms.URLField(required=False),
        desc2 = forms.CharField(required=False),
        i_publisher = forms.CharField(max_length=900,required=False),
        image_tittle =forms.CharField(max_length=900,required=False),
        i_image =forms.ImageField(max_length=900,required=True)
        

        widgets={

        'i_category' :forms.Select(attrs = {'class' : 'browser-default custom select','placeholder': "ALL"}),
        'i_subcategory' :forms.TextInput(attrs = {'class' : 'form-control','placeholder': 'Subcategory' })  ,
        'i_head_tittle' :forms.TextInput(attrs = {'class' : 'form-control' , 'placeholder': 'heading'} ) ,
        'i_sub_tittle' :forms.TextInput(attrs = {'class' : 'form-control' ,'placeholder': 'subtittle'} ),
        'i_count' : forms.Select( attrs = {'class' : 'browser-default custom select' ,'placeholder': "ALL"}),
        'i_src1' :forms.URLInput(attrs = {'class' : 'form-control','placeholder': 'https://maps.google.com/'}) ,
        'desc2' :forms.Textarea(attrs = {'class' : 'exampleFormControlTextarea4', 'placeholder': "keyword1 keyword2 (don't use comma or any symbol)"} ),
        'i_publisher' : forms.TextInput(attrs = {'class' : 'form-control','placeholder': 'publisher'} ) ,
        'image_tittle' :forms.TextInput(attrs = {'class' : 'form-control' ,'placeholder': 'image tittle'} ) ,
        'i_image' :forms.ClearableFileInput(attrs={'class':'','placeholder':'choose'}),

}

class infodatabase_form(forms.ModelForm):
    def __init__(self , filter_on , *args , **kwargs) :
        super ( infodatabase_form , self ).__init__ ( *args , **kwargs )
        print ( filter_on )
        self.fields['image2field'] = forms.FilePathField ( path = RESOURCE_DIR , match = filter_on, required = True )

    class Meta:
        model= infog
        fields = ['i_category','i_subcategory','i_head_tittle','i_sub_tittle','i_count','i_src1','desc2','i_publisher','image_tittle','image2field']

        labels= {'i_sub_tittle' :  "ENTER SUBTITTLE:-" ,'i_category' :  "CHOOSE CATEGORY:-", 'i_subcategory' :"ENTER SUBCATEGORY:-"  ,'i_head_tittle' :"ENTER HEADING:-"  ,'i_count' :  "CHOOSE COUNTRY:-"  ,'i_src1' :  "ENTER SOURCE LINK 1:-",'desc2' :  "ENTER KEYWORDS:-"  ,'i_publisher' :  "ENTER PUBLISHER NAME:-" , 'image_tittle' :  "ENTER IMAGE NAME:-",'image2field' :"CHOOSE FILE:-" }
        i_category = forms.ModelChoiceField(queryset = cat.objects.all(),required=True),
        i_subcategory = forms.CharField(max_length=900,required=False),
        i_head_tittle = forms.CharField(max_length=900,required=False),
        i_head_subtittle = forms.CharField(max_length=900,required=False),
        i_count = forms.ModelChoiceField(queryset = country.objects.all(),required=False),
        i_src1 = forms.URLField(required=False),
        desc2 = forms.CharField(required=False),
        i_publisher = forms.CharField(max_length=900,required=False),
        image_tittle =forms.CharField(max_length=900,required=False),
       

           
        widgets={

        'i_category' :forms.Select(attrs = {'class' : 'browser-default custom select','placeholder': "ALL"}),
        'i_subcategory' :forms.TextInput(attrs = {'class' : 'form-control','placeholder': 'Subcategory' })  ,
        'i_head_tittle' :forms.TextInput(attrs = {'class' : 'form-control' , 'placeholder': 'heading'} ) ,
        'i_sub_tittle' :forms.TextInput(attrs = {'class' : 'form-control' ,'placeholder': 'subtittle'} ),
        'i_count' : forms.Select( attrs = {'class' : 'browser-default custom select' ,'placeholder': "ALL"}),
        'i_src1' :forms.URLInput(attrs = {'class' : 'form-control','placeholder': 'https://maps.google.com/'}) ,
        'desc2' :forms.Textarea(attrs = {'class' : 'exampleFormControlTextarea4', 'placeholder': "keyword1 keyword2 (don't use comma or any symbol)"} ),
        'i_publisher' : forms.TextInput(attrs = {'class' : 'form-control','placeholder': 'publisher'} ) ,
        'image_tittle' :forms.TextInput(attrs = {'class' : 'form-control' ,'placeholder': 'image tittle'} ) ,
        'image2field':forms.Select(attrs = {'class' : 'browser-default custom select','placeholder': 'choose' }) 

} 


class infolink_form(forms.ModelForm):
    class Meta:
        model= infog
        fields = ['i_category','i_subcategory','i_head_tittle','i_sub_tittle','i_count','i_src1','desc2','i_publisher','image_tittle','imageurl1']
        labels= {'i_sub_tittle' :  "ENTER SUBTITTLE:-" ,'i_category' :  "CHOOSE CATEGORY:-", 'i_subcategory' :"ENTER SUBCATEGORY:-"  ,'i_head_tittle' :"ENTER HEADING:-"  ,'i_count' :  "CHOOSE COUNTRY:-"  ,'i_src1' :  "ENTER SOURCE LINK 1:-",'desc2' :  "ENTER KEYWORDS:-"  ,'i_publisher' :  "ENTER PUBLISHER NAME:-" , 'image_tittle' :  "ENTER IMAGE NAME:-",'imageurl1' : "ENTER JPG/PNG LINK 1:-" }



        i_category = forms.ModelChoiceField(queryset = cat.objects.all(),required=True),
        i_subcategory = forms.CharField(max_length=900,required=False),
        i_head_tittle = forms.CharField(max_length=900,required=False),
        i_head_subtittle = forms.CharField(max_length=900,required=False),
        i_count = forms.ModelChoiceField(queryset = country.objects.all(),required=False),
        i_src1 = forms.URLField(required=False),
        desc2 = forms.CharField(required=False),
        i_publisher = forms.CharField(max_length=900,required=False),
        image_tittle =forms.CharField(max_length=900,required=False),
        imageurl1=forms.URLField(required = True ),

        

        widgets={

        'i_category' :forms.Select(attrs = {'class' : 'browser-default custom select','placeholder': "ALL"}),
        'i_subcategory' :forms.TextInput(attrs = {'class' : 'form-control','placeholder': 'Subcategory' })  ,
        'i_head_tittle' :forms.TextInput(attrs = {'class' : 'form-control' , 'placeholder': 'heading'} ) ,
        'i_sub_tittle' :forms.TextInput(attrs = {'class' : 'form-control' ,'placeholder': 'subtittle'} ),
        'i_count' : forms.Select( attrs = {'class' : 'browser-default custom select' ,'placeholder': "ALL"}),
        'i_src1' :forms.URLInput(attrs = {'class' : 'form-control','placeholder': 'https://maps.google.com/'}) ,
        'desc2' :forms.Textarea(attrs = {'class' : 'exampleFormControlTextarea4', 'placeholder': "keyword1 keyword2 (don't use comma or any symbol)"} ),
        'i_publisher' : forms.TextInput(attrs = {'class' : 'form-control','placeholder': 'publisher'} ) ,
        'image_tittle' :forms.TextInput(attrs = {'class' : 'form-control' ,'placeholder': 'image tittle'} ) ,
        'imageurl1':forms.URLInput(attrs = {'class' : 'form-control','placeholder': 'https://maps.google.jpg/' }), 

}

class codes(forms.Form):
    fields = ('cde',)
    cde = forms.ModelChoiceField(queryset=codes_list.objects.values_list('co',flat=True),label="Enter",required=True)
    widgets={ 'cde':forms.Select(attrs={'class' : 'browser-default custom select' ,'placeholder': "code"}),}

class code_form(forms.ModelForm):
    class Meta:
        model = codes_list
        fields = ['co']
        labels = {'co':'enter the code'}
        co = forms.CharField(max_length = 900,required=True)
        widgets = {'co':forms.TextInput(attrs = {'class' : 'form-control' ,'placeholder': 'code'} )}