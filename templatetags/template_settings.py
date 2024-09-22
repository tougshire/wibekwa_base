from django import template

from wagtail.models import Site

from wibekwa_base.models import TemplateSettings

register = template.Library()

@register.simple_tag(takes_context=True)
def get_template_settings(context):

    template_settings = context.get("template_settings", "")

    if not template_settings:
        instance = TemplateSettings.objects.first()
        template_settings = {
            "show_leftbar": instance.show_leftbar,
            "show_rightbar": instance.show_rightbar,
            "mainmenu_location": instance.mainmenu_location,
            "themecolor": instance.themecolor,
        } if instance else {
            "show_leftbar": False,
            "show_rightbar": False,
            "mainmenu_location": "top",
            "themecolor": "black",
        }

        return template_settings


@register.simple_tag(takes_context=True)
def get_site_root(context):
    return Site.find_for_request(context["request"]).root_page
