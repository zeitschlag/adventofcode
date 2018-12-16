import re
import datetime

class Guard:
    def __init__(self):
        self.sleep_phases = list()

    def get_number_of_most_sleepy_minute(self):
        sleepy_minutes = dict()
        # count minutes
        for sleep_phase in self.sleep_phases:
            for sleepy_minute in sleep_phase.sleepy_minutes():
                if sleepy_minute.minute in sleepy_minutes:
                    sleepy_minutes[sleepy_minute.minute] += 1
                else:
                    sleepy_minutes[sleepy_minute.minute] = 1

        # find most sleepy minute
        amount_of_most_sleepy_minute = 0
        for sleepy_minute in sleepy_minutes:
            if sleepy_minutes[sleepy_minute] > amount_of_most_sleepy_minute :
                amount_of_most_sleepy_minute = sleepy_minutes[sleepy_minute]

        return amount_of_most_sleepy_minute

    def find_most_sleepy_minute(self):
        sleepy_minutes = dict()
        # count minutes
        for sleep_phase in self.sleep_phases:
            for sleepy_minute in sleep_phase.sleepy_minutes():
                if sleepy_minute.minute in sleepy_minutes:
                    sleepy_minutes[sleepy_minute.minute] += 1
                else:
                    sleepy_minutes[sleepy_minute.minute] = 1

        # find most sleepy minute
        most_sleepy_minute = 0
        threshold = 0
        for sleepy_minute in sleepy_minutes:
            if sleepy_minutes[sleepy_minute] > threshold:
                most_sleepy_minute = sleepy_minute
                threshold = sleepy_minutes[sleepy_minute]

        return most_sleepy_minute


class SleepPhase:

    def __init__(self, start, end):
        self.start = start
        self.end = end

    def sleepy_minutes(self):
        # iterate from self.start to self.end and add the minute-part
        minutes = list()
        delta = datetime.timedelta(minutes=1)

        tmpDate = self.start
        while tmpDate < self.end:
            minutes.append(tmpDate)
            tmpDate += delta
        return minutes

    def duration_in_minutes(self):
        return len(self.sleepy_minutes())


class Event:
    def __init__(self, line):
        pattern = "^\[(.+?)-(.+?)-(.+?) (.+?):(.+?)\] (.+)$"
        result = re.search(pattern, line)

        year = int(result.group(1))
        month = int(result.group(2))
        day = int(result.group(3))
        hour = int(result.group(4))
        minute = int(result.group(5))

        self.datetime = datetime.datetime(year=year, month=month, day=day, hour=hour, minute=minute)

        self.event_string = result.group(6)

    def get_guard(self):
        pattern = "^Guard #(.+?) begins shift$"
        result = re.search(pattern=pattern, string=self.event_string)

        if result:
            guard = Guard()
            guard.guard_id = result.group(1)
            return guard

        return None

    def get_sleep_time(self):
        pattern = "falls asleep"
        result = re.search(pattern=pattern, string=self.event_string)

        if result:
            return self.datetime

        return None

    def get_wakeup_time(self):
        pattern = "wakes up"
        result = re.search(pattern=pattern, string=self.event_string)

        if result:
            return self.datetime

        return None

    def __str__(self):
        return "[%s] %s" % (self.datetime, self.event_string)


