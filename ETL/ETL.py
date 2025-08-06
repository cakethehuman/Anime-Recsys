import requests
import pandas as pd
import time



anime_data = []

ses = requests.Session()
def get_info(id):
    url = f"https://api.jikan.moe/v4/anime/{id}/full"
    response = ses.get(url,timeout=120)
    if response.status_code == 200:
        try:
            data = response.json()
            print("Data has been read")
            return data
        except requests.exceptions.ReadTimeout:
            print("connection time out")
            df = pd.DataFrame(anime_data)
            df.to_csv("anime_list_test_error_saver.csv",index=False)
        except:
            print("error")
    else:
        print(f"{response.status_code} something wrong")
        


for id in range(64492,65001):
    anime_list = get_info(id)
    print(f"fetching {id}")

    
    if anime_list:
    #print(anime_list['data']["title"])
    #print(anime_list['data']["title_english"])
    #print(anime_list['data']["title_japanese"])
    #print(anime_list['data']["aired"]["from"])
    #print(anime_list['data']["aired"]["to"])
    #print(anime_list['data']["score"])
    #print(anime_list['data']["scored_by"])
        #for i in anime_list['data']["genres"]:
            #print(i["name"])
        #for i in anime_list['data']["themes"]:
            #print(i["name"])
        #for i in anime_list['data']["demographics"]:
            #print(i["name"])
        
        anime_list_data = {
            # titles
            "title" : f"{anime_list['data']['title']}",
            "title_english": f"{anime_list['data']['title_english']}",
            "title_japanese": f"{anime_list['data']['title_japanese']}",
            "image" : anime_list['data']['images']['jpg']["image_url"],
            
            # aired
            "aired_from": f"{anime_list['data']['aired']['from']}",
            "aired_to": f"{anime_list['data']['aired']['to']}",
            
            # episode status
            "synopsis": f"{anime_list['data']['synopsis']}",
            "status": anime_list['data']['status'],
            "episodes": anime_list['data']['episodes'],
            
            #popularity
            "rating": anime_list['data']['rating'],
            "rank": anime_list['data']['rank'],
            "popularity": anime_list['data']['popularity'],
            "members": anime_list['data']['members'],
            "favorites": anime_list['data']['favorites'],
            # score
            
            "score": anime_list['data']['score'],
            "scored_by": anime_list['data']['scored_by'],
            
            # features
            "genres": [f"{genre['name']}" for genre in anime_list['data']['genres']],
            "themes": [f"{theme['name']}" for theme in anime_list['data']['themes']],
            "demographics": [f"{demographics['name']}" for demographics in anime_list['data']['demographics']]
            } 
        
        anime_data.append(anime_list_data)
        df = pd.DataFrame(anime_data)
        df.to_csv("anime_list_60 - 65k.csv",index=False)
    time.sleep(1.5)
        
        
    
    


# fetching 36827

