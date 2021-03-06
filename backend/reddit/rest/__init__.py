from reddit.rest.comment import routes as comment_routes
from reddit.rest.topic import routes as topic_routes

ALL_ROUTES = [
    comment_routes,
    topic_routes,
]


def initialize(app):
    for endpoints in ALL_ROUTES:
        for route in endpoints:
            app.add_url_rule(route.path, view_func=route.handler)
