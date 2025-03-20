import gi
from lcd_codigo import mostrar_text_lcd  # Importar funcio del Puzzle 1

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, GLib, Gdk

class EntryWindow(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="Puzzle 2 - Display LCD")
        self.set_size_request(450, 250)

        # Aplicar CSS
        self.set_css()

        # Layout principal
        vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
        vbox.set_margin_top(15)
        vbox.set_margin_bottom(15)
        vbox.set_margin_start(15)
        vbox.set_margin_end(15)
        self.add(vbox)

        # Etiqueta dinstruccions
        label = Gtk.Label(label="Escriu un text de fins a 4 linies amb 20 caracters")
        label.get_style_context().add_class("title-label")
        vbox.pack_start(label, False, False, 0)

        # TextView per escriure el text
        self.entry = Gtk.TextView()
        self.entry.set_wrap_mode(Gtk.WrapMode.WORD)
        self.entry.set_size_request(0, 100)
        self.entry.get_style_context().add_class("text-entry")
        self.entry_buffer = self.entry.get_buffer()
        vbox.pack_start(self.entry, True, True, 0)


        # Boto per enviar el text al LCD
        self.button = Gtk.Button(label="Enviar al LCD")
        self.button.connect("clicked", self.on_button_clicked)
        self.button.get_style_context().add_class("display-button")
        vbox.pack_start(self.button, False, False, 0)

    def on_button_clicked(self, widget):
        """Obte el texto del TextView i lenvia al LCD."""
        texto = self.entry_buffer.get_text(self.entry_buffer.get_start_iter(), self.entry_buffer.get_end_iter(), True)
        mostrar_text_lcd(texto)  # Cridem a la funcio del puzle1 per mostrar el text
        print("Text enviat al LCD:\n", texto)    

    def set_css(self):
        """Aplica estils CSS per millorar lexperiencia."""
        css_provider = Gtk.CssProvider()
        css_provider.load_from_data(b"""
            .title-label {
                font-size: 20px;
                font-weight: bold;
                color: #4A4A4A;
            }
            .text-entry {
                font-family: monospace;
                font-size: 20px;
                padding: 5px;
                border: 1px solid #A0A0A0;
                background-color: #FAFAFA;
                border-radius: 8px;
            }
            .display-button {
                font-size: 20px;
                font-weight: bold;
                background-color: #4CAF50;
                color: white;
                padding: 10px;
                border-radius: 8px;
            }
            .display-button:hover {
                background-color: #45A049;
            }
        """)
        
        style_context = Gtk.StyleContext()
        screen = Gdk.Screen.get_default()
        style_context.add_provider_for_screen(screen, css_provider, Gtk.STYLE_PROVIDER_PRIORITY_APPLICATION)

# Ejecutar la aplicacion
win = EntryWindow()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()
