import logging


# middleware.py
class SampleMiddleware(object):
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # 前処理
        self.process_request(request)
        # ビューの処理
        response = self.get_response(request)
        # 後処理
        self.process_response(request, response)

        return response

    def process_request(self, request):
        if 'user_id' not in request.session:
            print('uuuu')

        
    
    def process_response(self, request, response):
        # logfile = r"/Users/Tatsuki/projects/django/book_shop_api/book_shop_api/development.log"
        # logging.basicConfig(filename=logfile, level=logging.DEBUG)
        # logging.info(request)
        # logging.info(request.session.get('user_id'))
        # print(request.session.get('user_id'))
        print("レスポンス")
