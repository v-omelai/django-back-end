from rest_framework.throttling import AnonRateThrottle


class ProxyThrottle(AnonRateThrottle):
    rate = '5/min'
