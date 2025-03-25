import gi
from lcd_codigo import mostrar_text_lcd  # Importamos la funcion del Puzzle 1

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, GLib, Gdk

class EntryWindow(Gtk.Window):
    def __init__(self):
        # Configuracio inicial de la finestra
        Gtk.Window.__init__(self, title="Puzzle 2 - Display LCD")
        self.set_size_request(285, 235)
        self.set_resizable(False)

        # Carreguem estils CSS
        self.set_css("estils.css")

        # Creem el layout principal vertical
        vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
        vbox.get_style_context().add_class("main-container")
        self.add(vbox)

        # Afegim una etiqueta amb instruccions
        label = Gtk.Label(label="Maxim: 4 files i 20 caracters")
        label.get_style_context().add_class("title-label")
        vbox.pack_start(label, False, False, 0)

        # Creem el quadre de text per escriure
        self.entry = Gtk.TextView()
        self.entry.set_wrap_mode(Gtk.WrapMode.WORD)
        self.entry.get_style_context().add_class("text-entry")
        self.entry_buffer = self.entry.get_buffer()
        self.entry.set_size_request(249, 109)  # Limitem tamany visible
        vbox.pack_start(self.entry, True, True, 0)

        # Afegim un boto per enviar el text
        self.button = Gtk.Button(label="Enviar al LCD")
        self.button.connect("clicked", self.on_button_clicked)
        self.button.get_style_context().add_class("display-button")
        vbox.pack_start(self.button, False, False, 0)

        # Connectem un event per limitar el text
        self.entry_buffer.connect("changed", self.on_text_changed)

    def on_button_clicked(self, widget):
        # Enviem el text del quadre al LCD
        texto = self.entry_buffer.get_text(self.entry_buffer.get_start_iter(), self.entry_buffer.get_end_iter(), True)
        mostrar_text_lcd(texto)
        print("Texto enviado al LCD:\n", texto)

    def on_text_changed(self, buffer):
        # Limitem el text a 4 filas i 20 caracters per fila
        texto = buffer.get_text(buffer.get_bounds()[0], buffer.get_bounds()[1], True)

        lineas = texto.split("\n")
        if len(lineas) > 4:
            lineas = lineas[:4]

        lineas = [linea[:20] for linea in lineas]
        texto_limitado = "\n".join(lineas)

        if texto != texto_limitado:
            buffer.set_text(texto_limitado)

    def set_css(self, css_file):
        # Carreguem i apliquem estils CSS desde un fitxer
        css_provider = Gtk.CssProvider()

        with open(css_file, "rb") as css:
            css_provider.load_from_data(css.read())

        screen = Gdk.Screen.get_default()
        style_context = Gtk.StyleContext()
        style_context.add_provider_for_screen(screen, css_provider, Gtk.STYLE_PROVIDER_PRIORITY_APPLICATION)

# Iniciem la aplicacio
win = EntryWindow()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()