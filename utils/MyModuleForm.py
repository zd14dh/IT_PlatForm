from django.forms import ModelForm,widgets as wid
from app01 import models



    #方法1
from django import forms
# class ItModelForm(ModelForm):
#     class Meta:
#         model =models.It
#         fields = "__all__"
#     bootstrapClass_filter=['it_start_time','it_end_time']
#     it_start_time=forms.DateField(label='开始时间',widget=wid.DateInput(attrs={"class":"form-control",'type':"date"}))
#     it_end_time=forms.DateField(label='结束时间',widget=wid.DateInput(attrs={"class":"form-control",'type':"date"}))
#     def __init__(self,*args,**kwargs):
#         super().__init__(*args,**kwargs)
#         for name ,field in self.fields.items():
#             if name in self.bootstrapClass_filter:
#                 continue
#             old_class = field.widget.attrs.get('class',"")
#             field.widget.attrs['class']='{}form-control'.format(old_class)
#             field.widget.attrs['placeholder']='请输入%s' % (field.label,)


    #方法2
class ItModelForm(ModelForm):
    class Meta:
        model =models.It
        fields = "__all__"
        labels = {
            "it_name":"项目名称",
            "it_desc":"项目描述",
            "it_start_time":"项目开始时间3",
            "it_end_time":"项目结束时间4",

        }
        error_messages={
            "it_name":{"required":"该字段不能为空"},
            "it_desc":{"required":"该字段不能为空"},
            "it_start_time":{"required":"该字段不能为空"},
            "it_end_time":{"required":"该字段不能为空"},
        }
        widgets = {
            "it_name":wid.Input(attrs={"class":"form-control","placeholder":"输入项目名称"}),
            "it_desc":wid.Textarea(attrs={"class":"form-control","placeholder":"输入项目描述"}),
            "it_start_time":wid.DateInput(attrs={"class":"form-control",'type':"date"}),
            "it_end_time":wid.DateInput(attrs={"class":"form-control",'type':"date"}),
        }

class ApiModelForm(ModelForm):
    class Meta:
        model=models.Api
        fields = "__all__"
        exclude=['api_run_status','api_run_time','api_pass_status','api_report','api_sub_it']
    bootstrapClass_filter=['api_run_status','api_run_time','api_pass_status','api_report']
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        for name ,field in self.fields.items():
            if name in self.bootstrapClass_filter:
                continue
            old_class = field.widget.attrs.get('class',"")
            field.widget.attrs['class']='{}form-control'.format(old_class)
            field.widget.attrs['placeholder']='请输入%s' % (field.label,)
