from flask import render_template
from . import main 
from ..requests import get_sources,get_articles
# views
@main.route('/')
def index ():
    """
    Function that returns the index page and its content
    """
    business_list = get_sources('gb','business')
    entertainment_list = get_sources('gb','entertainment')
    health_list = get_sources('gb','health')
    science_list = get_sources('gb','science')
    sports_list = get_sources('gb','sports')
    technology_list = get_sources('gb','technology')
    test_args ='working'
    return render_template('index.html',test_param = test_args,entertainment = entertainment_list,health = health_list,science = science_list, sports = sports_list,technology = technology_list)
    
@main.route('/news/<int:id>')
def news(id):
    """
    views news page function that that returns the news details page and its data
    """