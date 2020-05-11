from matplotlib import pyplot as plt
import matplotlib.dates as mdates
from datetime import date, timedelta
import numpy as np
import pandas as pd
from pandas.plotting import register_matplotlib_converters
from tkinter import messagebox


class Query(object):
    def __init__(self, df):
        self.df = df
        register_matplotlib_converters()

    def get_method(self, hb, str_=None, start=None, end=None, wv_or_mv=''):
        """calls 'getxx' functions to give the start date and end date to
        'show_bar' or 'show_hist' """
        if str_ != 'sd':
            try:
                method = getattr(self, 'get' + str_, None)
                s, e, = method()
            except(TypeError, IndexError, KeyError):
                messagebox.showerror(title='Error', message="Can not get the date period")
                s, e = None, None
        elif start and end:
            s = start
            e = end

        else:
            messagebox.showerror(title='ERR', message='info：\n'
                                 'str={}，start={}，end={}'.format(str_, start, end))

        if s is not None and e is not None:
            if hb == 'b':
                self.show_bar(s, e, wv_or_mv)
            elif hb == 'h':
                self.show_hist(s, e, wv_or_mv)
            else:
                raise Exception("Error occurs in 'get_method'")

    def gettw(self):
        """return the date period of this week"""
        tw_end = date.today()
        tw_start = (date.today() - timedelta(days=date.weekday(date.today())))
        return tw_start, tw_end

    def getlw(self):
        """return the date period of last week"""
        lw_end = (date.today() - timedelta(date.weekday(date.today()) + 1))
        lw_start = lw_end - timedelta(days=6)
        return lw_start, lw_end

    def gettm(self):
        """return the date period of this month"""
        tm_end = date.today()
        tm_start = date(date.today().year, date.today().month, 1)
        return tm_start, tm_end

    def getlm(self):
        """return the date period of last month"""
        lm_end = (date(date.today().year, date.today().month, 1) - timedelta(days=1))
        lm_start = date(lm_end.year, lm_end.month, 1)
        return lm_start, lm_end

    def getall(self):
        """return all of the records"""
        try:
            return self.df.index[0], self.df.index[-1]
        except IndexError:
            messagebox.showinfo(title='No record', message="log is empty, go on learning!")
        except:
            messagebox.showerror(title="sorry", message="something wrong happens in 'getall' method.")

    def show_theday(self, picked_date):
        """show record of picked date"""
        try:
            (hours, tension) = self.df.loc[picked_date]
            messagebox.showinfo(title="record of {}".format(picked_date),
                                message="learned {} hours, \ntension:{}".format(hours, tension))
        except KeyError:
            messagebox.showinfo(title="record of {}".format(picked_date),
                                message="No record")
        except:
            raise Exception("something beside KeyError happened.")

        return

    def show_bar(self, start=None, end=None, wv_or_mv=''):
        """plot the learning hours bar graph and tension line graph
        for the period using given view"""
        # daily view (default)
        if wv_or_mv == '':
            dates = self.df[start:end].index
            hours = self.df.loc[start:end]['hours']
            tension = self.df[start:end]['tension']
            if len(dates) <= 10:
                locator = mdates.DayLocator()
            else:
                locator = mdates.MonthLocator()
            width = 0.8
        # week view
        elif wv_or_mv == 'wv':
            dates = self.df[start:end].resample('W').sum().index
            hours = self.df[start:end].resample('W').sum()['hours']
            tension = self.df[start:end].resample('W').sum()['tension']
            locator = mdates.DayLocator()
            width = 1
        # month view
        elif wv_or_mv == 'mv':
            dates = self.df[start:end].resample('M').sum().index
            hours = self.df[start:end].resample('M').sum()['hours']
            tension = self.df[start:end].resample('M').sum()['tension']
            locator = mdates.DayLocator()
            width = 1
        else:
            raise Exception("ERROR in parameter 'wv_or_mv' ")

        formatter = mdates.DateFormatter('%a,\n%b %d')

        fig, ax1 = plt.subplots()

        # the Hours axis
        ax1.xaxis.set_major_locator(locator)
        ax1.xaxis.set_major_formatter(formatter)
        ax1.tick_params(axis='x')
        ax1.set_ylabel('Hours')

        # the Tension axis
        ax2 = ax1.twinx()
        ax2.set_ylabel('Tension')

        # Hours graph
        ax1.bar(dates, hours, facecolor='blue', alpha=0.3, width=width)

        # function for text
        def text_left_top(ax, cmstr='', height=0.92):
            ax.text(x=0.01, y=height, s=cmstr, transform=ax.transAxes)

        # text total hours
        text_left_top(ax=ax1, cmstr='Total Hours:{}'.format(str(hours.sum())), height=0.92)

        # text total tension
        text_left_top(ax=ax2, cmstr='Tension:{}'.format(str(tension.sum())), height=0.87)

        # Tension graph
        ax2.plot(dates, tension, 'ko--')

        # title
        plt.title("Record from {} to {}".format(start, end))
        plt.show()
        return

    def show_hist(self, start, end, wv_or_mv=''):
        """ plot the histogram of hours and tension in given period
        using given view"""
        if wv_or_mv == '':
            hours = self.df.loc[start:end]['hours']
            tension = self.df.loc[start:end]['tension']
        elif wv_or_mv == 'wv':
            hours = self.df.resample('W').sum()['hours']
            tension = self.df.resample('W').sum()['tension']
        elif wv_or_mv == 'mv':
            hours = self.df.resample('M').sum()['hours']
            tension = self.df.resample('M').sum()['tension']
        else:
            raise Exception("ERROR in parameter 'wv_or_mv' ")

        # create a fig with 2 rows and 1 column
        # subplot_1 is the hist of Hours
        plt.subplot(211)
        plt.title('Histogram from {} to {}'.format(start, end))
        plt.subplots_adjust(hspace=0.3)
        plt.hist(hours, align='left', rwidth=200, range=(0, 10))
        plt.xlabel('Hours')

        # turn to subplot_2
        # subplot_2 is the hist of tension
        plt.subplot(212)
        plt.hist(tension, align='left', bins=np.arange(-3, 5), rwidth=200)
        plt.xlabel('Tension')
        plt.show()
        return
