from django.contrib import admin
from .models import CollegeEvent,Register
class CollegeEventsAdmin(admin.ModelAdmin):
    list_display = ('event_name' , 'description' , 'seats',)

class RegisterAdmin(admin.ModelAdmin):
    list_display = ('participant_name','email','event_id')

admin.site.register(CollegeEvent,CollegeEventsAdmin)
admin.site.register(Register,RegisterAdmin)