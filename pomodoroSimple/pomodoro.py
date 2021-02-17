import datetime
import time


class Pomodoro:

    NO_TIMER = 0
    TASK_TIMER = 1
    SHORT_BREAK_TIMER = 2
    LONG_BREAK_TIMER = 3

    def __init__(self, timerLength, pomodoroSession):

        # define goals
        self.task_goal = pomodoroSession
        self.task_count = 0
        self.task_long_break_goal = 4

        # define task length
        self.task_length = datetime.timedelta(minutes=timerLength)

        # define break periods
        self.break_time_short = datetime.timedelta(minutes=3)
        self.break_time_long = datetime.timedelta(minutes=15)

        # initialize timer
        self.timer_set = self.NO_TIMER

    def start_session_pomodoro(self):

        # define start variable
        self.timer_start = datetime.datetime.now()
        self.timer_end = self.timer_start + self.task_length
        self.timer_set = self.TASK_TIMER

        print("Pomodoro Has Started \n")

    def end_session_pomodoro(self):
        self.task_count += 1

    def end_task(self):
        return self.task_count == self.task_goal

    def start_long_break(self):

        # define start variable
        self.timer_start = datetime.datetime.now()
        self.timer_end = self.timer_start + self.break_time_long
        self.timer_set = self.LONG_BREAK_TIMER

        print("Long Break Period Has Started \n")

    def start_short_break(self):
        # define start variable
        self.timer_start = datetime.datetime.now()
        self.timer_end = self.timer_start + self.break_time_short
        self.timer_set = self.SHORT_BREAK_TIMER

        print("Short Break Period Has Started \n")

    def get_time_remaining(self):
        return self.timer_end - datetime.datetime.now()

    def time_counter(self, timeDelta):

        seconds = int(timeDelta.total_seconds())
        hours, remainder = divmod(seconds, 3600)
        minutes, seconds = divmod(remainder, 60)

        return "{} : {}".format(minutes, seconds)

    def print_summary(self):
        task_name = "none"

        # format timer output
        if self.timer_set == self.TASK_TIMER:
            task_name = "task"
        elif self.timer_set == self.SHORT_BREAK_TIMER:
            task_name = "short break"
        elif self.timer_set == self.LONG_BREAK_TIMER:
            task_name = "long break"

        # format time remaining output
        time_remaining = self.time_counter(self.get_time_remaining())

        print("{} | Remaining : {}".format(task_name, time_remaining))
