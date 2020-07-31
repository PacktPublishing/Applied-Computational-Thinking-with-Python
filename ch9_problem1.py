#Print initial message for the user
print("This program will take your message and encode it.")

#Ask for the message
msg = input("What message would you like to code? ")

#Ask for shift
shift = int(input("How many places will you shift your message? "))
msgCipher = ""

#Iterate through the letters, adjusting for shift
for letter in msg:
  k = ord(letter)
  if 48 <= k <= 57:
    newk = (k - 48 + shift)%10 + 48
  elif 65 <= k <= 90:
    newk = (k - 65 + shift)%26 + 65
  elif 97 <= k <=122:
    newk = (k - 97 + shift)%26 + 97
  else:
    newk = k
  msgCipher += chr(newk)
print("Your coded message is below.")
print(msgCipher)
