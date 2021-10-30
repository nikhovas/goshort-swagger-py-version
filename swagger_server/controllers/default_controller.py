import connexion
import six
import flask

from swagger_server import util


def redirect(key):  # noqa: E501
    """Get redirection page

     # noqa: E501

    :param key: Url key
    :type key: str

    :rtype: None
    """
    if key == 'demo':
        return flask.redirect('example.com', code=301)
    else:
        return '', 404
