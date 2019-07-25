#Per utilizzare il servizio di invio eMail, nel proprio account Gmail, bisogna
#abilitare l'utilizzo delle APP MENO SICURO, affinchè il programma seguente possa essere
#utilizzate, altrimenti verrà generato un errore e sarà inviata una mail al proprio 
#indirizzo di posta elettronica.
import smtplib

def sendMail():
    print("""
    CERCHIAMO DI INVIARE UN eMAIL UTILIZZANDO IL SERVIZIO DI GMAIL!
    """)

    user = input("USERNAME: ")
    password = input("PASSWORD: ")
    destinatario = input("DESTINATARIO: ")
    oggetto = "Subject: " + input("OGGETTO: ")
    contenuto = "\n\n" + input("CONTENUTO MAIL: ")
    messaggio = oggetto + contenuto

    print("Connessione col Server...")
    email = smtplib.SMTP("smtp.gmail.com", 587)
    email.ehlo() #effettuo richiesta di accesso Server .
    email.starttls()
    email.login(user, password) #Effettuo il login .
    
    print("Invio in corso...")
    email.sendmail(user, destinatario, messaggio)
    email.quit()
    
    print("Messaggio Inviato correttamente!, grazie di aver usufruito del nostro servizio")

sendMail() #Richiamo la funzione, affinchè possa utilizzarla .