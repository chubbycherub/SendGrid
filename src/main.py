'''
Created on Dec 5, 2014

@author: Alex
'''

import sendgrid
import message
from sendgrid import SendGridClientError, SendGridServerError
from urllib2 import URLError



class Tests:
    # MAKE A SECURE CONNECTION TO SENDGRID
    # Fill in the variables below with your SendGrid 
    # username and password.
    #========================================================#
    
    
    # CREATE THE SENDGRID MAIL OBJECT
    #========================================================#
    
    #message = sendgrid.Mail()
    
    def __init__(self):
        self.sg_username = "hoanga"
        self.sg_password = "emails4ever"
        
        self.from_address = "alex.hoang.d@gmail.com"
        self.to_address = "alexhoangd@yahoo.com"
        
        self.sg = sendgrid.SendGridClient(self.sg_username, self.sg_password, raise_errors=True)
        #self.sg = sendgrid.SendGridClient(self.sg_username, self.sg_password)
    
    # ENTER THE EMAIL INFORMATION
    #========================================================#
    #message.set_from("alex.hoang.d@gmail.com")
    #message.set_subject("sendgrid test")
    #message.set_text("Hello,\n\nThis is a test message from SendGrid.    We have sent this to you because you requested a test message be sent from your account.\n\nThis is a link to google.com: http://www.google.com\nThis is a link to apple.com: http://www.apple.com\nThis is a link to sendgrid.com: http://www.sendgrid.com\n\nThank you for reading this test message.\n\nLove,\nYour friends at SendGrid")
    #message.set_html("<table style=\"border: solid 1px #000; background-color: #666; font-family: verdana, tahoma, sans-serif; color: #fff;\"> <tr> <td> <h2>Hello,</h2> <p>This is a test message from SendGrid.    We have sent this to you because you requested a test message be sent from your account.</p> <a href=\"http://www.google.com\" target=\"_blank\">This is a link to google.com</a> <p> <a href=\"http://www.apple.com\" target=\"_blank\">This is a link to apple.com</a> <p> <a href=\"http://www.sendgrid.com\" target=\"_blank\">This is a link to sendgrid.com</a> </p> <p>Thank you for reading this test message.</p> Love,<br/> Your friends at SendGrid</p> <p> <img src=\"http://cdn1.sendgrid.com/images/sendgrid-logo.png\" alt=\"SendGrid!\" /> </td> </tr> </table>")
    #message.add_to("alexhoangd@yahoo.com")
    
    def send_email(self):
        print "Running Scenario 1..."
        msg = message.Mail()
        msg.set_from(self.from_address)
        msg.set_from_name("Alex Hoang - Gmail")
        msg.set_subject("sendgrid send test")
        msg.set_text("Hello,\n\nThis is a test message from SendGrid.    We have sent this to you because you requested a test message be sent from your account.\n\nThis is a link to google.com: http://www.google.com\nThis is a link to apple.com: http://www.apple.com\nThis is a link to sendgrid.com: http://www.sendgrid.com\n\nThank you for reading this test message.\n\nLove,\nYour friends at SendGrid")
        #msg.set_html("<table style=\"border: solid 1px #000; background-color: #666; font-family: verdana, tahoma, sans-serif; color: #fff;\"> <tr> <td> <h2>Hello,</h2> <p>This is a test message from SendGrid.    We have sent this to you because you requested a test message be sent from your account.</p> <a href=\"http://www.google.com\" target=\"_blank\">This is a link to google.com</a> <p> <a href=\"http://www.apple.com\" target=\"_blank\">This is a link to apple.com</a> <p> <a href=\"http://www.sendgrid.com\" target=\"_blank\">This is a link to sendgrid.com</a> </p> <p>Thank you for reading this test message.</p> Love,<br/> Your friends at SendGrid</p> <p> <img src=\"http://cdn1.sendgrid.com/images/sendgrid-logo.png\" alt=\"SendGrid!\" /> </td> </tr> </table>")
        msg.add_bcc(self.from_address)
        #msg.reply_to(self.from_address)
        #msg.set_date(date)
        msg.add_to(self.to_address)
        msg.add_to_name("Alex Hoang - Yahoo")
    
     
        # SEND THE MESSAGE
        #========================================================#
        status, return_msg = self.sg.send(msg)
        
        print "status code: " + str(status)
        print "return message: " + return_msg
        
        try:
            assert status == 200, "status code did not return 200"
            assert "success" in return_msg, "message did not return success"
            print "Scenario 1 passed"
        except AssertionError as e:
            print "Scenario 1 failed: " + e.args[0]
        


    def send_email_with_cc(self):
        print "Running Scenario 2..."
        msg = message.Mail()
        msg.set_from(self.from_address)
        msg.set_subject("sendgrid test")
        msg.set_text("Hello,\n\nThis is a test message from SendGrid.    We have sent this to you because you requested a test message be sent from your account.\n\nThis is a link to google.com: http://www.google.com\nThis is a link to apple.com: http://www.apple.com\nThis is a link to sendgrid.com: http://www.sendgrid.com\n\nThank you for reading this test message.\n\nLove,\nYour friends at SendGrid")
        msg.set_html("<table style=\"border: solid 1px #000; background-color: #666; font-family: verdana, tahoma, sans-serif; color: #fff;\"> <tr> <td> <h2>Hello,</h2> <p>This is a test message from SendGrid.    We have sent this to you because you requested a test message be sent from your account.</p> <a href=\"http://www.google.com\" target=\"_blank\">This is a link to google.com</a> <p> <a href=\"http://www.apple.com\" target=\"_blank\">This is a link to apple.com</a> <p> <a href=\"http://www.sendgrid.com\" target=\"_blank\">This is a link to sendgrid.com</a> </p> <p>Thank you for reading this test message.</p> Love,<br/> Your friends at SendGrid</p> <p> <img src=\"http://cdn1.sendgrid.com/images/sendgrid-logo.png\" alt=\"SendGrid!\" /> </td> </tr> </table>")
        msg.add_to(self.to_address)
        msg.add_cc(self.from_address)
    
     
        # SEND THE MESSAGE
        #========================================================#
        status, return_msg = self.sg.send(msg)
        

    
        print "status code: " + str(status)
        print "return message: " + return_msg
        
        try:
            assert status == 200, "status code did not return 200"
            assert "success" in return_msg, "message did not return success"
            print "Scenario 2 passed"
        except AssertionError as e:
            print "Scenario 2 failed: " + e.args[0]
            
    
    def send_email_with_attachment(self):
        print "Running Scenario 3..."
        msg = message.Mail()
        msg.set_from(self.from_address)
        msg.set_subject("sendgrid test")
        msg.set_text("Hello,\n\nThis is a test message from SendGrid.    We have sent this to you because you requested a test message be sent from your account.\n\nThis is a link to google.com: http://www.google.com\nThis is a link to apple.com: http://www.apple.com\nThis is a link to sendgrid.com: http://www.sendgrid.com\n\nThank you for reading this test message.\n\nLove,\nYour friends at SendGrid")
        msg.set_html("<table style=\"border: solid 1px #000; background-color: #666; font-family: verdana, tahoma, sans-serif; color: #fff;\"> <tr> <td> <h2>Hello,</h2> <p>This is a test message from SendGrid.    We have sent this to you because you requested a test message be sent from your account.</p> <a href=\"http://www.google.com\" target=\"_blank\">This is a link to google.com</a> <p> <a href=\"http://www.apple.com\" target=\"_blank\">This is a link to apple.com</a> <p> <a href=\"http://www.sendgrid.com\" target=\"_blank\">This is a link to sendgrid.com</a> </p> <p>Thank you for reading this test message.</p> Love,<br/> Your friends at SendGrid</p> <p> <img src=\"http://cdn1.sendgrid.com/images/sendgrid-logo.png\" alt=\"SendGrid!\" /> </td> </tr> </table>")
        msg.add_to(self.to_address)
        
        msg.add_attachment("declaration_of_independence.pdf", "../us_doi.pdf")
     
        # SEND THE MESSAGE
        #========================================================#
        status, return_msg = self.sg.send(msg)
        
        print "status code: " + str(status)
        print "return message: " + return_msg
        
        try:
            assert status == 200, "status code did not return 200"
            assert "success" in return_msg, "message did not return success"
            print "Scenario 3 passed"
        except AssertionError as e:
            print "Scenario 3 failed: " + e.args[0]
    
    
    
    def send_email_with_attachment_too_large(self):
        print "Running Scenario 4..."
        msg = message.Mail()
        msg.set_from(self.from_address)
        msg.set_subject("sendgrid test")
        msg.set_text("Hello,\n\nThis is a test message from SendGrid.    We have sent this to you because you requested a test message be sent from your account.\n\nThis is a link to google.com: http://www.google.com\nThis is a link to apple.com: http://www.apple.com\nThis is a link to sendgrid.com: http://www.sendgrid.com\n\nThank you for reading this test message.\n\nLove,\nYour friends at SendGrid")
        msg.set_html("<table style=\"border: solid 1px #000; background-color: #666; font-family: verdana, tahoma, sans-serif; color: #fff;\"> <tr> <td> <h2>Hello,</h2> <p>This is a test message from SendGrid.    We have sent this to you because you requested a test message be sent from your account.</p> <a href=\"http://www.google.com\" target=\"_blank\">This is a link to google.com</a> <p> <a href=\"http://www.apple.com\" target=\"_blank\">This is a link to apple.com</a> <p> <a href=\"http://www.sendgrid.com\" target=\"_blank\">This is a link to sendgrid.com</a> </p> <p>Thank you for reading this test message.</p> Love,<br/> Your friends at SendGrid</p> <p> <img src=\"http://cdn1.sendgrid.com/images/sendgrid-logo.png\" alt=\"SendGrid!\" /> </td> </tr> </table>")
        msg.add_to(self.to_address)
        
        #adding 15 MB file
        msg.add_attachment("italy_guidebook.pdf", "../italy_guidebook.pdf")
        
        
        # SEND THE MESSAGE
        #========================================================#
        
        try:
            status, return_msg = self.sg.send(msg)
            print status
            print return_msg
        except URLError as e:
            print "URL error encountered: " + str(e.args) 
            print "Scenario 4 passed"
        except SendGridClientError:
            print "client error"
            print SendGridClientError
        except SendGridServerError:
            print "server error"
            print SendGridServerError
        else:
            print "exception occurred"    
        
        
    
        
        
if __name__ == '__main__':
    t = Tests()
    t.send_email()
    print "\n"
    t.send_email_with_cc()    
    print "\n"
    t.send_email_with_attachment() 
    print "\n"             
    t.send_email_with_attachment_too_large()   
    
    
                          
                          
    