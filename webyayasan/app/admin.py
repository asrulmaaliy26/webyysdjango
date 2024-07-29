from django.contrib import admin
from ckeditor.widgets import CKEditorWidget
from .models import Post, Category, Contact, Pendidikan
from django import forms

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = '__all__'
        widgets = {
            'content': CKEditorWidget(),  # Menggunakan CKEditor untuk field konten
        }

class PostInline(admin.TabularInline):
    model = Post
    extra = 1  # Menambahkan baris kosong untuk memasukkan data baru
    fields = ('postname', 'category', 'pendidikan', 'image', 'link', 'created', 'updated')  # Hanya menampilkan field yang diinginkan
    readonly_fields = ('created', 'updated')

class CategoryAdmin(admin.ModelAdmin):
    inlines = [PostInline]

class PendidikanAdmin(admin.ModelAdmin):
    inlines = [PostInline]

class PostAdmin(admin.ModelAdmin):
    form = PostForm
    list_display = ('postname', 'category', 'pendidikan', 'created', 'updated')  # Menampilkan field di daftar
    list_filter = ('category', 'pendidikan')  # Menambahkan filter berdasarkan kategori dan pendidikan
    search_fields = ('postname', 'content')  # Menambahkan fitur pencarian

admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Contact)
admin.site.register(Pendidikan, PendidikanAdmin)

admin.site.site_header = 'YAYASAN AL MANNAN | ADMIN PANEL'
admin.site.site_title = 'AL MANNAN | BLOGGING WEBSITE'
admin.site.index_title = 'Al - Mannan Site Administration'
