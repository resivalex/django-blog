from .resume import black_link, output_place, output_tags, \
    sape_tags, oneretarget_tags, selfeducation_tags, piratetrade_tags, piratetrade_2_tags, lakehouse_tags


def html():
    return f'''
<div class="container" itemscope itemtype="http://schema.org/Person">
	<div>
		[<a href="/resume-russian">Переключить на русский</a>]
	</div>

	<div class="main-header" itemprop="name">Reshetnikov Ivan Aleksandrovich</div>

	<p itemprop="description">
		I like writing beautiful and clean code, am interested in new technologies<br>
		I have a good sense of algorithm effectiveness<br>
		GitHub profile {black_link('https://github.com/resivalex')}
	</p>

	<div class="header" itemprop="jobTitle">Machine Learning Engineer</div>

  {
		output_place(month_period='2020.11-present',
			locale='en',
			name='Sape',
			link='https://sape.ru',
			description='Backlinks purchase service')
  }

	<div class="sub-header">Tasks</div>
	<p>
		— Price recommendation model development<br>
		— Searching for significant features, which cause product dissatisfaction<br>
		— Helping SEO-specialists to construct effective promotion strategies
	</p>

	<div class="sub-header">Achievements</div>
	<p>
		— Development of price recommendation model from data analysis to preparing for deploy
	</p>

	<div class="sub-header">Technologies</div>
  {
  	output_tags(sape_tags())
  }

	<div class="header" itemprop="jobTitle">Lead Ruby on Rails developer</div>

	{
		output_place(month_period='2016.12-2020.11',
			name='OneRetarget.com',
			link='https://oneretarget.com',
			description='A service to manage several ad platforms at one account')
	}

	<div class="sub-header">Tasks</div>
	<p>
		— Chosing the technical development strategy and tools, suggestion/discussion of implementation ways. Code review<br>
		— Creating tools to analyze and manage ads<br>
		— Synchronization of statistics, state of moderation<br>
		— Implementing of new formats. Error handling<br>
		— Deployment of the system. Backups. System state monitoring
	</p>

	<div class="sub-header">Achievements</div>
	<p>
		— Modifying the API in such a way it can be used for external users and the frontend<br>
		— Synchronization and display of advertising performance from Yandex.Metrica data<br>
		— Adding a section for problem detection in the system<br>
		— Implementation of interactive widgets: weekly schedule, bulk copying, ad preview<br>
		— Frontend migration from CoffeeScript and jQuery to ES6 and React<br>
		— Correction of the layout and use of the single style within the entire user account
	</p>

	<div class="sub-header">Technologies</div>
	{
		output_tags(oneretarget_tags())
	}

	<div class="header">Ruby on Rails developer</div>

	{
		output_place(month_period='2016.04-2016.11',
			name='Lakehouse',
			link='http://www.lakehouse.ru')
	}

	<div class="sub-header">Tasks</div>
	<p>
		— Real estate project support and development {black_link('http://o-din.ru/')}<br>
		— Beauty specialists qualification project support and development {black_link('http://e-academie.ru/')}
	</p>
	<div class="sub-header">Technologies</div>
	{
		output_tags(lakehouse_tags())
	}

	<div class="header">Самообразование</div>

	{
		output_place(month_period='2016.02-2016.04')
	}

	<div class="sub-header">Tasks</div>
	<p>
		— Graduation work rewriting {black_link('https://github.com/resivalex/student-progress-on-rails')}<br>
		— Trampoline center website development {black_link('https://github.com/resivalex/zaskok')}
	</p>
	<div class="sub-header">Technologies</div>
	{
		output_tags(selfeducation_tags())
	}

	<div class="header">Software developer</div>

	{
		output_place(month_period='2015.04-2016.01',
			name='Nasca Ltd.',
			link='http://piratetrade.ru',
			description='Exchange trading company')
	}

	<div class="sub-header">Tasks</div>
	<p>
		— Website development {black_link('http://pskovskie.ru/')} from scratch<br>
		— Development of a multi-component network application in a team of five members using the Scrum methodology<br>
		— Full implementation of an important component interacting with the exchange<br>
		— Unit-testing with Catch framework<br>
		— Partially designing and implementing a client application on Qt<br>
		— Using design patterns<br>
		— Code review
	</p>
	<div class="sub-header">Technologies</div>
	{
		output_tags(piratetrade_2_tags())
	}

	<div class="header">C++/Qt developer</div>

	{
		output_place(month_period='2012.12-2013.09',
			name='Nasca Ltd.',
			link='http://piratetrade.ru',
			description='Exchange trading company')
	}

	<div class="sub-header">Tasks</div>
	<p>
		— Improvements of the trading engine<br>
		— Exchange log parsing and analysis<br>
		— Features implementing for a transaction logging software<br>
		— Development of a program for emulation an exchange<br>
		— Sending email to users of specialized sites<br>
		— Automatic exchange log downloading<br>
		— Using system of version control
	</p>
	<div class="sub-header">Technologies</div>
	{
		output_tags(piratetrade_tags())
	}

	<div class="header">Higher education</div>

	<div class="row-with-icon">
		<div class="row-with-icon__icon"><span class="symbol-icon glyphicon glyphicon-send"></span></div>
		<div class="row-with-icon__info">
			<div>Pskov State University</div>
			<div>2008 - 2013</div>
			<div>Faculty of Informatics</div>
		</div>
	</div>

	<div class="header">Languages</div>

	<div class="row-with-icon">
		<div class="row-with-icon__icon"><span class="symbol-icon glyphicon glyphicon-send"></span></div>
		<div class="row-with-icon__info">
			<div itemprop="nationality">Russian — Native</div>
			<div>English — Upper Intermediate</div>
		</div>
	</div>

	<div class="header">Contacts</div>

	<div class="row-with-icon">
		<div class="row-with-icon__icon"><span class="symbol-icon glyphicon glyphicon-envelope"></span></div>
		<div class="row-with-icon__info">
			<div itemprop="email">resivalex@gmail.com</div>
		</div>
	</div>
</div>
    
    '''
