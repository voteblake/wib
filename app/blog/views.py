""" Module containing Flask routes and view logic. """
import os
from flask import render_template
import twitter, requests

from . import blog
from app import pages

def get_latest_location():
    """
    Gets latest user location via a call to the Twitter API
    Finds most recent tweet that contains a geocode and is not a retweet
    Returns the a list [lat, long] of that location
    """
    api = twitter.Api(consumer_key=os.environ.get('TCK'),
                      consumer_secret=os.environ.get('TCS'),
                      access_token_key=os.environ.get('TATK'),
                      access_token_secret=os.environ.get('TATS'))
    statuses = api.GetUserTimeline('VoteBlake')
    locations = [s.coordinates for s in statuses if s.coordinates and s.retweeted == False]
    long, lat = locations[0]['coordinates']

    location = [lat, long]

    return location


def format_location(location):
    """
    Formats a [lat, long] list in to a Google maps API formatted address
    """
    url = 'https://maps.googleapis.com/maps/api/geocode/json?latlng=' + str(location[0]) + ',' + str(location[1]) + '&sensor=false&result_type=locality|administrative_area_level_1|country&key=' + os.environ.get('GKEY')
    r = requests.get(url)

    return ''.join([c for c in r.json()['results'][0]['formatted_address'] if not c.isdigit()])


@blog.route('/')
@blog.route('/posts')
def posts():
    """ Index route of the blueprint """
    blog_posts = (p for p in pages)
    latest = sorted(blog_posts, reverse=True, key=lambda p: p.meta['date'])

    location = get_latest_location()

    return render_template('blog/posts.html', posts=latest, location=format_location(location), lat=location[0], long=location[1])

@blog.route('/<path:path>/')
def post(path):
    """ Individual blog post page """
    blog_post = pages.get_or_404(path)
    return render_template('blog/post.html', post=blog_post)
