DOMAINS = {
    'api': '{{  pillar["application"]["settings"]["domains"]["api"] }}',
    'microsites': '{{  pillar["application"]["settings"]["domains"]["microsites"] }}',
    'workspace': '{{  pillar["application"]["settings"]["domains"]["workspace"] }}',
    'cdn': '{{  pillar["application"]["cdn"] }}',
}

DOMAINS_ENGINE = {
    'api': '{{  pillar["application"]["settings"]["domains_engine"]["api"] }}',
    'microsites': '{{  pillar["application"]["settings"]["domains_engine"]["microsites"] }}',
    'workspace': '{{  pillar["application"]["settings"]["domains_engine"]["workspace"] }}',
}

RAVEN_CONFIG = {
    'dsn': '{{ pillar["sentry_dns_api"] }}',
}

DEBUG = {{ pillar["application"]["settings"]["debug"]}}
