from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.base import RedirectView
from django.core.urlresolvers import reverse, reverse_lazy

from .forms import ItemForm
from .models import ItemModel


class ItemList(ListView):
    model = ItemModel


class ItemDetail(DetailView):
    model = ItemModel


class ItemCreate(CreateView):
    # template_nameを指定しない場合は、modelを指定しないと、以下のエラー
    # ImproperlyConfigured
    # TemplateResponseMixin requires either a definition of 'template_name' or an implementation of 'get_template_names()'
    # また、各テンプレートファイルの格納ディレクトリは`path/to/project/<app_name>/templates/<app_name>`
    model = ItemModel

    form_class = ItemForm
    
    def get_success_url(self):
        return reverse('ns:item-update', args=(self.object.id,))


class ItemUpdate(UpdateView):
    model = ItemModel
    form_class = ItemForm
	
    def get_success_url(self):
        return reverse('ns:item-detail', args=(self.object.id,))


class ItemDelete(DeleteView):
    model = ItemModel
    
    def get_success_url(self):
        return reverse('ns:item-list')


class ItemRedirect(RedirectView):
    url = reverse_lazy('ns:item-list')
    # Django1.9より、permanent=Falseがデフォルトになった
    permanent = True