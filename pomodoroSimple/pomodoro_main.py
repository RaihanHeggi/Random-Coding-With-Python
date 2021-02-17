import pomodoro as P
import datetime


def main():

    timerLength = int(input("How Long Pomodoro Time You Want ? \n"))
    session = int(input("How Many Session Do You Want ? \n"))
    pomodoro = P.Pomodoro(timerLength, session)
    pomodoro.start_session_pomodoro()

    while True:
        last_summary = pomodoro.timer_start - datetime.timedelta(seconds=15)
        while pomodoro.get_time_remaining() > datetime.timedelta(seconds=0):
            current = datetime.datetime.now()

            if (current - last_summary) > datetime.timedelta(seconds=15):
                pomodoro.print_summary()
                last_summary = current

        if pomodoro.timer_set == pomodoro.TASK_TIMER:
            pomodoro.end_session_pomodoro()
            if pomodoro.end_task():
                break
            elif pomodoro.task_count % pomodoro.task_long_break_goal == 0:
                pomodoro.start_long_break()
            else:
                pomodoro.start_short_break
        else:
            pomodoro.start_session_pomodoro()

    print("\n End Of Pomodoro Session")


if __name__ == "__main__":
    main()
