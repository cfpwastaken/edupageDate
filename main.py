from edupage_api import Edupage
from datetime import datetime, timedelta
from halo import Halo
import os, sys

spinner = Halo(text="Logging in", spinner="dots")
spinner.start()

ep = Edupage()
username = os.getenv("EDUPAGE_USERNAME")
password = os.getenv("EDUPAGE_PASSWORD")
subdomain = os.getenv("EDUPAGE_SUBDOMAIN")
ep.login(username, password, subdomain)

name = sys.argv[1]

date = datetime.today()

try:
	while True:
		spinner.text = "Getting timetable for " + date.strftime("%A, %d.%m.%Y")
		t = ep.get_timetable(date)
		for i, lesson in enumerate(t.lessons):
			if lesson.name:
				if lesson.name != name:
					continue
				spinner.stop()
				print(str(i) + " " + lesson.name + " on " + date.strftime("%A, %d.%m.%Y") + ": " + lesson.curriculum)
				spinner.start()
		date -= timedelta(days=1)
except KeyboardInterrupt:
	spinner.stop()