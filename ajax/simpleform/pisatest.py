import os
import StringIO
from xhtml2pdf import pisa

from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import render
from django.template.loader import get_template
from django.template.context import Context
from django.utils.html import escape


def fetch_resources(uri, rel):
    """
    Callback to allow xhtml2pdf/reportlab to retrieve Images,Stylesheets, etc.
    `uri` is the href attribute from the html link element.
    `rel` gives a relative path, but it's not used here.

    """
    if uri.startswith(settings.MEDIA_URL):
        path = os.path.join(settings.MEDIA_ROOT,
                            uri.replace(settings.MEDIA_URL, ""))
    elif uri.startswith(settings.STATIC_URL):
        path = os.path.join(settings.STATIC_ROOT,
                            uri.replace(settings.STATIC_URL, ""))
    else:
        path = os.path.join(settings.STATIC_ROOT,
                            uri.replace(settings.STATIC_URL, ""))

        if not os.path.isfile(path):
            path = os.path.join(settings.MEDIA_ROOT,
                                uri.replace(settings.MEDIA_URL, ""))

            if not os.path.isfile(path):
                raise UnsupportedMediaPathException(
                                    'media urls must start with %s or %s' % (
                                    settings.MEDIA_ROOT, settings.STATIC_ROOT))

    return path


def render_to_pdf(template_src, context_dict):
    """Function to render html template into a pdf file"""
    template = get_template(template_src)
    context = Context(context_dict)
    html = template.render(context)
    result = StringIO.StringIO()

    pdf = pisa.pisaDocument(StringIO.StringIO(html.encode("UTF-8")),
                                            dest=result,
                                            encoding='UTF-8',
                                            link_callback=fetch_resources)
    if not pdf.err:
        response = HttpResponse(result.getvalue(),
                                                    mimetype='application/pdf')

        return response

    return HttpResponse('We had some errors<pre>%s</pre>' % escape(html))


def download_pdf(request):
    """Build briefing packages format and export as HTML and PDF."""
    response = HttpResponse(content_type='application/pdf')
    return generate_pdf('app/test.html', file_object=response)