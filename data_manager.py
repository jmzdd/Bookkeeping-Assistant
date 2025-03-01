# data_manager.py
import flet as ft

class DataManager:
    def __init__(self):
        self.work_day = None
        self.begin_time = None
        self.end_time = None
        self.name = ""
        self.hourly_rate = 0
        self.hourly_rate_list = []
        self.all_money = 0
        self.time_diffs = []
        self.work_days = []
        self.start_times = []
        self.end_times = []

    def set_work_day(self, work_day):
        self.work_day = work_day

    def get_work_day(self):
        return self.work_day

    def set_begin_time(self, begin_time):
        self.begin_time = begin_time

    def get_begin_time(self):
        return self.begin_time

    def set_end_time(self, end_time):
        self.end_time = end_time

    def get_end_time(self):
        return self.end_time

    def set_name(self, name):
        self.name = name

    def get_name(self):
        return self.name

    def set_hourly_rate(self, hourly_rate):
        self.hourly_rate = hourly_rate

    def get_hourly_rate(self):
        return self.hourly_rate

    def add_data(self, time_diff, work_day, start_time, end_time):
        self.time_diffs.append(time_diff)
        self.work_days.append(work_day)
        self.start_times.append(start_time)
        self.end_times.append(end_time)

    def delete_data(self):
        self.time_diffs.pop()
        self.work_days.pop()
        self.start_times.pop()
        self.end_times.pop()