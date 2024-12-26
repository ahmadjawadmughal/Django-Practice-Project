from django.contrib import admin
from .models import *
# Register your models here.

# admin.site.register(Husband)
# admin.site.register(Wife)
admin.site.register(Manufacturer)
admin.site.register(Car)
admin.site.register(Author)
admin.site.register(Book)
admin.site.register(Student)
admin.site.register(Course)
admin.site.register(Enrollment)

@admin.register(Husband)
class HusbandAdmin(admin.ModelAdmin):
    list_display = ("name", "age", "wealth", "avg_wealth")
    search_fields = ("name", "wealth")
    list_filter = ("name","age")

    def avg_wealth(self, obj):
        from django.db.models import Max,Min,Avg

        res = Husband.objects.aggregate(Avg("wealth"))

        return res["wealth__avg"]

    avg_wealth.short_description = "Avg Wealth (USD)"



@admin.register(Wife)
class WifeAdmin(admin.ModelAdmin):
    list_display = ('name', 'age', 'husband_name')

    def husband_name(self, obj):
        from django.utils.html import format_html

        return format_html("<b><em>{}</em></b>",obj.husband.name)