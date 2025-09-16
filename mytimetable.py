from pathlib import Path
file_path = Path("mbcholiday.txt")
content = file_path.read_text(encoding="utf-8")
holiday=[]
for elm in content.split("\n"):
    holiday.append(elm[0:10])
from datetime import datetime, timedelta
times_def=["08:30	17:10","08:30	17:15","08:30	17:10","08:30	17:15","08:30	17:10","08:30	12:30", "08:30	16:00"]
current_date = datetime.now()
current_date = datetime.strptime("2025-09-01", "%Y-%m-%d")
for i in range(332):
    _date = current_date + timedelta(days=i)
    _date_str=_date.strftime('%Y-%m-%d')
    _wday=_date.weekday()
    if _date_str in ["2025-09-01","2025-09-02"] : _wday=6
    if _date.weekday()==6: continue
    if _date_str in holiday: continue
    print(f"{_date.strftime('%Y-%m-%d')}	{times_def[_date.weekday()]}	1")#{_date.weekday()}")

print("""2026-08-25	09:00	16:00	1
2026-08-26	09:00	16:00	1
2026-08-27	09:00	16:00	1
2026-08-28	09:00	16:00	1
2026-08-29	09:00	13:00	1
2026-08-31	09:00	16:00	1""")
