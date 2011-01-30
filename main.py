#!/usr/bin/env python

from google.appengine.ext import webapp
from google.appengine.ext.webapp import util

import controller

def main():
    application = webapp.WSGIApplication([('/', controller.IndexRecords), 
                                          ('/new', controller.NewRecord)],
                                         debug=True)
    util.run_wsgi_app(application)


if __name__ == '__main__':
    main()
