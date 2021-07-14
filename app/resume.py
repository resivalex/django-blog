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


def light_bulb():
    return '''
<svg xmlns="http://www.w3.org/2000/svg" width="20" height="24" fill="currentColor" class="bi bi-lightbulb" viewBox="0 0 16 16">
  <path d="M2 6a6 6 0 1 1 10.174 4.31c-.203.196-.359.4-.453.619l-.762 1.769A.5.5 0 0 1 10.5 13a.5.5 0 0 1 0 1 .5.5 0 0 1 0 1l-.224.447a1 1 0 0 1-.894.553H6.618a1 1 0 0 1-.894-.553L5.5 15a.5.5 0 0 1 0-1 .5.5 0 0 1 0-1 .5.5 0 0 1-.46-.302l-.761-1.77a1.964 1.964 0 0 0-.453-.618A5.984 5.984 0 0 1 2 6zm6-5a5 5 0 0 0-3.479 8.592c.263.254.514.564.676.941L5.83 12h4.342l.632-1.467c.162-.377.413-.687.676-.941A5 5 0 0 0 8 1z"/>
</svg>'''


def chat():
    return '''
<svg xmlns="http://www.w3.org/2000/svg" width="20" height="24" fill="currentColor" class="bi bi-chat" viewBox="0 0 16 16">
  <path d="M2.678 11.894a1 1 0 0 1 .287.801 10.97 10.97 0 0 1-.398 2c1.395-.323 2.247-.697 2.634-.893a1 1 0 0 1 .71-.074A8.06 8.06 0 0 0 8 14c3.996 0 7-2.807 7-6 0-3.192-3.004-6-7-6S1 4.808 1 8c0 1.468.617 2.83 1.678 3.894zm-.493 3.905a21.682 21.682 0 0 1-.713.129c-.2.032-.352-.176-.273-.362a9.68 9.68 0 0 0 .244-.637l.003-.01c.248-.72.45-1.548.524-2.319C.743 11.37 0 9.76 0 8c0-3.866 3.582-7 8-7s8 3.134 8 7-3.582 7-8 7a9.06 9.06 0 0 1-2.347-.306c-.52.263-1.639.742-3.468 1.105z"/>
</svg>'''
