from flask import Flask
from flask_limiter import Limiter, HEADERS
from flask_limiter.util import get_remote_address

app = Flask(__name__)
limiter = Limiter(
    app,
    key_func=get_remote_address,
    default_limits=["200000000 per day", "500000 per hour"],
    retry_after='seconds',
    headers_enabled=True
)
limiter._header_mapping[HEADERS.RESET] = 'X-Reset'
limiter._header_mapping[HEADERS.LIMIT] = 'X-Limit'
limiter._header_mapping[HEADERS.REMAINING] = 'X-Remaining'


@app.route('/')
@limiter.limit("10/10 seconds", override_defaults=False)
def main_page():
    return "The WWT study group is amazing"


if __name__ == '__main__':
    app.run()
