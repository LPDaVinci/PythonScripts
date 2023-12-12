import psutil
import socket
import struct
import time
import smtplib  # SMTP-Modul für E-Mail-Versand

# Funktion zur Überprüfung des RAM
def check_ram():
    ram = psutil.virtual_memory()
    ram_usage = ram.used / ram.total
    print(f"RAM Total: {ram.total >> 30}GB")
    print(f"RAM Used: {ram.used >> 30}GB")
    print(f"RAM Free: {ram.free >> 30}GB")
    return ram_usage > 0.7  # Rückgabe True, wenn RAM-Nutzung über 70% liegt

# Funktion zur Überprüfung des Festplattenspeichers
def check_disk_space():
    disk = psutil.disk_usage('/')
    disk_usage = disk.used / disk.total
    print(f"Disk Total: {disk.total >> 30}GB")
    print(f"Disk Used: {disk.used >> 30}GB")
    print(f"Disk Free: {disk.free >> 30}GB")
    return disk_usage > 0.8  # Rückgabe True, wenn Festplattennutzung über 80% liegt

# Funktion zur Überprüfung der CPU-Auslastung
def check_cpu():
    cpu_usage = psutil.cpu_percent(interval=1)
    print(f"CPU Usage: {cpu_usage}%")
    return cpu_usage > 80  # Rückgabe True, wenn CPU-Auslastung über 80% liegt

# Funktion zur Überprüfung der Internetverbindung mit einem Ping-ähnlichen Ansatz
def check_internet():
    try:
        host = "1.1.1.1"  # Cloudflare DNS-Server IP-Adresse
        port = 80  # Beispiel-Port für die Verbindung
        icmp = socket.getprotobyname("icmp")
        with socket.socket(socket.AF_INET, socket.SOCK_RAW, icmp) as s:
            s.connect((host, port))
            s.settimeout(3)
            payload = b'\x08\x00\x7d\x4b\x00\x00\x00\x00Ping'
            s.sendall(payload)
            start_time = time.time()
            while True:
                recv_data, addr = s.recvfrom(1024)
                end_time = time.time()
                if end_time - start_time > 10:
                    raise socket.timeout()
                if recv_data:
                    print("Internet is reachable.")
                    return False  # Internet ist erreichbar
    except (socket.error, socket.timeout):
        print("Internet is unreachable.")
        return True  # Internet ist nicht erreichbar

# Funktion für den Versand von E-Mail-Benachrichtigungen
def send_alert(message):
    sender_email = "deine_email@gmail.com"  # Absender-E-Mail-Adresse
    receiver_email = "empfänger_email@gmail.com"  # Empfänger-E-Mail-Adresse
    password = "dein_email_passwort"  # Passwort für die Absender-E-Mail-Adresse (vermeide Hardcoding)

    subject = "System Alert"
    email_message = f"Subject: {subject}\n\n{message}"

    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, email_message)
        print("Alert email sent successfully!")
        server.quit()  # Schließe die Verbindung explizit
    except:
        print("SMTP connection error. Please verify SMTP settings and internet connectivity.")


# Testen der Funktionen
ram_alert = check_ram()  # RAM-Überprüfung
disk_alert = check_disk_space()  # Festplatten-Überprüfung
cpu_alert = check_cpu()  # CPU-Überprüfung
internet_alert = check_internet()  # Internet-Überprüfung

# Erzeuge eine Ausgabe basierend auf den Ergebnissen der Überprüfungen
if ram_alert or disk_alert or cpu_alert or internet_alert:
    alert_message = "Alert! System parameters exceed threshold:\n"
    if ram_alert:
        alert_message += "RAM usage is above 70%.\n"
    if disk_alert:
        alert_message += "Disk usage is above 80%.\n"
    if cpu_alert:
        alert_message += "High CPU usage detected!\n"
    if internet_alert:
        alert_message += "Internet is unreachable.\n"

    send_alert(alert_message)
else:
    print("System parameters are within normal limits.")
