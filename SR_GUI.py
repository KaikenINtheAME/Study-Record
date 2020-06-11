from tkinter import *
from TKINTERDATEPICKER import *
from SR_Record import Record
from SR_insert import Insert
from SR_query import Query
import os
import csv

if __name__ == "__main__":
    csv_path = './SR.csv'

    # create the csv file if not exist
    if os.path.isfile(csv_path):
        pass
    else:
        fileHeader = ['date', 'hours', 'tension']
        SR = open(csv_path, 'w')
        writer = csv.writer(SR)
        writer.writerow(fileHeader)
        SR.close()

    r = Record(csv_path)
    q = Query(r.df)
    i = Insert(r.df, csv_path)

    wd = Tk()
    wd.title('StudyRecord')
    wd.geometry('600x750')
    insertframe = ttk.LabelFrame(wd, text='Add / Alter', padding='50 50 50 50', height=250, width=500,
                                 borderwidth=10)
    insertframe.place(x=50, y=50)

    picked_date = StringVar()
    tension = StringVar()
    study_hours = StringVar()

    date_prompt = ttk.Label(wd, text='date:')
    dp_insert = Datepicker(wd, datevar=picked_date)
    show_existing_button = ttk.Button(wd, text='show the record of the day',
                                      command=lambda: (q.show_theday(picked_date.get())))
    sh_prompt = ttk.Label(wd, text='learned')
    hours_entry = Entry(wd, textvariable=study_hours, show=None)
    tension_prompt = ttk.Label(wd, text='hours,tension：')
    tension_entry = Entry(wd, textvariable=tension, show=None)
    add_button = ttk.Button(wd, text='ok',
                            command=lambda: (i.insert_day(picked_date.get(),
                                                          study_hours.get(), tension.get())))

    # insert frame layout
    date_prompt.place(x=100, y=100)
    dp_insert.place(x=150, y=100)
    show_existing_button.place(x=300, y=100)
    sh_prompt.place(x=100, y=200)
    hours_entry.place(x=150, y=200)
    tension_prompt.place(x=250, y=200)
    tension_entry.place(x=340, y=200)
    add_button.place(x=350, y=250)

    queryframe = ttk.Labelframe(wd, text='Query', padding='50 50 50 50', height=250, width=500,
                                borderwidth=10)
    queryframe.place(x=50, y=400)

    sd_start = StringVar()
    sd_end = StringVar()
    start_date = StringVar()
    end_date = StringVar()
    interval = StringVar()
    wv_or_mv = StringVar()

    dp_start = Datepicker(wd, datevar=sd_start)
    dp_end = Datepicker(wd, datevar=sd_end)

    tw = ttk.Radiobutton(wd, text='This Week', variable=interval, value='tw')
    lw = ttk.Radiobutton(wd, text='last Week', variable=interval, value='lw')
    tm = ttk.Radiobutton(wd, text='This Month', variable=interval, value='tm')
    lm = ttk.Radiobutton(wd, text='Last Month', variable=interval, value='lm')
    sd = ttk.Radiobutton(wd, text='given', variable=interval, value='sd')
    al = ttk.Radiobutton(wd, text='All', variable=interval, value='all')
    wv = ttk.Radiobutton(wd, text='Week View', variable=wv_or_mv, value='wv')
    mv = ttk.Radiobutton(wd, text='Month View', variable=wv_or_mv, value='mv')
    dv = ttk.Radiobutton(wd, text="Day View", variable=wv_or_mv, value='')

    stoe = ttk.Label(wd, text='to')
    hist = ttk.Button(wd, text='show hist', command=lambda: (q.get_method('h', interval.get(),
                                                                          sd_start.get(), sd_end.get(),
                                                                          wv_or_mv.get())))
    bar = ttk.Button(wd, text='show bar', command=lambda: (q.get_method('b', interval.get(),
                                                                        sd_start.get(), sd_end.get(),
                                                                        wv_or_mv.get())))

    # query frame layout
    tw.place(x=100, y=450)
    lw.place(x=200, y=450)
    tm.place(x=300, y=450)
    lm.place(x=400, y=450)
    sd.place(x=100, y=500)
    al.place(x=100, y=550)
    wv.place(x=150, y=550)
    mv.place(x=260, y=550)
    dv.place(x=400, y=550)
    dp_start.place(x=180, y=500)
    stoe.place(x=330, y=500)
    dp_end.place(x=350, y=500)
    hist.place(x=300, y=600)
    bar.place(x=400, y=600)

    manual_button = ttk.Button(wd, text='manual', command=lambda: (r.manual()))
    about_button = ttk.Button(wd, text='about', command=lambda: (r.about()))

    manual_button.place(x=370, y=680)
    about_button.place(x=470, y=680)

    wd.mainloop()
