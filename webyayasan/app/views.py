from django.views.generic import TemplateView
from django.conf import settings
from django.shortcuts import render, redirect
from .models import Post, Category, Pendidikan, Contact
from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from .forms import ContactForm

def index(request):
    context = {}
    try:
        penting_posts = Post.objects.filter(category__name='penting')[:3]
        header_beranda_posts = Post.objects.filter(category__name='header_beranda')
        recent_posts = Post.objects.all().order_by("-id")[:3]

        context.update({
            'penting_posts': penting_posts,
            'header_beranda_posts': header_beranda_posts,
            'recent_posts': recent_posts,
            'media_url': settings.MEDIA_URL
        })
    except Post.DoesNotExist as e:
        context['error'] = f"Error fetching posts: {str(e)}"

    return render(request, 'index.html', context)

def prestasi(request):
    context = {}
    try:
        recent_posts = Post.objects.filter(category__name='prestasi').order_by("-id")[:3]
        posts = Post.objects.filter(category__name='prestasi')
        posts_asia = Post.objects.filter(category__name='prestasi',pendidikan__name='asia')
        posts_nasional = Post.objects.filter(category__name='prestasi',pendidikan__name='nasional')
        posts_provinsi = Post.objects.filter(category__name='prestasi',pendidikan__name='provinsi')
        posts_kabupaten = Post.objects.filter(category__name='prestasi',pendidikan__name='kabupaten')
        posts_kecamatan = Post.objects.filter(category__name='prestasi',pendidikan__name='kecamatan')

        context.update({
            'posts': posts,
            'posts_asia': posts_asia,
            'posts_nasional': posts_nasional,
            'posts_provinsi': posts_provinsi,
            'posts_kabupaten': posts_kabupaten,
            'posts_kecamatan': posts_kecamatan,
            'recent_posts': recent_posts,
            'media_url': settings.MEDIA_URL
        })
    except Post.DoesNotExist as e:
        context['error'] = f"Error fetching posts: {str(e)}"

    return render(request, 'prestasi.html', context)

def pendidikan_ma(request):
    context = {}
    try:
        kegiatan_posts = Post.objects.filter(category__name='kegiatan', pendidikan__name='ma')
        prestasi_posts = Post.objects.filter(category__name='prestasi', pendidikan__name='ma')

        context.update({
            'kegiatan_posts': kegiatan_posts,
            'prestasi_posts': prestasi_posts,
            'media_url': settings.MEDIA_URL
        })
        print(kegiatan_posts)
    except Post.DoesNotExist as e:
        context['error'] = f"Error fetching posts: {str(e)}"

    return render(request, 'pendidikan_ma.html', context)

def pendidikan_smp(request):
    context = {}
    try:
        kegiatan_posts = Post.objects.filter(category__name='kegiatan', pendidikan__name='smp')
        prestasi_posts = Post.objects.filter(category__name='prestasi', pendidikan__name='smp')

        context.update({
            'kegiatan_posts': kegiatan_posts,
            'prestasi_posts': prestasi_posts,
            'media_url': settings.MEDIA_URL
        })
        print(kegiatan_posts)
    except Post.DoesNotExist as e:
        context['error'] = f"Error fetching posts: {str(e)}"

    return render(request, 'pendidikan_smp.html', context)

def pendidikan_tpq(request):
    context = {}
    try:
        kegiatan_posts = Post.objects.filter(category__name='kegiatan', pendidikan__name='tpq')
        prestasi_posts = Post.objects.filter(category__name='prestasi', pendidikan__name='tpq')

        context.update({
            'kegiatan_posts': kegiatan_posts,
            'prestasi_posts': prestasi_posts,
            'media_url': settings.MEDIA_URL
        })
        print(kegiatan_posts)
    except Post.DoesNotExist as e:
        context['error'] = f"Error fetching posts: {str(e)}"

    return render(request, 'pendidikan_tpq.html', context)

def pendidikan_kampus(request):
    context = {}
    try:
        kegiatan_posts = Post.objects.filter(category__name='kegiatan', pendidikan__name='kampus')
        prestasi_posts = Post.objects.filter(category__name='prestasi', pendidikan__name='kampus')

        context.update({
            'kegiatan_posts': kegiatan_posts,
            'prestasi_posts': prestasi_posts,
            'media_url': settings.MEDIA_URL
        })
        print(kegiatan_posts)
    except Post.DoesNotExist as e:
        context['error'] = f"Error fetching posts: {str(e)}"

    return render(request, 'pendidikan_kampus.html', context)

def pendidikan_mahad(request):
    context = {}
    try:
        kegiatan_posts = Post.objects.filter(category__name='kegiatan', pendidikan__name='mahad')
        prestasi_posts = Post.objects.filter(category__name='prestasi', pendidikan__name='mahad')

        context.update({
            'kegiatan_posts': kegiatan_posts,
            'prestasi_posts': prestasi_posts,
            'media_url': settings.MEDIA_URL
        })
        print(kegiatan_posts)
    except Post.DoesNotExist as e:
        context['error'] = f"Error fetching posts: {str(e)}"

    return render(request, 'pendidikan_mahad.html', context)

def berita(request):
    context = {}
    try:
        # Ambil semua post dan urutkan berdasarkan ID
        post_list = Post.objects.all().order_by("-id")
        
        # Setup pagination
        paginator = Paginator(post_list, 5)  # Tampilkan 5 post per halaman
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)

        penting_posts = Post.objects.filter(category__name='penting')
        recent_posts = Post.objects.all().order_by("-id")[:2]

        context.update({
            'page_obj': page_obj,
            'penting_posts': penting_posts,
            'recent_posts': recent_posts,
            'media_url': settings.MEDIA_URL
        })
    except Post.DoesNotExist as e:
        context['error'] = f"Error fetching posts: {str(e)}"

    return render(request, 'berita.html', context)

def beritadetail(request, id):
    context = {}
    try:
        post = get_object_or_404(Post, id=id)
        recent_posts = Post.objects.all().order_by("-id")[:2]
        context.update({
            'post': post,
            'media_url': settings.MEDIA_URL,
            'recent_posts': recent_posts,
        })
    except Post.DoesNotExist as e:
        context['error'] = f"Error fetching post detail: {str(e)}"

    return render(request, 'beritadetail.html', context)

def contact_view(request):
    success_message = ''
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            success_message = 'Thank you for contacting us. We will get back to you soon.'
            form = ContactForm()  # Reset the form after saving
    else:
        form = ContactForm()
    return render(request, 'faqs.html', {'form': form, 'success_message': success_message})


def profil(request):
    return render(request, 'profil.html')

def struktur_organisasi(request):
    return render(request, 'struktur_organisasi.html')

def akreditasi(request):
    return render(request, 'akreditasi.html')

def pendidikan_ma(request):
    return render(request, 'pendidikan_ma.html')

def faqs(request):
    return render(request, 'faqs.html')

def helpdesk(request):
    return render(request, 'helpdesk.html')

def ppdb(request):
    return render(request, 'ppdb.html')
