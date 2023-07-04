#24.1
import datetime

date_str = input("Введите дату (ГГГГ-ММ-ДД): ")
date = datetime.datetime.strptime(date_str, "%Y-%m-%d")
week_number = date.isocalendar()[1]
print("Номер недели:", week_number)


#24.2
import datetime

year = 2015
week_number = 50
first_day_of_year = datetime.date(year, 1, 1)
first_monday = first_day_of_year + datetime.timedelta(days=(week_number - 1) * 7 - first_day_of_year.weekday() + 1)

print("Output:", first_monday)


#24.3
import datetime

year = 2023
for month in range(1, 13):
    for day in range(1, 32):
        try:
            date = datetime.date(year, month, day)
            if date.weekday() == 6:
                print(date)
        except ValueError:
            break


#24.4
import datetime

def add_years(date, years):
    new_date = date + datetime.timedelta(days=years * 365)
    return new_date

date1 = datetime.date(2015, 1, 1)
date2 = datetime.date(2015, 1, 1)
date3 = datetime.date(2015, 1, 1)

new_date1 = add_years(date1, -1)
print(new_date1)

new_date2 = add_years(date2, 0)
print(new_date2)

new_date3 = add_years(date3, 2)
print(new_date3)


#25.1
import datetime

time_utc = datetime.datetime.utcnow()
print("Время по Гринвичу (UTC):", time_utc)

time_local = datetime.datetime.now()
print("Местное время:", time_local)


#25.2
import datetime

date1_str = input("Введите первую дату (ГГГГ-ММ-ДД): ")
date1 = datetime.datetime.strptime(date1_str, "%Y-%m-%d")

date2_str = input("Введите вторую дату (ГГГГ-ММ-ДД): ")
date2 = datetime.datetime.strptime(date2_str, "%Y-%m-%d")

delta = date2 - date1
days = delta.days

print("Количество дней:", days)


#25.3
import datetime

date1_str = input("Введите первую дату и время (ГГГГ-ММ-ДД ЧЧ:ММ:СС): ")
date1 = datetime.datetime.strptime(date1_str, "%Y-%m-%d %H:%M:%S")

date2_str = input("Введите вторую дату и время (ГГГГ-ММ-ДД ЧЧ:ММ:СС): ")
date2 = datetime.datetime.strptime(date2_str, "%Y-%m-%d %H:%M:%S")

delta = date2 - date1

days = delta.days
hours, remainder = divmod(delta.seconds, 3600)
minutes, seconds = divmod(remainder, 60)

print("Разница между датами:")
print("Дни:", days)
print("Часы:", hours)
print("Минуты:", minutes)
print("Секунды:", seconds)


#25.4
import calendar

def create_calendar(year, month):
    cal = calendar.HTMLCalendar()
    calendar_html = cal.formatmonth(year, month)
    return calendar_html

year = int(input("Введите год: "))
month = int(input("Введите месяц (число от 1 до 12): "))

calendar_html = create_calendar(year, month)
print(calendar_html)


#26.1
def extract_domains(emails):
    domains = set()
    for email in emails:
        domain = email.split("@")[-1]
        domains.add(domain)
    return domains

email_list = [
    "user1@example.com",
    "user2@test.com",
    "user3@example.com",
    "user4@domain.com",
    "user5@test.com"
]

domain_set = extract_domains(email_list)
print("Список доменов:")
for domain in domain_set:
    print(domain)


#26.2
def extract_vowel_words(text):
    vowels = {'a', 'e', 'i', 'o', 'u'}
    words = text.split()
    vowel_words = []
    for word in words:
        first_letter = word[0].lower()
        if first_letter in vowels:
            vowel_words.append(word)
    return vowel_words

text = "dogs and cats get along well"
vowel_words_list = extract_vowel_words(text)
print("Слова, начинающиеся на гласную букву:")
for word in vowel_words_list:
    print(word)


#26.3
import re

def split_string(text, delimiters):
    pattern = '|'.join(map(re.escape, delimiters))
    substrings = re.split(pattern, text)
    return substrings

text = "Hello,world;how|are/you"
delimiters = [",", ";", "|", "/"]
substrings_list = split_string(text, delimiters)
print("Подстроки:")
for substring in substrings_list:
    print(substring)









