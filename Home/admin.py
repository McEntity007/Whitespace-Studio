from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(State)
admin.site.register(City)
admin.site.register(User)
admin.site.register(ProductCategory)
admin.site.register(Product)
admin.site.register(ProductImage)
admin.site.register(ProductInquiry)
admin.site.register(DesignCategory)
admin.site.register(Design)
admin.site.register(DesignImage)
admin.site.register(DesignInquiry)
admin.site.register(Feedback)

admin.site.register(Contact)


