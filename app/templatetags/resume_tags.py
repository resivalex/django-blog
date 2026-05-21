from django import template
from django.utils.safestring import mark_safe

register = template.Library()


TAGS_TEMPLATE = "app/includes/tags.html"


def tags_context(tags):
    return {"tags": tags}


def maksmart_tags():
    return [
        "Python",
        "PyTorch",
        "scikit-learn",
        "LightGBM",
        "fastText",
        "AutoML",
        "Active Learning",
        "LLM/RAG",
        "embeddings",
        "FastAPI",
        "Docker",
        "PostgreSQL",
        "ClickHouse",
    ]


def architech_tags():
    return [
        "Python",
        "LightGBM",
        "PyTorch",
        "Streamlit",
        "FastAPI",
        "PostgreSQL",
        "Docker",
        "Apache Superset",
        "ChatGPT API",
        "pytest",
    ]


def sape_tags():
    return [
        "Python",
        "scikit-learn",
        "fastText",
        "word2vec",
        "Gensim",
        "Pandas",
        "NumPy",
        "ClickHouse",
        "Flask",
        "pytest",
        "Jupyter",
        "Power BI",
    ]


def oneretarget_tags():
    return [
        "Ruby on Rails",
        "PostgreSQL",
        "RSpec",
        "Cucumber",
        "Capybara",
        "Docker",
        "Jenkins",
        "Capistrano",
        "React",
        "ES6",
        "Redux",
    ]


def lakehouse_tags():
    return [
        "Ruby on Rails 4",
        "PostgreSQL",
        "RSpec",
        "Capybara",
        "Capistrano",
        "Linux",
        "AngularJS",
        "CoffeeScript",
    ]


def selfeducation_tags():
    return [
        "Ruby on Rails",
        "RSpec",
        "Linux",
        "Capistrano",
        "AngularJS",
        "CoffeeScript",
        "PHP",
        "HTML",
        "SASS",
        "MySQL",
        "D3.js",
        "SVG",
    ]


def piratetrade_2_tags():
    return [
        "Ruby on Rails 4",
        "Ruby Slim",
        "JavaScript",
        "CSS",
        "SASS",
        "Bootstrap",
        "AJAX",
        "C++",
        "Boost Thread",
        "WebSocket",
        "JSON",
        "Catch",
        "JIRA",
        "Confluence",
        "Git",
    ]


def piratetrade_tags():
    return ["C++", "C++ Standard Library", "Qt", "JavaScript", "jQuery", "HTML", "SVN"]


@register.inclusion_tag(TAGS_TEMPLATE)
def output_maksmart_tags():
    return tags_context(maksmart_tags())


@register.inclusion_tag(TAGS_TEMPLATE)
def output_architech_tags():
    return tags_context(architech_tags())


@register.inclusion_tag(TAGS_TEMPLATE)
def output_sape_tags():
    return tags_context(sape_tags())


@register.inclusion_tag(TAGS_TEMPLATE)
def output_oneretarget_tags():
    return tags_context(oneretarget_tags())


@register.inclusion_tag(TAGS_TEMPLATE)
def output_lakehouse_tags():
    return tags_context(lakehouse_tags())


@register.inclusion_tag(TAGS_TEMPLATE)
def output_selfeducation_tags():
    return tags_context(selfeducation_tags())


@register.inclusion_tag(TAGS_TEMPLATE)
def output_piratetrade_2_tags():
    return tags_context(piratetrade_2_tags())


@register.inclusion_tag(TAGS_TEMPLATE)
def output_piratetrade_tags():
    return tags_context(piratetrade_tags())


@register.simple_tag
def black_link(url, text=None):
    if text is None:
        text = url
    return mark_safe(f'<a target="_blank" class="resume-link" href="{url}">{text}</a>')
