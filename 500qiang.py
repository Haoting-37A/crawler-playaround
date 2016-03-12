import requests

def access_pages(id_lst, url_prefix, access_token):
    param_page = {"access_token": access_token, "fields": "posts"}
    for id in id_lst:
        r = requests.get(url_prefix+id, params=param_page)
        r_json = r.json()
        post_id = r_json.get('id')
        tmp_type = access_post(post_item)
        

def access_posts(post_id, url_prefix, access_token):
    param_post = {"access_token": access_token, "fields": "status_type"}
    r = requests.get(url_prefix+id, params=param_post)
    r_json = r.json()
    post_type = r_json.get('status_type')
    return post_type

if __name__ == '__main__':
    id_lst = ['125524087493943']
    access_token = 'CAACEdEose0cBAFYSdLxR1t8RtI0ab6tE5pjfow0wdppZAVLOsZC2uuYvz1GZBeJYYTkkWsx7qdCG4WAQvZCE3qL4tjGKlW2ppHSZCpFJPJl7pwFjeZBPmektO8b41byE6tUtzPrZAMAo4Tm3qP4ac37FtZAwhQv1LbETo9ZABHRJh1GlhlTtKZBZC7xJe8BLYXAGeEF2onmr9UighQVyyJK8spV'
    access_pages(id_lst, 'http://graph.facebook.com/v2.5/', access_token)
