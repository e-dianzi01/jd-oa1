from django.forms.widgets import TextInput
from django.template import loader
from django.utils.safestring import mark_safe


class VideoInput(TextInput):
    input_type = None  # Subclasses must define this.
    template_name = 'video_input.html'

    def render(self, name, value, attrs=None, renderer=None):
        context = self.get_context(name, value, attrs)
        template = loader.get_template(self.template_name).render(context)
        return mark_safe(template)


class VideoPosterInput(TextInput):
    input_type = None  # Subclasses must define this.
    template_name = 'video_poster.html'

    def render(self, name, value, attrs=None, renderer=None):
        context = self.get_context(name, value, attrs)
        template = loader.get_template(self.template_name).render(context)
        return mark_safe(template)
