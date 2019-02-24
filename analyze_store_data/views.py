""" module to views methods """

from pyramid.response import Response
from pyramid.view import view_config

from analyze_store_data import utils

@view_config(renderer='json')
def home_api(context, request):
    """ View to return report data in json format """
    
    conn = request.dbsession
    data = utils.select_report_data(conn)
    
    return [dict(i) for i in data]
