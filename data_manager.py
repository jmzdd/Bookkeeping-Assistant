# data_manager.py
class DataManager:
    def __init__(self):
        self.work_day = None
        self.begin_time = None
        self.end_time = None

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
