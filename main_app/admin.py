from django.contrib import admin
from . models import Challenge, ChallengeComment, Post, PostComment
# Register your models here.

admin.site.register(Challenge)
admin.site.register(ChallengeComment)
admin.site.register(Post)
admin.site.register(PostComment)