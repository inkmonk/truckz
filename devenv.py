from contextlib import contextmanager
from webapp.models import *
from toolspy import *

import json
from webapp.app_factory import create_app
import click


@click.command()
@click.option('--config', default=None)
@click.option('--dbname', default=None)
def app_console(config, dbname):

    app = create_app(db)

    app.config['TESTING'] = True
    app.config['WTF_CSRF_ENABLED'] = False

    # Needed for making the console work in app request context
    ctx = app.test_request_context()
    ctx.push()
    # app.preprocess_request()

    # The test client. You can do .get and .post on all endpoints
    client = app.test_client()

    get = client.get
    post = client.post
    put = client.put
    patch = client.patch
    delete = client.delete


    # Helper method for sending JSON POST.
    def jpost(url, **kwargs):
        return client.post(url, data=json.dumps(kwargs, default=dthandler),
                           content_type="application/json")


    def jput(url, **kwargs):
        return client.put(url, data=json.dumps(kwargs, default=dthandler),
                          content_type="application/json")


    def jpatch(url, **kwargs):
        return client.patch(url, data=json.dumps(kwargs, default=dthandler),
                            content_type="application/json")

    def jread(resp):
        return json.loads(resp.data)

    def rget(url, **kwargs):
        return jread(get(url, **kwargs))

    def rpost(url, **kwargs):
        return jread(post(url, **kwargs))

    def rjpost(url, **kwargs):
        return jread(jpost(url, **kwargs))


    # Use this in your code as `with login() as c:` and you can use
    # all the methods defined on `app.test_client`
    @contextmanager
    def login(email="demo@stickystamp.com", password="password"):
        client.post('/login', data={'email': email, 'password': password})
        yield
        client.get('/logout', follow_redirects=True)

    q = db.session.query
    add = db.session.add
    addall = db.session.add_all
    commit = db.session.commit
    delete = db.session.delete

    sitemap = app.url_map._rules_by_endpoint

    routes = {}
    endpoints = {}

    for rule in app.url_map._rules:
        routes[rule.rule] = rule.endpoint
        endpoints[rule.endpoint] = rule.rule
    try:
        import IPython
        IPython.embed()
    except:
        import code
        code.interact(local=merge(locals(), globals()))

if __name__ == '__main__':
    app_console()
