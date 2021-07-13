from .period import Period


def sape_tags():
    return ['Python', 'Pandas', 'MatPlotLib', 'NumPy', 'SciKit-Learn', 'Gensim', 'Jupyter', 'Flask', 'PyTest']


def oneretarget_tags():
    return [
        'Ruby on Rails 5', 'PostgreSQL', 'RSpec', 'Cucumber', 'Capybara', 'Jenkins', 'Docker', 'Capistrano',
        'Trailblazer', 'React.js', 'ES6', 'Redux', 'Flow', 'SASS', 'BEM', 'Webpack', 'yarn', 'styled-components',
        'delayed_job', 'VK API', 'myTarget API', 'Facebook API', 'AdWords API', 'Metrica API', 'Backup'
    ]


def lakehouse_tags():
    return ['Ruby on Rails 4', 'RSpec', 'Linux', 'Capistrano', 'Capybara', 'AngularJS', 'CoffeeScript', 'PostgreSQL']


def selfeducation_tags():
    return [
        'Ruby on Rails', 'RSpec', 'Linux', 'Capistrano', 'CoffeeScript', 'AngularJS',
        'PHP', 'HTML', 'CoffeeScript', 'SASS', 'MySQL', 'D3.js', 'SVG'
    ]


def piratetrade_2_tags():
    return [
        'Ruby on Rails 4', 'Ruby Slim', 'JavaScript', 'CSS', 'SASS', 'Bootstrap', 'AJAX', 'friendlyId', 'dragonfly',
        'C++', 'Boost Thread', 'WebSocket', 'JSON', 'Stash', 'JIRA', 'Confluence', 'Git'
    ]


def piratetrade_tags():
    return ['C++', 'C++ Standard Library', 'Qt', 'JavaScript', 'jQuery', 'HTML', 'SVN']


def output_tags(tags):
    return '\n'.join([f'<div class="tag">{tag}</div>' for tag in tags])


def output_place(month_period=None, locale=None, duration=None, rus_month_period=None,
                 name=None, link=None, description=None):
    result = ''
    period = None
    if month_period is not None:
        months = month_period.split('-')
        period = Period(months[0], months[1])
        if locale is not None and locale == 'ru':
            duration = period.to_russian_duration()
            period = period.to_russian_string()
        else:
            duration = period.to_english_duration()
            period = period.to_english_string()
    if rus_month_period is not None:
        months = rus_month_period.split('-')
        period = Period(months[0], months[1])
        duration = period.to_english_duration()
        period = period.to_english_string()
    if duration is not None or period is not None:
        result += f'''<div class="row-with-icon">
          <div class="row-with-icon__icon"><span class="symbol-icon glyphicon glyphicon-time"></span></div>
          <div class="row-with-icon__info">
            <div>{duration}</div>
            <div class="row-with-icon__comment">{period}</div>
          </div>
        </div>'''
    if name is not None or link is not None or description is not None:
        result += f'''<div class="row-with-icon">
          <div class="row-with-icon__icon"><span class="symbol-icon glyphicon glyphicon-map-marker"></span></div>
          <div class="row-with-icon__info">
            <div>{name}</div>
            <div>{black_link(link) if link else ''}</div>
            <div class="row-with-icon__comment">{description}</div>
          </div>
        </div>'''
    return result


def black_link(url):
    return f'<a target="_blank" class="black-link" href="{url}">{url}</a>'
