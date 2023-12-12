import psutil
import socket
import struct
import time
import requests
import smtplib
import logging

from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

class SystemMonitor:
    def __init__(self):
        self.webhook_url = 'YOURWEBHOOK'
        self.setup_logging()

    def setup_logging(self):
        logging.basicConfig(filename='system_monitor.log', level=logging.INFO,
                            format='%(asctime)s - %(levelname)s - %(message)s')

    def log_message(self, message, level='info'):
        levels = {'info': logging.INFO, 'error': logging.ERROR, 'warning': logging.WARNING}
        logging.log(levels[level], message)

    def send_discord_alert(self, category, message, color):
        colors = {
            "RAM": 0xFF5733,
            "Disk Space": 0x3498db,
            "CPU": 0x27ae60,
            "Internet Connectivity": 0xe74c3c,
            "System Functional": 0x2ecc71
        }

        discord_data = {
            "embeds": [
                {
                    "title": f"System Alert: {category}",
                    "description": message,
                    "color": colors[color]
                }
            ]
        }

        try:
            response = requests.post(self.webhook_url, json=discord_data)
            if response.status_code == 204:
                print(f"Discord alert for {category} sent successfully!")
            else:
                print(f"Failed to send Discord alert for {category}. Status code: {response.status_code}")
        except requests.RequestException as e:
            print(f"Error sending Discord alert for {category}: {e}")

    def check_ram_condition(self):
        threshold = 0.7  # RAM-Schwellenwert, z.B. 70%
        ram = psutil.virtual_memory()
        used_percentage = ram.used / ram.total
        return used_percentage > threshold, used_percentage * 100

    def check_disk_space_condition(self):
        threshold = 0.1  # Festplattenspeicher-Schwellenwert, z.B. 80%
        disk = psutil.disk_usage('/')
        used_percentage = disk.used / disk.total
        return used_percentage > threshold, used_percentage * 100

    def check_cpu_condition(self):
        threshold = 80  # CPU-Schwellenwert, z.B. 80%
        cpu_usage = psutil.cpu_percent(interval=1)
        return cpu_usage > threshold, cpu_usage

    def check_internet_condition(self):
        try:
            host = "1.1.1.1"
            port = 80
            icmp = socket.getprotobyname("icmp")
            s = socket.socket(socket.AF_INET, socket.SOCK_RAW, icmp)
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
                    return False, None
        except (socket.error, socket.timeout):
            return True, None

    def send_alert(self, message):
        smtp_server = 'smtp.gmail.com'
        port = 587
        sender_email = 'YOUR_EMAIL@gmail.com'  # Absender-E-Mail-Adresse
        receiver_email = 'RECIPIENT_EMAIL@gmail.com'  # Empfänger-E-Mail-Adresse
        password = 'YOUR_PASSWORD'  # Absender-E-Mail-Passwort
        subject = 'System Alert'  # E-Mail-Betreff

        email_message = MIMEMultipart()
        email_message['From'] = sender_email
        email_message['To'] = receiver_email
        email_message['Subject'] = subject
        email_message.attach(MIMEText(message, 'plain'))

        try:
            with smtplib.SMTP(smtp_server, port) as server:
                server.starttls()
                server.login(sender_email, password)
                server.sendmail(sender_email, receiver_email, email_message.as_string())
                print("Alert email sent successfully!")
        except:
            print("SMTP connection error. Please verify SMTP settings and internet connectivity.")

    def monitor_system(self):
        while True:
            ram_alert, ram_percentage = self.check_ram_condition()
            if ram_alert:
                alert_message = f"Alert: RAM usage exceeded threshold. Currently at {ram_percentage:.2f}%."
                self.send_discord_alert("RAM", alert_message, "RAM")
                self.log_message(alert_message, 'error')
                self.send_alert(alert_message)
                print(alert_message)
            else:
                log_message = f"RAM usage within limits. Currently at {ram_percentage:.2f}%."
                self.log_message(log_message, 'info')
                print(log_message)

            disk_alert, disk_percentage = self.check_disk_space_condition()
            if disk_alert:
                alert_message = f"Alert: Disk Space usage exceeded threshold. Currently at {disk_percentage:.2f}%."
                self.send_discord_alert("Disk Space", alert_message, "Disk Space")
                self.log_message(alert_message, 'error')
                self.send_alert(alert_message)
                print(alert_message)
            else:
                log_message = f"Disk Space usage within limits. Currently at {disk_percentage:.2f}%."
                self.log_message(log_message, 'info')
                print(log_message)

            cpu_alert, cpu_usage = self.check_cpu_condition()
            if cpu_alert:
                alert_message = f"Alert: CPU usage exceeded threshold. Currently at {cpu_usage:.2f}%."
                self.send_discord_alert("CPU", alert_message, "CPU")
                self.log_message(alert_message, 'error')
                self.send_alert(alert_message)
                print(alert_message)
            else:
                log_message = f"CPU usage within limits. Currently at {cpu_usage:.2f}%."
                self.log_message(log_message, 'info')
                print(log_message)

            internet_alert, _ = self.check_internet_condition()
            if internet_alert:
                alert_message = "Alert: Internet Connectivity issue."
                self.send_discord_alert("Internet Connectivity", alert_message, "Internet Connectivity")
                self.log_message(alert_message, 'error')
                self.send_alert(alert_message)
                print(alert_message)
            else:
                self.log_message("Internet Connectivity is fine.", 'info')
                print("Internet Connectivity is fine.")

            time.sleep(5)

if __name__ == "__main__":
    monitor = SystemMonitor()
    monitor.monitor_system()
