# pages/views.py
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Page

class PageListView(ListView):
    model = Page
    template_name = 'pages/page_list.html'
    context_object_name = 'pages'
    paginate_by = 10

    def get_queryset(self):
        qs = super().get_queryset()
        q = self.request.GET.get('q')
        if q:
            qs = qs.filter(title__icontains=q) | qs.filter(subtitle__icontains=q)
        return qs

class PageDetailView(DetailView):
    model = Page
    template_name = 'pages/page_detail.html'
    context_object_name = 'page'

class OwnerRequiredMixin(UserPassesTestMixin):
    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user

class PageCreateView(LoginRequiredMixin, CreateView):
    model = Page
    form_class = None
    template_name = 'pages/page_form.html'
    success_url = reverse_lazy('pages:list')

    def get_form_class(self):
        from .forms import PageForm
        return PageForm

    def form_valid(self, form):
        form.instance.author = self.request.user
        messages.success(self.request, 'Página creada correctamente.')
        return super().form_valid(form)

class PageUpdateView(LoginRequiredMixin, OwnerRequiredMixin, UpdateView):
    model = Page
    form_class = None
    template_name = 'pages/page_form.html'
    success_url = reverse_lazy('pages:list')

    def get_form_class(self):
        from .forms import PageForm
        return PageForm

    def form_valid(self, form):
        messages.success(self.request, 'Página actualizada.')
        return super().form_valid(form)

class PageDeleteView(LoginRequiredMixin, OwnerRequiredMixin, DeleteView):
    model = Page
    template_name = 'pages/page_confirm_delete.html'
    success_url = reverse_lazy('pages:list')

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, 'Página eliminada.')
        return super().delete(request, *args, **kwargs)