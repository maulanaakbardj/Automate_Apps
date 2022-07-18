
# importing the module
import pywhatkit

# phone number
phone_no = input("Enter phone number: ")

# using Exception Handling to avoid
# unprecedented errors
try:
   
  # sending message to receiver
  # using pywhatkit
  pywhatkit.sendwhatmsg(phone_no,
                        "Hello from Maul Center",
                        22, 28)
  print("Successfully Sent!")
 
except:
   
  # handling exception
  # and printing error message
  print("An Unexpected Error!")
