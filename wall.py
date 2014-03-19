import requests
import json

TOKEN = ''

def get_posts():
    """
        Returns the list of posts on my timeline
    """

    parameters = {'access_token': TOKEN}
    r = requests.get('https://graph.facebook.com/me/feed', params=parameters)
    result = json.loads(r.text)
    return result['data']

def comment_on_posts(posts):
    """Comments on all posts"""
    for post in posts:
        url = 'https://graph.facebook.com/%s/comments' % post['post_id']
        message = 'Commenting through the Graph API'
        parameters = {'access_token': TOKEN, 'message': message}
        s = requests.post(url, data = parameters)

if __name__ == '__main__':
    print get_posts()