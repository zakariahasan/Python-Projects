import os
import smtplib
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart


def message(to=None,subject=None, text=None, img=None, attachment=None):
    # build message contents
    msg = MIMEMultipart()
    msg['Subject'] = subject  # add in the subject
    msg.attach(MIMEText(text))  # add text contents
    if type(to) is not list:
        msg["To"] = to
    
    # initialize an empty string 
    str1 = ""  
    
    # traverse in the string   
    for ele in to:  
        str1 += ele+','   
    
    # return string   
    msg["To"] = str1  

    # check if we have anything given in the img parameter
    if img is not None:
        # if we do, we want to iterate through the images, so let's check that
        # what we have is actually a list
        if type(img) is not list:
            img = [img]  # if it isn't a list, make it one
        # now iterate through list
        for one_img in img:
            img_data = open(one_img, 'rb').read()  # read the image binary data
            # attach the image data to MIMEMultipart using MIMEImage, we add
            # the given filename use os.basename
            msg.attach(MIMEImage(img_data, name=os.path.basename(one_img)))

    # do the same for attachments as we did for images
    if attachment is not None:
        if type(attachment) is not list:
            attachment = [attachment]  # if it isn't a list, make it one
            
        for one_attachment in attachment:
            with open(one_attachment, 'rb') as f:
                # read in the attachment using MIMEApplication
                file = MIMEApplication(
                    f.read(),
                    name=os.path.basename(one_attachment)
                )
            # here we edit the attached file metadata
            file['Content-Disposition'] = f'attachment; filename="{os.path.basename(one_attachment)}"'
            msg.attach(file)  # finally, add the attachment to message object
    return msg




mail_user=os.getenv('mail_user_2')
mail_pass=os.getenv('mail_pass_2')



From = mail_user
To = ['kanon@gmail.com','kanon.bumblebee1@gmail.com']
Subject = 'Hello Kanon'
Text = 'How you doing'
img = ['product_2.jpg','5FDD9C8F.jpg']
attachment ='product_2.jpg' 



# initialize connection to  email server
smtp = smtplib.SMTP('smtp.gmail.com', port='587')

# send the extended hello to the server
#smtp.ehlo()

# tell server to communicate with TLS encryption
smtp.starttls()  

# login to the email server
smtp.login(mail_user, mail_pass)

smtp.sendmail(From,To, message(To,Subject,Text,img,attachment).as_string())


# For mail Bomber
#for i in range(2):
    #smtp.sendmail(From,To, message(To,Subject,Text,img,attachment).as_string())

smtp.quit()  

