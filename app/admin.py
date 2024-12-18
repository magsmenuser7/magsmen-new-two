from django.contrib import admin
from .models import BlogPost,Category,ContactData,Media,StepformData,Subscribe,CareerInfo,ApplyForm

# Register your models here.

class AdminHappyCategories(admin.ModelAdmin):
    list_display=('Name','Created')


class AdminHappyBlogpost(admin.ModelAdmin):
    list_display=('Id','Category','Title','Tags','CreatedName','Create_at','status')
    list_filter = ["CreatedName",'Create_at']


class AdminCareerInfo(admin.ModelAdmin):
    list_display = ['ExpertiseName','Location','CreatedAt']



class AdminApplyForm(admin.ModelAdmin):
    list_display=['Name','Email','Phone']


class AdminHappyContact(admin.ModelAdmin):
    list_display=('Name','Email','Phone','Subject','Message')


class AdminMedia(admin.ModelAdmin):
    list_display = ['Title','Image','Url']



class AdminStepformData(admin.ModelAdmin):
    list_display = ['name','email','phone','Brandmarketposition','BrandCorevalue','Brandperceive_targetaudience','CustomerFeedback','BrandPerformence','Challenges_Obstacles']


class AdminSubscribe(admin.ModelAdmin):
    list_display = ('Email',)


admin.site.register(Category,AdminHappyCategories)
admin.site.register(BlogPost,AdminHappyBlogpost)
admin.site.register(CareerInfo,AdminCareerInfo)
admin.site.register(ApplyForm,AdminApplyForm)
admin.site.register(ContactData,AdminHappyContact)
admin.site.register(Media,AdminMedia)
admin.site.register(StepformData,AdminStepformData)
admin.site.register(Subscribe,AdminSubscribe)