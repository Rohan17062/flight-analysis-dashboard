import mysql.connector
class DB:
    def __init__(self):
        try:
           self.conn=mysql.connector.connect(
            host='127.0.0.1',
            user='root',
            password='',
            database='mad'
           )
           self.mycursor=self.conn.cursor()
        except:
            print('connection error')

    def extract_city_name(self):
        L=[]
        self.mycursor.execute("""
        select distinct(Source) from mad.flights_cleaned
        union
        select distinct(Destination) from mad.flights_cleaned
        """)
        data=self.mycursor.fetchall()
        for i in data:
            L.append(i[0])
        return L

    def extract_date(self):
        L=[]
        self.mycursor.execute("""
        select distinct(Date_of_Journey) from mad.flights_cleaned
        """)
        data=self.mycursor.fetchall()
        for i in data:
            L.append(i[0])
        return L

    def extract_flight_details(self,source,destination,date):
        self.mycursor.execute("""
        select Airline,Date_of_Journey,Source,Destination,
         Route,Price from mad.flights_cleaned
        where Source=%s and Destination=%s and
        Date_of_Journey=%s
        """,(source,destination,date))
        data=self.mycursor.fetchall()
        return data

    def extract_pie_details(self):
        name=[]
        frequency=[]
        self.mycursor.execute("""
        select Airline,count(*) from mad.flights_cleaned
        group by Airline
        """)
        data=self.mycursor.fetchall()
        for i in data:
            name.append(i[0])
            frequency.append(i[1])
        return name,frequency

    def extract_busy_details(self):
        source=[]
        frequency1=[]
        self.mycursor.execute("""
        select Source,count(*) from (select Source from mad.flights_cleaned
         union all
        select Destination from mad.flights_cleaned) t1
         group by t1.Source
         order by count(*) desc
        """)
        data=self.mycursor.fetchall()
        for i in data:
            source.append(i[0])
            frequency1.append(i[1])
        return source,frequency1

    def expense(self):
        name=[]
        price=[]
        self.mycursor.execute("""
        SELECT Airline,avg(Price) as price FROM mad.flights_cleaned
        group by Airline
        having count(*)>15
        order by avg(Price) desc
        """)
        data = self.mycursor.fetchall()
        for i in data:
            name.append(i[0])
            price.append(i[1])
        return name,price







