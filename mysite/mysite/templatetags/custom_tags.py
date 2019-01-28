from django import template
from khayyam import JalaliDatetime
from datetime import datetime
from django.utils import formats
 
register = template.Library()

@register.simple_tag
def to_persian(input, lang):
	if lang == "fa":
		dt = JalaliDatetime(input)
		return dt.strftime('%C')
	else:
		return  formats.date_format(input, "SHORT_DATETIME_FORMAT")
	
