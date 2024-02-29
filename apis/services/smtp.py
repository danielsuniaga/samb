import apis.repositories.notification as repository_notifications

class cases_smtp:

    def __init__(self,cursor):

        self.smtp = repository_notifications.repositories_smtp(cursor)

    def send_notification_email(self,date,mensaje):
        
        return self.smtp.send(date,mensaje)