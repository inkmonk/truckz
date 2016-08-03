"""
Custom filters for use in Jinja2 templates
"""
import time
import hashlib
import hmac
from flask.json import _json
from flask_sqlalchemy_booster import json_encoder
from datetime import timedelta


def timestampize(dt):
    return time.mktime(dt.timetuple())


def hash_hmac(message, secret_key, algo_name):
    return hmac.new(
        secret_key, message, getattr(hashlib, algo_name)).hexdigest()


def json_dumps(obj):
    return _json.dumps(obj, default=json_encoder)


def capitalize_words(sentence):
    return ' '.join(word.capitalize() for word in sentence.split(" "))


def readable_timestamp(timestamp):
    if timestamp is None:
        return "Not Available"
    return timestamp.strftime("%B %d, %Y %I:%M %p")


def readable_boolean(boolean_val):
    if boolean_val:
        return "Yes"
    else:
        return "No"


def format_datetime(dt, format_string):
    if dt is None:
        return ""
    return dt.strftime(format_string)


def attrs_list(obj, attrs):
    return [getattr(obj, attr) for attr in attrs]

def decimal_part(number):
    if number is None:
        return None
    return str(number).partition('.')[-1]


def url_without_query_params(url):
    if url is None:
        return None
    return url.partition('?')[0]


def todict(
        item, rels_to_expand=None, attrs_to_serialize=None,
        rels_to_serialize=None, group_listrels_by=None):
    if item is None:
        return None
    if isinstance(item, list):
        return[m.todict(
            rels_to_expand=rels_to_expand,
            attrs_to_serialize=attrs_to_serialize,
            rels_to_serialize=rels_to_serialize,
            group_listrels_by=group_listrels_by) for m in item]
    return item.todict(
        rels_to_expand=rels_to_expand,
        attrs_to_serialize=attrs_to_serialize,
        rels_to_serialize=rels_to_serialize,
        group_listrels_by=group_listrels_by)


def partition(s, delim):
    if s is None or delim is None:
        return (None, None)
    res = s.partition(delim)
    return (res[0], res[-1])


def time_delta(dt, **kwargs):
    if dt is None:
        return None
    return dt + timedelta(**kwargs)
