from django.db import models
from wagtail.admin.panels import (
    FieldPanel,
    MultiFieldPanel,
    PublishingPanel
)
from wagtail.contrib.settings.models import (
    BaseGenericSetting,
    register_setting,
)
from wagtail.fields import RichTextField
from wagtail.models import (
    DraftStateMixin,
    PreviewableMixin,
    RevisionMixin,
    TranslatableMixin,
)
from wagtail.contrib.settings.models import (
    BaseGenericSetting,
    register_setting,
)
from wagtail.snippets.models import register_snippet

@register_setting
class NavigationSettings(BaseGenericSetting):
    twitter_url = models.URLField(verbose_name="Twitter URL", blank=True)
    github_url = models.URLField(verbose_name="GitHub URL", blank=True)
    mastodon_url = models.URLField(verbose_name="Mastodon URL", blank=True)

    panels = [
        MultiFieldPanel(
            [
                FieldPanel("twitter_url"),
                FieldPanel("github_url"),
                FieldPanel("mastodon_url"),
            ],
            "Social settings",
        )
    ]

@register_snippet
class TemplateSettings(models.Model):

    show_leftbar=models.BooleanField(
        default=False,
        help_text="If the left sidebar should be shown - requires a template named wibewa/includes/sidebarleft.html"
    )
    show_rightbar=models.BooleanField(
        default=False,
        help_text="If the right sidebar should be shown - requires a template named wibewa/includes/sidebarright.html"
    )

    mainmenu_location=models.CharField(
        "main menu location",
        max_length=20,
        choices=(("none","None"),("top","Top"),("left","Left"),("right","Right")),
        help_text="The location of the main menu",
        default="top"
    )
    themecolor=models.CharField(
        "theme color",
        max_length=30,
        default="blue",
        help_text='The theme color. This should match the base name of a css file in a static folder wibekwa/css'
    )

    def __str__(self):
        return "Template Settings"

    class Meta():
        verbose_name_plural = "Template Settings"

@register_snippet
class FooterText(
    DraftStateMixin,
    RevisionMixin,
    PreviewableMixin,
    TranslatableMixin,
    models.Model,
):
    body = RichTextField()

    panels = [
        FieldPanel("body"),
        PublishingPanel(),
    ]

    def __str__(self):
        return "Footer text"

    def get_preview_template(self, request, mode_name):
        return "base.html"

    def get_preview_context(self, request, mode_name):
        return {"footer_text": self.body}

    class Meta(TranslatableMixin.Meta):
        verbose_name_plural = "Footer Text"
