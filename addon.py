from xbmcswift2 import Plugin, xbmcgui
from resources.lib import mainaddon

plugin = Plugin()

URL1 = "https://feeds.soundcloud.com/users/soundcloud:users:276623469/sounds.rss" #SPOKENEDITION
URL2 = "https://feeds.megaphone.fm/theatlanticsdailyidea" #ATLANTICSDAILYIDEA
URL3 = "https://feeds.megaphone.fm/radioatlantic" #RADIOATLANTIC
URL4 = "https://feeds.megaphone.fm/theinterview" #THEATLANTICINTERVIEW
URL5 = "https://feeds.megaphone.fm/crazygenius" #CRAZYGENIUS

@plugin.route('/')
def main_menu():
    items = [
   {
            'label': plugin.get_string(30001), 
            'path': plugin.url_for('spoken_episodes'),
            'thumbnail': "https://i1.sndcdn.com/avatars-000323911236-xz3vii-original.jpg"},
   {
            'label': plugin.get_string(30002), 
            'path': plugin.url_for('daily_episodes'),
            'thumbnail': "https://megaphone-prod.s3.amazonaws.com/podcasts/e7243c36-77ec-11e9-b17a-7336227a9acb/image/uploads_2F1560355474940-ii2om4v0ktc-3943e9b6e78f1788e7694b9ef88f7a1b_2FAtlantic_daily_idea_3000x3000.png"},
   {
            'label': plugin.get_string(30003), 
            'path': plugin.url_for('radio_episodes'),
            'thumbnail': "https://megaphone-prod.s3.amazonaws.com/podcasts/99303972-bebd-11e9-afe6-6f2c4205c3ae/image/uploads_2F1565805801785-7uakn7v7nso-00bfba516d621370e97a74945f4bea2b_2FRA-3000x3000.jpg"},
   {
            'label': plugin.get_string(30004), 
            'path': plugin.url_for('interview_episodes'),
            'thumbnail': "https://cdn.theatlantic.com/assets/media/podcasts/series/2018/09/The_Atlantic_Interview/square.jpg"},
        {
            'label': plugin.get_string(30005),
            'path': plugin.url_for('crazygenius_episodes'),
            'thumbnail': "https://cdn.theatlantic.com/assets/media/podcasts/series/2019/04/CrazyGenius_Final_Cover_1/square.jpg"},
   ]
    return items

@plugin.route('/spoken_episodes/')
def all_episodes1():
    soup1 = mainaddon.get_soup1(URL1)
    playable_podcast1 = mainaddon.get_playable_podcast1(soup1)
    items = mainaddon.compile_playable_podcast1(playable_podcast1)
    return items

@plugin.route('/daily_episodes/')
def all_episodes2():
    soup2 = mainaddon.get_soup2(URL2)
    playable_podcast2 = mainaddon.get_playable_podcast2(soup2)
    items = mainaddon.compile_playable_podcast2(playable_podcast2)
    return items

@plugin.route('/radio_episodes/')
def all_episodes3():
    soup3 = mainaddon.get_soup3(URL3)
    playable_podcast3 = mainaddon.get_playable_podcast3(soup3)
    items = mainaddon.compile_playable_podcast3(playable_podcast3)
    return items

@plugin.route('/interview_episodes/')
def all_episodes4():
    soup4 = mainaddon.get_soup4(URL4)
    playable_podcast4 = mainaddon.get_playable_podcast4(soup4)
    items = mainaddon.compile_playable_podcast4(playable_podcast4)
    return items

@plugin.route('/crazygenius_episodes/')
def all_episodes5():
    soup5 = mainaddon.get_soup5(URL5)
    playable_podcast5 = mainaddon.get_playable_podcast5(soup5)
    items = mainaddon.compile_playable_podcast5(playable_podcast5)
    return items

if __name__ == '__main__':
    plugin.run()
