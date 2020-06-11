import pandas as pd
from datetime import date,timedelta,datetime
from tkinter import messagebox


class Insert(object):

    def __init__(self, df, csv_path):
        self.path = csv_path
        self.df = df

    def insert_day(self,inst_day, hours, tension):
        inst_day = date.fromisoformat(inst_day)
        day_str = inst_day
        try:
            hours = float(hours)
            tension = float(tension)
        except:
            messagebox.showerror(title='something wrong happens...', message="'Hours' and 'tension'\n"
                                                                             "must be numbers")
            raise Exception(TypeError)
        try:
            self.df.loc[day_str] = [hours, tension]
            self.df.to_csv(self.path,header=True)
            messagebox.showinfo(title='insertion done', message='date:{}\nhours:{}\ntension:{}'.format
                                                                (day_str, hours, tension))
        except:
            messagebox.showerror(title='sorry...', message='insert failed.')
            raise Exception('ERROR: INSERT FAILED\n'
                            'DATE:{}\n'.format(day_str),
                            'HOURS:{}\n'.format(hours),
                            'TENSION:{}'.format(tension))

