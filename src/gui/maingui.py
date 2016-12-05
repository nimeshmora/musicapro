import gi
import essentia

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
from essentia.standard import *


class Handler:
    def onDeleteWindow(self, *args):
        Gtk.main_quit(*args)

    def onBtnClicked(self, button):
        print("Dancebility value of song:")
        audio = MonoLoader(filename='../../res/b.mp3')()
        dnc, dfa = Danceability()(audio)
        print dnc

        loudness = Loudness()(audio)
        print("Loudness value of song:")
        print loudness

    def createGUI(self):
        builder = Gtk.Builder()
        builder.add_from_file("../../res/musicagui.glade")
        builder.connect_signals(Handler())

        window = builder.get_object("window1")
        window.show_all()

        Gtk.main()