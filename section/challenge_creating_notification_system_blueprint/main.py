from abc import ABC, abstractmethod

# Define the abstract base class Notifier

# Define the EmailNotifier subclass

# Define the SMSNotifier subclass

# Define the notify_user function

print(notify_user(email_notifier, "Welcome!"))
print(notify_user(sms_notifier, "Your code is 1234."))