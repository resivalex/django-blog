from django.template.loader import render_to_string
from weasyprint import HTML

RESUME_TEMPLATE = "app/resume.html"
RESUME_PDF_FILENAME = "Ivan_Reshetnikov_Senior_ML_AI_Engineer.pdf"


def write_resume_pdf(base_url, target=None, request=None):
    html_string = render_to_string(RESUME_TEMPLATE, {"is_pdf": True}, request=request)
    html = HTML(string=html_string, base_url=base_url)
    return html.write_pdf(target, pdf_tags=True)
