from datetime import datetime

list_of_birthday_dates = [
    {"Name": "Nik", "Birthday": datetime(2000, 7, 7)},
    {"Name": "Bob", "Birthday": "4.07.2000"},
    {"Name": "Billi", "Birthday": datetime(2001, 7, 1)},
    {"Name": "Sem", "Birthday": "2.07.1998"},
    {"Name": "Filip", "Birthday": datetime(1996, 7, 8)},
    {"Name": "Kristi", "Birthday": "29.06.2002"},
    {"Name": "Olga", "Birthday": "1.07.1998"},
    {"Name": "Natali", "Birthday": "01.06.1988"},
    {"Name": "Tatyana", "Birthday": "30.06.2000"},
    {"Name": "Tom", "Birthday": "5.06.2000"},
]

# Визначае скільки днів лишилося до дня народження, з урахуванням 29-го 02-го та кінця року.
def diff_BD(data: datetime,):
    
    day_now = datetime.now()
    bd_month = data.month
    bd_day = data.day
    if (bd_month == 2) and (bd_day == 29):
        day_now = datetime(data.year, day_now.month, day_now.day)
    difference_day = (datetime(day_now.year, bd_month, bd_day) - day_now).days
    if difference_day < 0:
        difference_day = (datetime(day_now.year, bd_month, bd_day) - day_now).days + 365
    return difference_day

# Проходить усіх сотрудників,форматуе строки до таймдата.
def birthday_reader(employees_list: list,):

    print_list = [[], [], [], [], []]
    wek_day_UA_list = [ "Понеділок: ","Вівторок: ","Середа: ", "Четверг: ","П'ятниця: ",]

    for i in range(len(employees_list)):
        data = employees_list[i].get("Birthday")
        if type(data) == datetime:
            data = data.date()
        if type(data) == str:
            data = datetime.strptime(data, "%d.%m.%Y")
            data = data.date()
        # Викликаємо функцію яка залежно від дня виклику вирішує чи треба поздоровити.
        if return_WD(diff_BD(data)):
            wd = datetime(datetime.now().year, data.month, data.day).weekday()
            # Якщо день припав на вихідні то записуем на понеділок
            if wd > 4:
                print_list[0].append(employees_list[i].get("Name"))
            else:
                print_list[wd].append(employees_list[i].get("Name"))
    
    for i in range(5):
        if len(print_list[i]) > 0:
            print(wek_day_UA_list[i], ", ".join(print_list[i]))

# Вибирає тих у кого день народження з суботи цього тиждня та до п'ятниці включно наступного.
def return_WD(rest_days,):
    now = datetime.now()
    day_week = now.weekday()
    min_rest_days = 4 - day_week
    max_rest_days = 4 - day_week + 6
    if min_rest_days <= rest_days <= max_rest_days:
        return True
    else:
        return False


birthday_reader(list_of_birthday_dates)
