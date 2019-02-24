""" module to methods reports processor """

import time
import twitter
from datetime import datetime
from analyze_store_data import utils, config

api = twitter.Api(
    consumer_key=config.TWITTER_API_KEY,
    consumer_secret=config.TWITTER_API_SECRET_KEY,
    access_token_key=config.TWITTER_ACCESS_TOKEN,
    access_token_secret=config.TWITTER_SECRET_TOKEN,
)


def filter_moust_rating_app(data, categoria):
    """ filter data to get news app """

    report = sorted(
        list(filter(lambda d: d["prime_genre"] == categoria, data)),
        key=lambda k: float(k["rating_count_tot"]),
        reverse=True,
    )
    return report[:1][-1]


def get_twitter_citations(app_name):
    max_id = 0
    count = 0
    start = datetime.utcnow()
    print("Getting citations of:", app_name)

    while max_id >= 0:
        retries = 0
        success = False
        while not success:
            print(".", sep=" ", end="", flush=True)

            try:
                r = api.GetSearch(
                    term=app_name,
                    max_id=max_id,
                    count=100,
                    return_json=True,
                    result_type="recent",
                )
                time.sleep(5)
                success = True

                for i in r["statuses"]:
                    count += 1
                    c = datetime.strptime(i["created_at"], config.PATTERN).replace(
                        tzinfo=None
                    )
                    if (start - c).seconds > config.THRESHOLD:
                        max_id = 0

            except Exception as e:
                print("Retrying", count, e)
                retries += 1
                time.sleep(450)

        next = r["search_metadata"].get("next_results")
        if next:
            max_id = int(next[next.find("max_id=") + 7 : next.find("&")])
        else:
            max_id = -1

    print("TOTAL:", count)
    return count


def build_report_store_data(data, r_sorted=True):
    """ build and proccess report to data from AppleStore  """

    filter_category = ["Book", "Music"]
    _data = list(filter(lambda d: d["prime_genre"] in filter_category, data))

    if r_sorted:
        _data = sorted(_data, key=lambda k: float(k["rating_count_tot"]), reverse=True)

    for app in _data:
        citations = get_twitter_citations(app["track_name"])
        # import random
        # citations = random.randint(1, 100000)
        app["n_citacoes"] = citations

    _data = sorted(_data, key=lambda k: float(k["n_citacoes"]), reverse=True)
    report = [
        {key: d.get(key, "") for key in utils.REPORT_HEAD_LIST} for d in _data[:10]
    ]
    return report
