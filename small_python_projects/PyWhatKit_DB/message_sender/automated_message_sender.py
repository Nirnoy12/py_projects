import pywhatkit as pw

# Take input and prepend +91
no = input("Enter a 10-digit Indian number: ")
num = "+91" + no  # This stays a string (no int conversion needed)

# Message input
msg = input("Enter the message you want to send: ")

# Time input
hr, min = map(int, input("At what hour and at what minute do you want to send the message (hh mm): ").split())

# Send WhatsApp message
pw.sendwhatmsg(num, msg, hr, min, 40)
