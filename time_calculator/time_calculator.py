week = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']


def add_time(*params):
    try:
        start_time, duration_time, day = params
        end_time, carry = count_time(start_time, duration_time)
        weekday = week[(week.index(day.lower())+carry) % 7]
        end_time += ', ' + weekday.capitalize()
    except:
        start_time, duration_time = params
        end_time, carry = count_time(start_time, duration_time)

    if carry == 1:
        end_time += ' (next day)'
    if carry > 1:
        end_time += f' ({carry} days later)'

    return end_time.replace('0:', '12:')


def count_time(start, duration):
    times, during = start.split(' ')
    start_hour, start_min = map(int, times.split(':'))
    dur_hour, dur_min = map(int, duration.split(':'))

    if during == 'PM':
        start_hour += 12
    add_min = start_min + dur_min
    end_min = add_min % 60
    end_min = '0' + str(end_min) if end_min < 10 else end_min
    carry_hour = add_min // 60
    add_hour = start_hour + dur_hour + carry_hour
    end_hour = add_hour % 24
    carry_day = add_hour // 24
    end_time = f'{end_hour-12}:{end_min} PM' if end_hour > 11 else f'{end_hour}:{end_min} AM'

    return end_time, carry_day


if __name__ == '__main__':
    print(add_time("8:16 PM", "466:02", "tuesday"))
