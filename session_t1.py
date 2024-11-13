from datetime import datetime

# دریافت تاریخ تولد به فرمت YYYY-MM-DD
year = int(input("سال تولد خود را وارد کنید: "))
month = int(input("ماه تولد خود را وارد کنید: "))
day = int(input("روز تولد خود را وارد کنید: "))

# ساخت یک شیء datetime برای تاریخ تولد
birth_date = datetime(year, month, day)

# گرفتن تاریخ امروز
today = datetime.today()

# محاسبه تعداد روزهای گذشته از تاریخ تولد
days_lived = (today - birth_date).days

# نمایش نتیجه
print(f"شما تا امروز {days_lived} روز زندگی کرده‌اید.")