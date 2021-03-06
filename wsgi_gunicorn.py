#!/usr/bin/env python
# -*- coding: utf-8 -*-
from werkzeug.contrib.fixers import ProxyFix

from odot.server import create_app

app = create_app('odot')

app.wsgi_app = ProxyFix(app.wsgi_app)


if __name__ == '__main__':
    app.run(host='0.0.0.0')
