from django.contrib import admin
from .models import *
#---------------------------
admin.site.register(User)
admin.site.register(Comment)
admin.site.register(ProductComment)
admin.site.register(ArticleComment)
admin.site.register(WatchedProduct)
#---------------------------
