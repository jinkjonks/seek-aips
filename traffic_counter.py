import logging
from datetime import datetime, timedelta
from heapq import heappush, heappop

# Magic numbers for the traffic counter according to specs
NO_PERIODS = 3  # n * 30 minutes
TOP_N = 3  # number of top entries to show
PERIOD_LENGTH = 30  # minutes


class TrafficEntry:
    """
    Class for storing entries
    """

    def __init__(self, time: datetime, cars: int):
        self.time = time
        self.cars = cars

    def print(self):
        """
        Get string representation of entry    
        """
        time_string = self.time.strftime("%Y-%m-%dT%H:%M:%S")
        return(f"{time_string} {self.cars}")


class TrafficCounter:
    """
    Class for reading and interpreting Traffic
    """

    def __init__(self):
        self.db = []  # array of Entry objecs
        self.__length = 0  # number of entries in db
        self.__total_cars = 0  # total number of cars
        self.__date_index = {}  # dictionary of dates and their index in db

    def read_file(self, txt: str):
        logging.debug('Reading file')
        curr_date = None
        for line in txt.split('\n'):
            logging.debug(f'Processing line: {line}')
            timestamp, cars = line.split()
            time = datetime.strptime(timestamp, "%Y-%m-%dT%H:%M:%S")
            date = datetime.date(time)

            if curr_date != date:
                self.__date_index[date] = self.__length
                curr_date = date
            new_entry = TrafficEntry(time, int(cars))
            self.db.append(new_entry)
            self.__total_cars += int(cars)
            self.__length += 1

    def get_total_cars(self) -> int:
        """
        Returns total number of cars
        """
        return self.__total_cars

    def get_totals_by_dates(self, dates: str) -> str:
        totals = []
        days = []
        for line in dates.split('\n'):
            curr_date = datetime.strptime(line, "%Y-%m-%d").date()
            logging.debug("Processing date: " + str(curr_date))
            days.append(line)
            day_total = 0
            if curr_date in self.__date_index:
                i = self.__date_index[curr_date]
                while i < self.__length and self.db[i].time.date() == curr_date:
                    day_total += self.db[i].cars
                    i += 1

            totals.append(day_total)

        printout = []
        for i in range(len(days)):
            printout.append(f"{days[i]} {totals[i]}")
        return '\n'.join(printout)

    def get_most_cars(self) -> str:
        """
        Get most cars for specified number of periods. 
        Yes, the binary min heap is overkill for only top 3 entries 
        """
        if self.__length == 0:
            return None

        min_heap = [0]  # heap of indices for periods containing the most cars
        for i in range(self.__length):
            if self.db[i].cars > self.db[min_heap[0]].cars:
                if len(min_heap) >= TOP_N:
                    heappop(min_heap)

                heappush(min_heap, i)

        printout = []
        for i in min_heap:
            printout.append(self.db[i].print())
        return '\n'.join(printout)

    def get_least_cars(self) -> str:
        """
        Finds contiguous periods where the number of cars is the least
        If there are none, -1 is returned 
        Otherwise list of timestamps are returned 
        Multiple timestamps are returned in case of ties
        """
        idx = []  # array of indices of timestamps to return (if any)
        min_total = None  # minimum number of cars in period
        curr_arr = [0]  # array of indices
        i = 1  # index of current element in self.db

        while i < self.__length - NO_PERIODS + 1:
            if self.db[i-1].time + timedelta(minutes=PERIOD_LENGTH) == self.db[i].time:
                curr_arr.append(i)
            else:
                curr_arr = [i]
            i += 1

            if len(curr_arr) > NO_PERIODS:
                curr_arr.pop(0)
            if len(curr_arr) == NO_PERIODS:
                curr_sum = sum([self.db[j].cars for j in curr_arr])
                if min_total is None or min_total > curr_sum:
                    idx = [curr_arr[0]]
                    min_total = curr_sum
                elif min_total == curr_sum:
                    idx.append(curr_arr[0])

        if min_total is None:
            return -1
        
        return '\n'.join([self.db[j].time.strftime("%Y-%m-%dT%H:%M:%S") for j in idx])
        
