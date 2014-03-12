#-*-coding:utf-8-*-
from flask import Flask, jsonify, abort, request, url_for
from flask.ext.restful import Api, Resource, reqparse, fields, marshal

app = Flask(__name__)
api = Api(app)

# explicit local image
def make_public_url(headline):
    new_headline = {}
    for field in headline:
        if field == 'img':
        	# files under static folder can be accessed directly
        	# to generate the url, create StaticImage resource to reference its endpoint
            new_headline['img'] = url_for('staticimage', localpath = headline[field], _external = True)
        else:
            new_headline[field] = headline[field]
    return new_headline

class StaticImage(Resource):
	def __init__(self):
		super(StaticImage, self).__init__()

api.add_resource(StaticImage, '/static/system/media_image/<string:localpath>', endpoint = 'staticimage')

# mockup headlines
headlines = [
    {
      'id': 37354,
      'title': '90后小偷竟有“超强大脑”',
      'img': 'guide_37354/thumb.jpg',
      'created_at': '2014-03-12 09:24:05'
    },
    {
      'id': 37331,
      'title': '庆春路过江隧道出现漏水',
      'img': 'guide_37331/thumb.jpg',
      'created_at': '2014-03-12 08:18:07'
    },
    {
      'id': 37346,
      'title': '《新闻联播》竟然也下“彩蛋”',
      'img': 'guide_37346/thumb.jpg',
      'created_at': '2014-03-12 08:36:15'
    },
    {
      
      'id': 37338,
      'title': '老烟厂要变成杭城首个室内步行街',
      'img': 'guide_37338/thumb.jpg',
      'created_at': '2014-03-12 08:25:24'
    },
    {
      
      'id': 37371,
      'title': '假如对象从事过性工作，咋办',
      'img': 'guide_37371/thumb.jpg',
      'created_at': '2014-03-12 14:06:24'
    }
]

class HeadlineAPI(Resource):
	def get(self):
		return { 'headlines': map(make_public_url, headlines ) }

api.add_resource(HeadlineAPI, '/api/news/headline', endpoint = 'headlines')

# run server
if __name__ == '__main__':
    #app.run(debug = True)
	app.run(
	    host = 'mbpr2013.local', # in order to be accessed from cell phone
	    debug = True
	)