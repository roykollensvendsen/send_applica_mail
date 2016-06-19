#!/usr/bin/env python
# -*- coding: utf-8 -*-'''

"""Usage: send_applica_mail.py USERNAME PASSWORD RECEIVER SUBJECT MESSAGE_FILE
          send_applica_mail.py (-h | --help)

Arguments:
  USERNAME      Your username
  PASSWORD      Your password
  RECEIVER      E-mail address of the reciver
  SUBJECT       String describing the subject
  MESSAGE_FILE  File containing message

Options:
    -h,--help  Show this screen and exit.
"""

from selenium import webdriver
from docopt import docopt


class ApplicaMail(object):
    """A class for communicating with applica web-mail"""

    def __init__(self):
        """Open applica web-mail in firefox"""
        self.browser = webdriver.Firefox()
        self.browser.get('https://post.applica.no')

    def log_on(self, username, password):
        """Log on with your username and password"""
        self.browser.find_element_by_id('username').send_keys(username)
        self.browser.find_element_by_id('password').send_keys(password)
        self.browser.find_element_by_class_name('btn').click()

    def send_msg(self, receiver, subj, msg):
        """Send an e-mail to someone"""
        self.browser.find_element_by_id('newmsgc').click()
        self.browser.switch_to_window(self.browser.window_handles[1])
        self.browser.find_element_by_id('divTo').send_keys(receiver)
        self.browser.find_element_by_id('txtSubj').send_keys(subj)
        self.browser.find_element_by_id('ifBdy').send_keys(msg)
        self.browser.find_element_by_id('send').click()


def main(docopt_args):
    """Our main method"""
    # Create an ApplicaMail object
    applica_mail = ApplicaMail()
    # Log on to Applica web-mail
    applica_mail.log_on(docopt_args['USERNAME'],
                        docopt_args['PASSWORD'])
    # Retreive message file
    message_file = open(docopt_args['MESSAGE_FILE'],'r')
    # Send an e-mail
    applica_mail.send_msg(docopt_args['RECEIVER'],
                          docopt_args['SUBJECT'],
                          message_file.read())


if __name__ == "__main__":
    arguments = docopt(__doc__)
    main(arguments)
