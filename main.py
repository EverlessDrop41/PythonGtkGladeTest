#This app is a simple Hello world that uses PyGtk
from gi.repository import Gtk

def setLabel(Label, text):
	try:
		Label.set_text(text)
	except:
		Gtk.main_quit()

class SignalMaster:
	def defaultLog (self, button):
		setLabel(builder.get_object("HelloWorldLabel"),"Hi world")
	def customLog (self, button):
		custTextInput = builder.get_object("CustomLogInput")
		try:
			custText = custTextInput.get_text()
		except AttributeError:
			print "Cust Text Input doesn't have: get_text()"

		setLabel(builder.get_object("HelloWorldLabel"),custText)


if __name__ == "__main__":
	builder = Gtk.Builder()
	builder.add_from_file("HelloWorld.glade")
	window = builder.get_object("window1")
	window.show_all()
	builder.connect_signals(SignalMaster())
	Gtk.main()
