import time
import random
import logging
import smtplib
import os
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from dotenv import load_dotenv

load_dotenv()

logging.basicConfig(
   filename="flight.log",
   level=logging.INFO,
   format="%(asctime)s - %(levelname)s - %(message)s",
   filemode="w",
)


def send_email(subject, body, to_email):
   from_email = os.getenv('EMAIL')
   from_password = os.getenv('PASS')
   smtp_server = "smtp.gmail.com"
   smtp_port = 587

   if not from_email or not from_password:
      logging.error("Email credentials not found in environment variables. Please set EMAIL and PASS.")
      print("Email credentials not configured. Cannot send crash notification.")
      return

   try:
      msg = MIMEMultipart()
      msg["From"] = from_email
      msg["To"] = to_email
      msg["Subject"] = subject
      msg.attach(MIMEText(body, "plain"))

      server = smtplib.SMTP(smtp_server, smtp_port)
      server.starttls()
      server.login(from_email, from_password)
      server.sendmail(from_email, to_email, msg.as_string())
      server.quit()

      logging.info(f"Email sent to {to_email} with subject: {subject}")
      print(f"Crash notification email sent to {to_email}")
   except Exception as e:
      logging.error(f"Failed to send email: {e}")
      print(f"Failed to send crash notification email: {e}")


def flight_simulator(source, destination):
   print(f"Flight taking off from {source} to {destination}\n")
   logging.info(f"Flight taking off from {source} to {destination}")

   altitude = 0
   speed = 0
   distance = 500
   covered = 0

   for i in range(3):
      altitude += 1000
      speed += 200
      msg = f"Takeoff step {i+1}: Speed={speed} km/h, Altitude={altitude} ft"
      print(msg)
      logging.info(msg)
      time.sleep(2)

   while covered < distance:
      speed += random.randint(-80, 80)
      altitude += random.randint(-125, 125)
      covered += speed * 0.05

      msg = f"Journey: {covered:.1f} km covered, Speed={speed}, Altitude={altitude}"
      print(msg)
      logging.info(msg)

      if random.random() < 0.3:
         crash_msg = f"MAYDAY MAYDAY:::  CRASHED:::   at {covered:.1f} km!"
         print(f"\n {crash_msg} ")
         logging.critical(crash_msg)

         send_email(
               subject="ALERT: Flight Crash Detected!",
               body=f"The flight from {source} to {destination} has crashed at {covered:.1f} km.\n"
               f"Final Speed: {speed} km/h\n"
               f"Final Altitude: {altitude} ft",
               to_email="23bcp332@sot.pdpu.ac.in",  
         )
         return

      time.sleep(1)

   msg = f"Flight safely landed at {destination}. Final Speed={speed}, Altitude={altitude}"
   print(f"\n{msg}")
   logging.info(msg)


if __name__ == "__main__":
   flight_simulator("Daman", "America")