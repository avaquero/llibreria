from django import template
register = template.Library()

@register.assignment_tag
def get_twitter_bootstrap_alert_msg_css_name(tags):
    return 'notice' if tags == 'info' else tags