import ipyreact
import pathlib
from traitlets import Int, Unicode, Float, Bool, Dict, signature_has_traits

default_position = 38*60+24.0
default_url = 'https://vimeo.com/663967148/fb7c372be3?share=copy'


class VideoPlayer(ipyreact.ReactWidget):
    url = Unicode(default_url).tag(sync=True)
    width = Unicode("640px").tag(sync=True)
    height = Unicode("360px", allow_none=True).tag(sync=True)
    playing = Bool(False).tag(sync=True)
    loop = Bool(False).tag(sync=True)
    controls = Bool(True).tag(sync=True)
    light = Bool(False).tag(sync=True)
    volume = Float(1.0, allow_none=True).tag(sync=True)
    muted = Bool(False).tag(sync=True)
    playbackRate = Float(default_value=1.0).tag(sync=True)
    progressInterval = Int(default_value=1000).tag(sync=True)
    playsinline = Bool(False).tag(sync=True)
    config = Dict({}).tag(sync=True)
    
    time = Float(0.0).tag(sync=True)
    # Helper to call seek method in reactplayer on
    seek_position = Float(0.0, allow_none=True).tag(sync=True)
    
    _esm = pathlib.Path(__file__).parent / "player.tsx"

    @property
    def current_time(self):
        return self.time
    
    @current_time.setter
    def current_time(self, value):
        self.seek(value)

    def play_pause(self):
        with self.hold_sync():
            self.playing = not self.playing
            self.seek_position = None

    def seek(self, seek_position):
        with self.hold_sync():
            self.seek_position = seek_position
            self.time = seek_position

