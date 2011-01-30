import os
from google.appengine.ext.webapp import template
import logging

class Index:
    def __init__(self, request, records):
        self.request = request
        self.records = records
    
    def render(self, out):
        template_values = {
            'text' : 'test',
            'records' : self.records,
        }
        
        path = os.path.join('templates/index.html')
        logging.info(path)
        out.write(template.render(path, template_values))
        
class New:
    #def __init__(self, request):
    #    self.request = request
    #    self.records = records
    
    def render(self, out):
        template_values = {
            'text' : 'test',
        }
        
        path = os.path.join('templates/new.html')
        logging.info(path)
        out.write(template.render(path, template_values))
