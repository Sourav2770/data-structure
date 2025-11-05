class Time:
    def __init__(self, hours=0, minutes=0, seconds=0):
    
        self.__hours = hours
        self.__minutes = minutes
        self.__seconds = seconds
        self.__normalize_time()

    
    def __normalize_time(self):
        if self.__seconds >= 60:
            self.__minutes += self.__seconds // 60
            self.__seconds %= 60
        if self.__minutes >= 60:
            self.__hours += self.__minutes // 60
            self.__minutes %= 60
        if self.__hours >= 24:
            self.__hours %= 24

    def display_time(self):
        print(f"{self.__hours:02d}:{self.__minutes:02d}:{self.__seconds:02d}")

    
    def add_time(self, *args):
        """
        Overloading behavior:
        - add_time(Time_object)
        - add_time(hours, minutes, seconds)
        """
        if len(args) == 1 and isinstance(args[0], Time):
        
            other = args[0]
            self.__hours += other.__hours
            self.__minutes += other.__minutes
            self.__seconds += other.__seconds
        elif len(args) == 3:
        
            h, m, s = args
            self.__hours += h
            self.__minutes += m
            self.__seconds += s
        else:
            print("Invalid arguments! Use add_time(Time) or add_time(h, m, s).")

        self.__normalize_time()


    def get_time(self):
        return self.__hours, self.__minutes, self.__seconds



t1 = Time(2, 45, 50)
t2 = Time(1, 30, 20)

print("Initial Time 1:")
t1.display_time()
print("Initial Time 2:")
t2.display_time()


print("\nAdding t2 to t1:")
t1.add_time(t2)
t1.display_time()

print("\nAdding 2 hours, 40 minutes, and 50 seconds to t1:")
t1.add_time(2, 40, 50)
t1.display_time()
