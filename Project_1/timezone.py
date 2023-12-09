from datetime import timedelta, datetime

class TimeZone:
    def __init__(self, name, offset_hours, offset_minutes):
        # name validation
        if not name or len(str(name).strip()) == 0:
            raise ValueError("Name cannot be empty")
        self._name = str(name).strip()
        
        # offset hours validation
        if not isinstance(offset_hours, int):
            raise ValueError("Offset hours must be integer")
        if abs(offset_hours) > 59:
            raise ValueError("Offset hours cannot be greater that 59")
        
        # offset minutes validation
        if not isinstance(offset_minutes, int):
            raise ValueError("Offset minutes must be integer")
        if abs(offset_minutes) > 59:
            raise ValueError("Offset minutes cannot be greater that 59")
        
        # offset must be between -12 hrs and +14 hrs
        offset = timedelta(hours=offset_hours, minutes=offset_minutes)
        if offset < timedelta(hours=-12, minutes=0) or offset > timedelta(hours=14, minutes=0):
            raise ValueError("Offset time must be between -12:00 hrs and +14:00 hrs")
        
        self._offset_hours = offset_hours
        self._offset_minutes = offset_minutes
        self._offset = offset

    # making name read-only property
    @property
    def name(self):
        return self._name
    
    # making offset read-only property
    @property
    def offset(self):
        return self._offset
    
    # will use to check if two objects are equal or not
    def __eq__(self, other):
        return (isinstance(other, TimeZone) and
                self._name == other._name and
                self._offset_hours == other._offset_hours and
                self._offset_minutes == other._offset_minutes)
    
    def __repr__(self) -> str:
        return (f"TimeZone(name='{self._name}'," 
                f"offset_hours={self._offset_hours},"
                f"offset_minutes={self._offset_minutes})")

if __name__ == '__main__':
    obj = TimeZone("abc", 7, 2)
    print(obj) # calls __repr__ method

    current_time_utc = datetime.utcnow()
    print(current_time_utc) # <class 'datetime.datetime'>
    print(current_time_utc + obj.offset)