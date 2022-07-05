from traffic_counter import TrafficCounter

txt = '''2021-12-01T05:00:00 5
2021-12-01T05:30:00 12
2021-12-01T06:00:00 14
2021-12-01T06:30:00 15
2021-12-01T07:00:00 25
2021-12-01T07:30:00 46
2021-12-01T08:00:00 42
2021-12-01T15:00:00 9
2021-12-01T15:30:00 11
2021-12-01T23:30:00 0
2021-12-05T09:30:00 18
2021-12-05T10:30:00 15
2021-12-05T11:30:00 7
2021-12-05T12:30:00 6
2021-12-05T13:30:00 9
2021-12-05T14:30:00 11
2021-12-05T15:30:00 15
2021-12-08T18:00:00 33
2021-12-08T19:00:00 28
2021-12-08T20:00:00 25
2021-12-08T21:00:00 21
2021-12-08T22:00:00 16
2021-12-08T23:00:00 11
2021-12-09T00:00:00 4'''

traffic_counter = TrafficCounter()
traffic_counter.read_file(txt)

total_cars = traffic_counter.get_total_cars()
print(f"There are {total_cars} total cars.")

total_cars_in_dates = traffic_counter.get_totals_by_dates(
    "2021-12-01\n2021-12-09")
print(f"Totals by specified dates")
print(total_cars_in_dates)

max_cars = traffic_counter.get_most_cars()
print(f"The most cars were at:")
print(max_cars)

periods= traffic_counter.get_least_cars()
print(f"The least cars were during the period/s starting at:")
print(periods)