class FourthDay:

    def first_part(self, input_file_path):
        lines = open(input_file_path, "r").read().split("\n")
        all_events = list()
        all_guards = dict()

        # read input
        for line in lines:
            event = Event(line=line)
            all_events.append(event)

        # order input
        sorted_events = sorted(all_events, key=lambda event: event.datetime, reverse=False)

        current_asleep_datetime = None
        current_guard = None
        for event in sorted_events:
            changed_guard = event.get_guard()

            if changed_guard is not None:
                if changed_guard.guard_id in all_guards:
                    changed_guard = all_guards[changed_guard.guard_id]
                else:
                    all_guards[changed_guard.guard_id] = changed_guard

                current_guard = changed_guard

            # all sleep phases are identical

            if current_guard is not None:
                sleep_time = event.get_sleep_time()
                if sleep_time is not None:
                    current_asleep_datetime = sleep_time

                wakeup_time = event.get_wakeup_time()
                if wakeup_time is not None:
                    sleep_phase = SleepPhase(start=current_asleep_datetime, end=wakeup_time)

                    if current_guard.sleep_phases is None:
                        current_guard.sleep_phases = list()

                    current_guard.sleep_phases.append(sleep_phase)
                    current_asleep_datetime = None

        most_sleepy_guard = self.find_most_sleepy_guard(all_guards)
        # find most sleepy minute for this guard
        most_sleepy_minute = most_sleepy_guard.find_most_sleepy_minute()
        # multiply guard-id with their most sleepy minute

        print("Result for first puzzle of fourth day: %s * %s = %s" % (most_sleepy_guard.guard_id, most_sleepy_minute, int(most_sleepy_guard.guard_id) * int(most_sleepy_minute)))

    def second_part(self, input_file_path):
        # Of all guards, which guard is most frequently asleep on the same minute?
        lines = open(input_file_path, "r").read().split("\n")
        all_events = list()
        all_guards = dict()

        # read input
        for line in lines:
            event = Event(line=line)
            all_events.append(event)

        # order input
        sorted_events = sorted(all_events, key=lambda event: event.datetime, reverse=False)

        current_asleep_datetime = None
        current_guard = None
        for event in sorted_events:
            changed_guard = event.get_guard()

            if changed_guard is not None:
                if changed_guard.guard_id in all_guards:
                    changed_guard = all_guards[changed_guard.guard_id]
                else:
                    all_guards[changed_guard.guard_id] = changed_guard

                current_guard = changed_guard

            if current_guard is not None:
                sleep_time = event.get_sleep_time()
                if sleep_time is not None:
                    current_asleep_datetime = sleep_time

                wakeup_time = event.get_wakeup_time()
                if wakeup_time is not None:
                    sleep_phase = SleepPhase(start=current_asleep_datetime, end=wakeup_time)

                    if current_guard.sleep_phases is None:
                        current_guard.sleep_phases = list()

                    current_guard.sleep_phases.append(sleep_phase)
                    current_asleep_datetime = None

        most_sleepy_guard = None
        most_sleepy_minute = 0
        number_of_most_sleepy_minute = 0
        for guard_id in all_guards:
            guard = all_guards[guard_id]

            current_sleepy_minute = guard.find_most_sleepy_minute()
            number_of_sleepy_minute = guard.get_number_of_most_sleepy_minute()

            print("Guard #%s: sleeps most often at %s, %s times" % (guard.guard_id, current_sleepy_minute, number_of_sleepy_minute))

            if number_of_sleepy_minute > number_of_most_sleepy_minute:
                number_of_most_sleepy_minute = number_of_sleepy_minute
                most_sleepy_minute = current_sleepy_minute
                most_sleepy_guard = guard

        print("Result for second puzzle of fourth day: %s * %s = %s" % (most_sleepy_guard.guard_id, most_sleepy_minute, int(most_sleepy_guard.guard_id) * int(most_sleepy_minute)))

    def find_most_sleepy_guard(self, all_guards):

        most_sleepy_guard = None
        max_sleep = 0

        for guard_id in all_guards:
            guard = all_guards[guard_id]

            total_sleep = 0 # minutes
            for sleep_phase in guard.sleep_phases:
                total_sleep += sleep_phase.duration_in_minutes()

            if total_sleep >= max_sleep:
                max_sleep = total_sleep
                most_sleepy_guard = guard

        return most_sleepy_guard;


if __name__ == "__main__":
    fourth_day = FourthDay()
    fourth_day.first_part("input.txt")
    fourth_day.second_part("input.txt")