from openpyxl import Workbook
from openpyxl import load_workbook

class AdInfo:
    
    def __init__(self, adinfo_template):
        '''
        :param: adinfo_template: filename for adinfo json template.

        '''
        self.adinfo_template = adinfo_template

    def open_file(self, filename):
        wb = load_workbook(filename=filename)
        return wb

    def get_adinfo_data(self, adinfo_filename, adinfo_template=self.adinfo_template):
        data = self.open_file(filename).active
        json_template = None
        json_adinfo_heading = None
        with open(adinfo_template, 'r') as template:
            json_template = json.load(template)
        for key in json_template['heading']:
            json_adinfo_heading[key] = data[json_template[key]]


 
