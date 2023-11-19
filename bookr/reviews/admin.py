from django.contrib import admin

from reviews import models
from reviews.models import (Publisher, Contributor, Book, BookContributor, Review)


# Register your models here.


class ContributorAdmin(admin.ModelAdmin):
    list_display = ('last_names', 'first_names')
    search_fields = ('last_names__startswith', 'first_names')
    list_filter = ('last_names',)


class BookAdmin(admin.ModelAdmin):
    search_fields = ('title', 'isbn__exact', 'publisher__name__startswith')
    date_hierarchy = 'publication_date'
    list_display = ('title', 'isbn13')
    list_filter = ('publisher', 'publication_date')

    def isbn13(self, obj):
        return f'{obj.isbn[0:3]}-{obj.isbn[3:4]}-{obj.isbn[4:6]}-{obj.isbn[6:12]}-{obj.isbn[12:13]}'


class ReviewAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {"fields": ("creator", "book")}),
        ("Review content", {"fields": ("content",
                                       "rating")}),
    )


admin.site.register(Publisher)
admin.site.register(Contributor, ContributorAdmin)
admin.site.register(Book, BookAdmin)
admin.site.register(BookContributor)
admin.site.register(Review, ReviewAdmin)
