import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.image import MIMEImage
from email.mime.text import MIMEText
from email import encoders
from dotenv import load_dotenv

load_dotenv()

def load_credentials():
   """Load email credentials from environment variables."""
   
   sender_email = str(os.getenv("EMAIL"))
   password = str(os.getenv("PASS"))
   return sender_email, password


def create_email_message(sender_email, recipients, subject):
   """Create the basic email message structure."""

   message = MIMEMultipart("related")
   message["From"] = sender_email
   message["To"] = ", ".join(recipients)
   message["Subject"] = subject
   return message


def create_email_body(plain_text, html_content):
   """Create email body with both plain text and HTML versions."""

   alt = MIMEMultipart("alternative")
   alt.attach(MIMEText(plain_text, "plain"))
   alt.attach(MIMEText(html_content, "html"))
   return alt


def attach_inline_image(message, image_path):
   """Attach an inline image to the email."""

   if os.path.exists(image_path):
      with open(image_path, "rb") as img:
         img_data = img.read()
      image = MIMEImage(img_data)
      image.add_header("Content-ID", "<inline_image>")
      image.add_header("Content-Disposition", "inline", filename=os.path.basename(image_path))
      message.attach(image)
      print(f"Inline image attached: {image_path}")
   else:
      print(f"Image not found: {image_path}")


def attach_file(message, filepath):
   """Attach a file to the email."""

   if os.path.exists(filepath):
      filename = os.path.basename(filepath)
      with open(filepath, "rb") as attachment:
         part = MIMEBase("application", "octet-stream")
         part.set_payload(attachment.read())
      encoders.encode_base64(part)
      part.add_header("Content-Disposition", f"attachment; filename={filename}")
      message.attach(part)
      print(f"File attached: {filename}")
   else:
      print(f"File not found: {filepath}")


def send_email(sender_email, password, recipients, message):
   """Send the email using SMTP."""

   try:
      server = smtplib.SMTP("smtp.gmail.com", 587)
      server.starttls()
      server.login(sender_email, password)
      server.sendmail(sender_email, recipients, message.as_string())
      server.quit()
      
      print("Email sent successfully!")
   except Exception as e:
      print(f"Error while sending email: {e}")


def main():
   """Main function to orchestrate email sending."""
   
   sender_email, password = load_credentials()
   
   recipients = ["jm.mahival@gmail.com", "jayneel.mmahival@gmail.com"]
   subject = "Multipart Email with Inline Image & Attachment"
   
   plain_text = input("Enter plain text: ")
   html_content = """
   <html>
   <body>
      <p>Hello,</p>
      <p>This is an <b>HTML version</b> of the email.</p>
      <p>Here's an inline image below:</p>
      <img src="cid:inline_image">
   </body>
   </html>
   """
   
   message = create_email_message(sender_email, recipients, subject)
   
   body = create_email_body(plain_text, html_content)
   message.attach(body)
   
   image_path = "./Main/IA2_assignment/2_image.png"
   attach_inline_image(message, image_path)
   
   filepath = "./Main/IA2_assignment/2_pdf.pdf"
   attach_file(message, filepath)
   
   send_email(sender_email, password, recipients, message)


if __name__ == "__main__":
   main()