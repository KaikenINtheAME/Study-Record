import pandas as pd
from tkinter import *


class Record(object):

    def __init__(self, csv_path):
        self.path = csv_path
        self.df = pd.DataFrame(pd.read_csv(self.path, index_col='date', parse_dates=True))

    def about(self):
        ab = Tk()
        ab.title('about')
        about_doc = '''
            version:0.2
            requires:
            \tPython version: 3.7.4
            \tpandas version: 0.25.1
            \tmatplotlib version: 3.1.1
            used TKINTERDATEPICKER code from Miguel Martinez Lopez
    
            email to seventhsamurai@outlook.com for any question
            '''
        Label(ab, justify="left", text=about_doc).pack()
        ab.mainloop()

    def manual(self):
        mn = Tk()
        mn.title('manual')
        manual_doc = """
             basic operation：
             1.add 
             \tpick a date
             \tenter learning hours and tension(-3 to 3 recommend)
             \tclick 'ok'

             2.alter
             \tpick a date
             \tclick 'show the record' to confirm record of the day
             \tenter new numbers of learning hours and tension
             \tclick 'ok'

             3.query
             \tchoose one from 'this week' 'last week' 'this month' 'last month' 'given' or 'all'
             \t(pick the start date and end date if you pick 'given')
             \tchoose the kind of view 
             \tclick 'show bar' or 'show hist' to get the bar or histogram chart

             CAUTION：
             \tit's still a demo
             \temail to seventhsamurai@outlook.com for any question 
             """
        Label(mn, justify='left', text=manual_doc).pack()
        mn.mainloop()
