from django.contrib import admin
from polls.models import Question,Choice,Word,WordBook

admin.site.register(Question)
admin.site.register(Choice)
admin.site.register(Word)
admin.site.register(WordBook)

# Register your models here.
