import smtplib 
  
# creates SMTP session 
s = smtplib.SMTP('smtp.gmail.com', 587) 
  
# start TLS for security 
s.starttls() 
  
# Authentication 
s.login("lakshmisow14@gmail.com", "password") 
  
# message to be sent 
message = "Welcome to python lab"
  
# sending the mail 
s.sendmail("sowbhagyalakshmisow@gmail.com", "lakshmisow14@gmail.com", message)
print("s")
  
# terminating the session 
s.quit() 
