# importing the module
import pywhatkit

# phone number
phone_no = input("Enter phone number: ")

# Group whatsapp
group_wa = input("Enter Group whatsapp: ")

# Send a WhatsApp Message to a Contact at 1:30 PM
pywhatkit.sendwhatmsg(phone_no, "Hi", 13, 30)

# to Close the Tab in 2 Seconds after Sending the Message
pywhatkit.sendwhatmsg(phone_no, "Hi", 13, 30, 15, True, 2)

# Send an Image to a Group with the Caption as Hello
pywhatkit.sendwhats_image(phone_no, "Images/Hello.png", "Hello")

# Send an Image to a Contact with the no Caption
pywhatkit.sendwhats_image(phone_no, "Images/Hello.png")

# Send a WhatsApp Message to a Group at 12:00 AM
pywhatkit.sendwhatmsg_to_group(group_wa, "Hey All!", 0, 0)

# Send a WhatsApp Message to a Group instantly
pywhatkit.sendwhatmsg_to_group_instantly(group_wa, "Hey All!")

# Plays Lovely by billie ellish on youtube
pywhatkit.playonyt("lovely by billie")
