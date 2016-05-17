from gi.repository import Notify
import ping, socket

try:
	#ping.verbose_ping('www.google.com', count=3)
	if ping.Ping('www.wikipedia.org', timeout=2000).do():
		Notify.init("Teste")
		Notify.Notification.new("Pingou").show()
except socket.error, e:
    print "Ping Error:", e
