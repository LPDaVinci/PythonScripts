import psutil
import socket
import struct
import time
import smtplib  # SMTP-Modul für E-Mail-Versand
import requests  # Modul für HTTP-Anfragen

# Funktion zur Überprüfung des RAM
def check_ram():
    ram = psutil.virtual_memory()
    ram_usage = ram.used / ram.total
    print(f"RAM Total: {ram.total >> 30}GB")
    print(f"RAM Used: {ram.used >> 30}GB")
    print(f"RAM Free: {ram.free >> 30}GB")
    if ram_usage > 0.7:
        print("Alert: RAM usage is above 70%.")
    return ram_usage > 0.7  # Rückgabe True, wenn RAM-Nutzung über 70% liegt

# Funktion zur Überprüfung des Festplattenspeichers
def check_disk_space():
    disk = psutil.disk_usage('/')
    disk_usage = disk.used / disk.total
    print(f"Disk Total: {disk.total >> 30}GB")
    print(f"Disk Used: {disk.used >> 30}GB")
    print(f"Disk Free: {disk.free >> 30}GB")
    if disk_usage > 0.8:
        print("Alert: Disk usage is above 80%.")
    return disk_usage > 0.8  # Rückgabe True, wenn Festplattennutzung über 80% liegt

# Funktion zur Überprüfung der CPU-Auslastung
def check_cpu():
    cpu_usage = psutil.cpu_percent(interval=1)
    print(f"CPU Usage: {cpu_usage}%")
    if cpu_usage > 80:
        print("Alert: High CPU usage detected!")
    return cpu_usage > 80  # Rückgabe True, wenn CPU-Auslastung über 80% liegt

# Funktion zur Überprüfung der Internetverbindung mit einem Ping-ähnlichen Ansatz
def check_internet():
    try:
        host = "1.1.1.1"  # Cloudflare DNS-Server IP-Adresse
        port = 80  # Beispiel-Port für die Verbindung
        icmp = socket.getprotobyname("icmp")
        with socket.socket(socket.AF_INET, socket.SOCK_RAW, icmp) as s:
            s.connect((host, port))
            s.settimeout(10)
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
    except (socket.error, socket.timeout) as e:
        print(f"Error checking internet connectivity: {e}")
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

# Funktion für den Versand von Discord-Webhook-Benachrichtigungen
def send_discord_alert(category,message):
    # Discord-Webhook-URL hier einfügen
    webhook_url = 'YOUR_WEBHOOK'

    colors = {
        "RAM": 0xFF5733,  # Orange
        "Disk Space": 0x3498db,  # Blau
        "CPU": 0x27ae60,  # Grün
        "Internet Connectivity": 0xe74c3c,  # Rot
        "System Functional": 0x2ecc71  # Hellgrün
    }

    discord_data = {
        "embeds": [
            {
                "title": f"System Alert: {category}",
                "description": message,
                "color": colors[category]
            }
        ]
    }


    try:
        response = requests.post(webhook_url, json=discord_data)
        if response.status_code == 204:
            print(f"Discord alert for {category} sent successfully!")
        else:
            print(f"Failed to send Discord alert for {category}. Status code: {response.status_code}")
    except requests.RequestException as e:
        print(f"Error sending Discord alert for {category}: {e}")

# Dauerhaftes Monitoring in einer Schleife
while True:
    categories = {
        "RAM": check_ram(),
        "Disk Space": check_disk_space(),
        "CPU": check_cpu(),
        "Internet Connectivity": check_internet()
    }
    
    alarm_triggered = any(categories.values())

    for category, alert_status in categories.items():
        if alert_status:
            alert_message = f"Alert: {category} exceeded threshold."
            send_alert(alert_message)  # Sende E-Mail
            send_discord_alert(category, alert_message)  # Sende Discord-Webhook-Benachrichtigung
        else:
            print(f"{category} is within normal limits.")

    if not alarm_triggered:
        functional_message = "System is operating within normal parameters."
        send_discord_alert("System Functional", functional_message)  # Sende Discord-Webhook-Benachrichtigung
        print("System is operating within normal parameters.")


    time.sleep(300)  # Warte 5 Minuten vor der nächsten Überprüfung
