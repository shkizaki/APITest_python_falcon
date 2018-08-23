# coding: utf-8
import falcon
import json
class ItemsResource:
    def on_get(self, req, resp):
        value = req.params['key']
        items = {
            'title': 'Web API Test',
            'tags': [
                {'name': 'Test', 'Version':[]},
                {'name': 'request', value:[]}
            ]
        }
        print(req.headers)
        resp.status = falcon.HTTP_200
        resp.content_type = 'text/plain'
        resp.body = json.dumps(items, ensure_ascii=False)

    def on_post(self, req, resp):
        params = req.stream.read().decode('utf-8')
        items = {
            'title': 'Web API(POST)',
            'tags': [
                {'name': 'Test', 'Version':[]},
                {'name': 'request', params:[]}
            ]
        }
        resp.status = falcon.HTTP_200
        resp.content_type = 'text/plan'
        resp.body = json.dumps(items, ensure_ascii=False)

api = falcon.API()
api.add_route('/test_api', ItemsResource())

if __name__ == "__main__":
    from wsgiref import simple_server

    httpd = simple_server.make_server("localhost", 8008, api)
    httpd.serve_forever()
