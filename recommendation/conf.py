from os import environ as env


DEBUG = env.get('RECOMMENDATION_ENV', 'development') == 'development'
KEY_PREFIX = env.get('RECOMMENDATION_KEY_PREFIX', 'query_')

CACHE_TTL = env.get('RECOMMENDATION_CACHE_TTL', 7 * 24 * 60 * 60)
MEMCACHED_TTL = env.get('RECOMMENDATION_MEMCACHED_TTL', CACHE_TTL)

BING_ACCOUNT_KEY = env.get('BING_ACCOUNT_KEY', '')
EMBEDLY_API_KEY = env.get('EMBEDLY_API_KEY', '')
YAHOO_OAUTH_KEY = env.get('YAHOO_OAUTH_KEY', '')
YAHOO_OAUTH_SECRET = env.get('YAHOO_OAUTH_SECRET', '')


RECOMMENDATION_SERVICES = env.get('RECOMMENDATION_SERVICES')
if DEBUG and RECOMMENDATION_SERVICES:
    REDIS_HOST = RECOMMENDATION_SERVICES
    REDIS_PORT = 6379
    REDIS_DB = 0
    MEMCACHED_HOST = '%s:11211' % RECOMMENDATION_SERVICES
else:
    REDIS_HOST = env.get('REDIS_HOST', 'localhost')
    REDIS_PORT = env.get('REDIS_PORT', 6379)
    REDIS_DB = env.get('REDIS_DB', 0)
    MEMCACHED_HOST = env.get('MEMCACHED_HOST', 'memcached:11211')

CELERY_BROKER_URL = env.get('CELERY_BROKER_URL', 'redis://%s:%d/%d' %
                            (REDIS_HOST, REDIS_PORT, REDIS_DB))
