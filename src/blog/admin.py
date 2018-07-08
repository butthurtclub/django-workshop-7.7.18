from django import forms
from django.contrib import admin
from blog import models
from ckeditor.widgets import CKEditorWidget


@admin.register(models.Article)
class AdminArticle(admin.ModelAdmin):
    content = forms.CharField(widget=CKEditorWidget())


@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Tag)
class TagAdmin(admin.ModelAdmin):
    pass
