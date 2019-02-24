""" module to methods to main  """

import argparse
import sys
import os
from wsgiref.simple_server import make_server
from pyramid.config import Configurator

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from analyze_store_data import utils, report


def main():
    """ method to main process """

    parser = argparse.ArgumentParser(
        description="Process data file of Apple Store and returns file to analize data "
    )

    parser.add_argument(
        "--path_file", "-p", default="./AppleStore.csv", help="Path to file csv"
    )
    parser.add_argument(
        "--path_report",
        "-r",
        default="./AnalyzeReportData.csv",
        help="Path to result report file csv",
    )

    parser.add_argument(
        "--path_data_base",
        "-db",
        default="./report_analyze.DB",
        help="Path to Reporta Data Base",
    )

    args = parser.parse_args()
    SPACE = 20

    connection = utils.initialization_database(args.path_data_base)
    data_store = utils.parcer_file(args.path_file)

    moust_rating_app = report.filter_moust_rating_app(data_store, "News")
    print("\n", "#" * SPACE, " Apps News mais avaliada ", "#" * SPACE)
    print(
        "Utilizando a API do %(track_name)s para identifica "
        "as 10 Aplicações do gênero Music e Book com maior "
        "número de citações" % moust_rating_app
    )

    data = report.build_report_store_data(data_store)

    utils.generate_csv(data, args.path_report)
    utils.insert_report_data(connection, data)

    main_api(connection=connection)


def main_api(**settings):
    """ This function returns a Pyramid WSGI application.
    """
    config = Configurator(settings=settings)
    config.add_request_method(
        lambda r: settings['connection'],
        'dbsession',
        reify=True
    )
    
    config.scan('analyze_store_data.views')
    app = config.make_wsgi_app()
    
    print("Init server API in port 8080")
    server = make_server('0.0.0.0', 8080, app)
    server.serve_forever()

if __name__ == "__main__":
    main()