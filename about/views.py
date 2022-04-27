from django.views.generic import TemplateView


class DescriptionView(TemplateView):
    template_name = 'about/description.html'

    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        return context
