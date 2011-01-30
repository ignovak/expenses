from google.appengine.ext import webapp
from google.appengine.ext.webapp import util
from google.appengine.ext import db
from datetime import datetime

import view

import logging

class Expenses(db.Model):
    """Table with expance records (date, name, amount, description)"""
    date = db.DateTimeProperty()
    value = db.IntegerProperty()
    type = db.BooleanProperty()
    owner = db.StringProperty()
    name = db.StringProperty()
    description = db.TextProperty()

class IndexRecords(webapp.RequestHandler):
    def get(self):
        res = Expenses.all().order('-date')
        records = [i for i in res]
        page = view.Index(self.request, records)
        page.render(self.response.out)

class NewRecord(webapp.RequestHandler):
    def get(self):
        page = view.New()
        page.render(self.response.out)
        #self.response.out.write('Hello world!')
    def post(self):
        rec = Expenses()
        rec.name = self.request.get('name')
        rec.value = int(self.request.get('value'))
        rec.owner = self.request.get('owner')
        rec.type = self.request.get('type') == 'increase'
        rec.date = datetime.now()
        rec.description = self.request.get('description')
        rec.put()
        #IndexRecords().get()
        #self.response.out.write('Ok!\n<a href=\'/\'>Return to list</a>')
        self.redirect("/")
