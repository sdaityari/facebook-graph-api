# Facebook contests

import requests
import json

TOKEN = ''

def user_likes_page(user_id, page_id):
    """
        Returns whether a user likes a page
    """
    url = 'https://graph.facebook.com/%d/likes/%d/' % (user_id, page_id)
    parameters = {'access_token': TOKEN}
    r = requests.get(url, params = parameters)
    result = json.loads(r.text)
    if result['data']:
        return True
    else:
        return False

def get_common_likes(post_id, page_id):
    """
        Returns the number of likes common to a post and the page
    """
    count_likes = 0
    url = 'https://graph.facebook.com/%d/likes/' % post_id
    parameters = {'access_token': TOKEN}
    r = requests.get(url, params = parameters)
    result = json.loads(r.text)
    for like in result['data']:
        if user_likes_page(int(like['id']), page_id):
            count_likes += 1
            print 1
    return count_likes

if __name__ == '__main__':
    print get_common_likes(10202535513136341, 490352370999414)