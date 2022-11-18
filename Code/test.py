from DataBase import database
import pywhatkit
import datetime

# Show data from database
database.showAll()

# Show phone number from database
num = str(database.showPhno('xyz'))
msg = "Hello...!"
t = datetime.datetime.now()
pywhatkit.sendwhatmsg("+91"+num, msg, int(t.strftime('%H')), int(t.strftime('%M'))+1)


# print(type(num))
# print("Hours: "+t.strftime('%H'))
# print(int(t.strftime('%M'))+1)
# print(type(t.strftime('%M')))