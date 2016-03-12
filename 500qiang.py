import requests

def access_pages(id_lst, url_prefix, access_token):
    param_page = {"access_token": access_token, "fields": "posts"}
    for id in id_lst:
        r = requests.get(url_prefix+id, params=param_page)
        r_json = r.json()
        posts = r_json.get('posts').get('data')
        for post in posts:
            post_id = post.get('id')
            tmp_type = access_posts(post_id, url_prefix, access_token)
            print tmp_type

def access_posts(post_id, url_prefix, access_token):
    param_post = {"access_token": access_token, "fields": "status_type"}
    r = requests.get(url_prefix+post_id, params=param_post)
    r_json = r.json()
    post_type = r_json.get('status_type')
    return post_type

if __name__ == '__main__':
    id_lst = ['125524087493943']
    access_token = 'CAACEdEose0cBAIj8fUrZCoaZCVkg4xOwp70kR2T8U8OVNHw2BCNZBiyzIIALiQA87EZCUYQ7EuCuxioQepWWI5s7YOtNGBhpsslbsGKxtpwh4TNC74ZCz4Cvi5bWZCVsRHR9UNwX1lVzrGF0IqXgg7Y91u7zoSZChxrDiZC9hVFXA3jRTr6JVlXQYQ3tetYV6Fl4S08BRL02bUrbb2OYr5d4'
    access_pages(id_lst, 'https://graph.facebook.com/v2.5/', access_token)
