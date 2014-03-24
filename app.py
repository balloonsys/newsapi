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
        elif field == 'imgs':
            new_headline['imgs'] = [];
            for img in headline[field]:
              new_headline['imgs'].append(url_for('staticimage', localpath = img, _external = True))
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
      'created_at': '2014-03-12 09:24:05',
      'ntype': 0
    },
    {
      'id': 37331,
      'title': '庆春路过江隧道出现漏水',
      'img': 'guide_37331/thumb.jpg',
      'created_at': '2014-03-12 08:18:07',
      'ntype': 0
    },
    {
      'id': 37346,
      'title': '《新闻联播》竟然也下“彩蛋”',
      'img': 'guide_37346/thumb.jpg',
      'created_at': '2014-03-12 08:36:15',
      'ntype': 0
    },
    {
      
      'id': 37338,
      'title': '老烟厂要变成杭城首个室内步行街',
      'img': 'guide_37338/thumb.jpg',
      'created_at': '2014-03-12 08:25:24',
      'ntype': 0
    },
    {
      
      'id': 37371,
      'title': '假如对象从事过性工作，咋办',
      'img': 'guide_37371/thumb.jpg',
      'created_at': '2014-03-12 14:06:24',
      'ntype': 0
    }
]

class HeadlineAPI(Resource):
	def get(self):
		return { 'headlines': map(make_public_url, headlines ) }

api.add_resource(HeadlineAPI, '/api/news/headline', endpoint = 'headlines')

# mockup latest news
latestNews = [
    {
      'id': 37974,
      'title': '恐婚时代：18个媒人说一门亲',
      'abstract': '彩礼3斤3两百元大钞。',
      'imgs': ['guide_37974/thumb.jpg'],
      'page_view': 312,
      'created_at': '2014-03-24 14:09:34',
      'ntype': 0
    },
    {
      'id': 37971,
      'title': '近4成青年的初夜在19岁前?',
      'abstract': '网友：我又拖后腿了！',
      'imgs': ['guide_37971/thumb.jpg'],
      'page_view': 748,
      'created_at': '2014-03-24 13:47:03',
      'ntype': 0
    },
    {
      'id': 37972,
      'title': '中国飞机发现白色方形漂浮物',
      'abstract': '从万米高空看，2块漂浮物面积较大',
      'imgs': ['guide_37972/thumb.jpg'],
      'page_view': 277,
      'created_at': '2014-03-24 13:37:41',
      'ntype': 0
    },
    {
      'id': 37970,
      'title': '学校惊现上吊女尸？',
      'abstract': '惊！吓！',
      'imgs': ['guide_37970/thumb.jpg'],
      'page_view': 608,
      'created_at': '2014-03-24 12:16:03',
      'ntype': 0
    },
    {
      'id': 37968,
      'title': '出差找“艳遇”嫌丑被捅伤',
      'abstract': '哑巴吃黄连，他也不敢报警',
      'imgs': ['guide_37968/thumb.jpg'],
      'page_view': 429,
      'created_at': '2014-03-24 10:52:19',
      'ntype': 0
    },
    {
      'id': 37966,
      'title': '四大行发难支付宝的前因后果',
      'abstract': '你怎么看？快来投一票吧',
      'imgs': ['guide_37966/thumb.jpg'],
      'page_view': 1211,
      'created_at': '2014-03-24 10:47:17',
      'ntype': 0
    },
    {
      'id': 37967,
      'title': '四大行封杀余额宝：徒劳且不智',
      'abstract': '四大行封杀余额宝提供了一个很好的司法案例',
      'imgs': ['guide_37967/thumb.jpg'],
      'page_view': 393,
      'created_at': '2014-03-24 10:21:36',
      'ntype': 0
    },
    {
      'id': 37941,
      'title': '马云回应：虽死犹生 必须扛住',
      'abstract': '工，农，中，建四大银行一致限制支付宝用户额度',
      'imgs': ['guide_37941/thumb.jpg'],
      'page_view': 312,
      'created_at': '2014-03-24 10:14:50',
      'ntype': 0
    },
    {
      'id': 37965,
      'title': '两男一女开着跑车偷羊',
      'abstract': '村民纷纷奔走相告：“大灰狼”抓到了!',
      'imgs': ['guide_37965/thumb.jpg'],
      'page_view': 460,
      'created_at': '2014-03-24 10:03:36',
      'ntype': 0
    },
    {
      'id': 37964,
      'title': '被苹果玩坏的iOS 7你中枪没？',
      'abstract': '涉及蓝牙指纹等多方面',
      'imgs': ['guide_37964/thumb.jpg'],
      'page_view': 312,
      'created_at': '2014-03-24 10:02:42',
      'ntype': 0
    }
]

latestNewsInPage2 = [
    {
      'id': 37963,
      'title': '双燃料出租车想要“喝”气不容易',
      'abstract': '唯一加气点在半山 ，排队要排近一个小时……',
      'imgs': ['guide_37963/thumb.jpg'],
      'page_view': 88,
      'created_at': '2014-03-24 09:57:46',
      'ntype': 0
    },
    {
      'id': 37513,
      'title': '3.15】曝光台',
      'abstract': '',
      'imgs': ['guide_37513/thumb.jpg'],
      'page_view': 620,
      'created_at': '2014-03-15 11:13:40',
      'ntype': 1
    },
]

class LatestNewsAPI(Resource):
  def get(self):
    p = int(request.args.get('page', 1))
    if p == 1:
      return { 'data': map(make_public_url, latestNews ), 'has_more': True }
    else:
      return { 'data': map(make_public_url, latestNewsInPage2 ), 'has_more': False }

api.add_resource(LatestNewsAPI, '/api/news/list', endpoint = 'latestnews')

# run server
if __name__ == '__main__':
    #app.run(debug = True)
	app.run(
	    host = 'mbpr2013.local', # in order to be accessed from cell phone
	    debug = True
	)