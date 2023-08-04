
# import os
# path = "C:/Users/HP/Music/filedestination2/"
# # Check whether the specified path exists or not
# isExist = os.path.exists(path)
# #printing if the path exists or not
# print(isExist)

# ----------------------------COMPLETE--------------------------------------------
#python program to check if a directory exists
import os
import datetime

from datetime import date

d = date.today()

# today = datetime.now()


print (d)

path = ("C:/Users/HP/Music/filedestination/BackUp/" + d.strftime('%d%m%Y'))
# Check whether the specified path exists or not
isExist = os.path.exists(path)
if not isExist:

   # Create a new directory because it does not exist
   os.makedirs(path)
   print("The new directory is created!")
   print(path)



# from datetime import date

# # d = date.fromordinal(730920)

# d = date.today()

# # d.isoformat()

# # d.strftime("%d/%m/%Y")

# print (d)
