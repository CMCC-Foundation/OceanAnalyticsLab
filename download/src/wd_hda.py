from download.src.working_domain import WorkingDomain
from download.src import time_utils


class WorkingDomainHda(WorkingDomain):
    def get_time(self):
        # enable this to download splitted file from hda
        # time_list_raw is a pandas.DataTimeIndex: An immutable container for datetimes -> to convert in str
        # with the appropriate format
        time_list_raw = time_utils.generate_time_list(self.get_start_time(), self.get_end_time(), self.get_time_freq())
        time_list = [
            self.get_formatted_date(time.year, str(time.month).zfill(2), str(time.day).zfill(2), self.get_time_freq())
            for time in time_list_raw
        ]

        return [time_list[0], time_list[-1]]

    def get_formatted_date(self, year, month, day, time_freq):
        date_formatted = "{}-{}-{}".format(year, month, day)

        return date_formatted
