import requests

URL = "https://tenor.googleapis.com/v2/search?appversion=browser-r20240917-1&prettyPrint=false&key=AIzaSyC-P6_qz3FzCoXGLk6tgitZo4jEJ5mLzD8&client_key=tenor_web&locale=en_GB&anon_id=AAYijDTZ4OoCrIpgvhlAEw&q={}&limit=1&contentfilter=low&fields=next%2Cresults.id%2Cresults.media_formats%2Cresults.title%2Cresults.h1_title%2Cresults.long_title%2Cresults.itemurl%2Cresults.url%2Cresults.created%2Cresults.user%2Cresults.shares%2Cresults.embed%2Cresults.hasaudio%2Cresults.policy_status%2Cresults.source_id%2Cresults.flags%2Cresults.tags%2Cresults.copied_post_pid%2Cresults.content_rating%2Cresults.bg_color%2Cresults.legacy_info%2Cresults.geographic_restriction%2Cresults.content_description&searchfilter=none&component=web_mobile"

def fetchmeme(meme_name):
    url = URL.format(meme_name)

    response = requests.get(url)

    if response.status_code == 200:
        return response.json().get("results")[0].get('media_formats').get("mediumgif").get('url')
    else:
        print("Request failed to fetch meme")


