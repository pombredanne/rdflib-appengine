import webapp2
from rdflib import Graph
from rdflib_appengine.ndbstore import NDBStore

_GRAPH_ID = 'default-graph'
_GRAPH_INSTANCE_ID = 'Graph-instance'

class MainPage(webapp2.RequestHandler):
    def get(self):
        #Access-Control-Allow-Origin: *
        self.response.headers['Access-Control-Allow-Origin'] = '*'
        self.response.headers['Content-Type'] = 'application/sparql-results+json; charset=utf-8'
        self.response.write(query(self.request.get('query')))

class FourOhFour(webapp2.RequestHandler):
    def get(self):
        #Access-Control-Allow-Origin: *
        self.response.headers['Access-Control-Allow-Origin'] = '*'
        self.response.set_status(404)

application = webapp2.WSGIApplication([
    ('/ds/.*', MainPage),
    ('/.*', FourOhFour),
], debug=True)

def update(q):
    graph().update(q)
    
def query(q):
    return graph().query(q).serialize(format='json')
    
def graph():
    return Graph(store = NDBStore(identifier = _GRAPH_ID))

