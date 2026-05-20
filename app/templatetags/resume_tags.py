from django import template
from django.utils.safestring import mark_safe
from .period import Period

register = template.Library()


TAGS_TEMPLATE = "app/includes/tags.html"
PLACE_TEMPLATE = "app/includes/place.html"


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


@register.inclusion_tag(PLACE_TEMPLATE)
def output_place(
    month_period=None,
    duration=None,
    name=None,
    link=None,
    description=None,
):
    period = None
    if month_period is not None:
        months = month_period.split("-")
        period = Period(months[0], months[1])
        duration = period.duration()
        period = period.to_string()

    return {
        "duration": duration,
        "period": period,
        "name": name,
        "link": link,
        "description": description,
        "show_time": duration is not None or period is not None,
        "show_organization": (
            name is not None or link is not None or description is not None
        ),
    }


@register.simple_tag
def black_link(url, text=None):
    if text is None:
        text = url
    return mark_safe(f'<a target="_blank" class="black-link" href="{url}">{text}</a>')
