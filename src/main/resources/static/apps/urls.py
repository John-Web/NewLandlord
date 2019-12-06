from apps.account.views import IndexHandler, LoginHandler, SignupHandler
from apps.game.views import SocketHandler

url_patterns = [
    ('/', IndexHandler),
    ('/login', LoginHandler),
    ('/signup', SignupHandler),
    ('/ws', SocketHandler),
]
