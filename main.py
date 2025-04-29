import datetime as dt
import pandas
import random
import smtplib
current_dt=dt.datetime.now()
tdy_month=current_dt.month
tdy_day=current_dt.day
tdy_year=current_dt.year
current_m_d=(tdy_month,tdy_day)

birth=pandas.read_csv("birthdays.csv")

#######O/P#########
'''     name                       email  year  month  day
0  YOOHOO  testingpythonyah@yahoo.com  1888      4   29
1    Neha         itsnehakv@gmail.com  2005     11   17
2     GOO  testingpythongoo@gmail.com  1961      4   29
3   Mumma      nishipadman3@gmail.com  1971      5    3'''
##################


month_day_dict=birth.to_dict(orient="records")

######O/P########
'''[{'name': 'ignore', 'email': nan, 'year': nan, 'month': nan, 'day': nan},
 {'name': 'YOOHOO', 'email': 'testingpythonyah@yahoo.com', 'year': 1888.0, 'month': 4.0, 'day': 29.0},
 {'name': 'Neha', 'email': 'itsnehakv@gmail.com', 'year': 2005.0, 'month': 11.0, 'day': 17.0},
 {'name': 'GOO', 'email': 'testingpythongoo@gmail.com', 'year': 1961.0, 'month': 4.0, 'day': 29.0},
 {'name': 'Mumma', 'email': 'nishipadman3@gmail.com', 'year': 1971.0, 'month': 5.0, 'day': 3.0}]'''
#################

#************old solution************
# month_day_dict={(row.month,row.day):row for (index,row) in birth.iterrows()}
# this does not work in case two ppl have same birthdays, won't work, the keys of the dictionary doesn't accept duplicate keys.
#######O/P########
'''{(4, 29): name                            GOO
email    testingpythongoo@gmail.com
year                           1961
month                             4
day                              29
Name: 2, dtype: object, (11, 17): name                    Neha
email    itsnehakv@gmail.com
year                    2005
month                     11
day                       17
Name: 1, dtype: object, (5, 3): name                      Mumma
email    nishipadman3@gmail.com
year                       1971
month                         5
day                           3
Name: 3, dtype: object}
'''
################

for bday in month_day_dict:
    if (bday["month"],(bday["day"]))==current_m_d:
        birthday_name =bday["name"]
        birthday_email =bday["email"]
        birthday_year = bday["year"]
        letter_no=random.randint(1,3)
        with open(f"letter_templates/letter_{letter_no}.txt") as letter:
            content=letter.read()
            content=content.replace("[NAME]",birthday_name)
            content=content.replace("[AGE]",str(int(tdy_year-birthday_year)))


        email = "testingpythongoo@gmail.com"
        password = "cvnrjemfwloqsyec"
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=email,password=password)
            connection.sendmail(from_addr=email,
                                to_addrs=birthday_email,
                                msg=f"Subject:Happy Birthday!\n\n{content}")



