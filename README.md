# Ipyreactplayer

[![Version](https://img.shields.io/pypi/v/ipyreactplayer.svg)](https://pypi.python.org/project/ipyreactplayer) [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/seidlr/ipyreactplayer/blob/main/example.ipynb)

Use Ipyreactplayer if you want to be able to control a videoplayer in a jupyter notebook, lab, voila or solara.
It is a simple wrapper using [Ipyreact](https://github.com/widgetti/ipyreact) with [react-player](https://github.com/cookpete/react-player)
Similar to [streamlit-player](https://github.com/okld/streamlit-player) or [dash-player](https://dash.plotly.com/dash-player) in nature.

Works with:

- Google Colab [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/seidlr/ipyreactplayer/blob/main/example.ipynb)
- Jupyter notebook
- Jupyter lab
- Voila (`version>0.5`)
- [Solara](https://github.com/widgetti/solara/)
  see the example under `solara`.

## Usage

### With ipywidgets

```python
from ipyreactplayer import VideoPlayer

url = 'https://vimeo.com/663967148/fb7c372be3?share=copy'
player = VideoPlayer(url=url)
display(player)

# seek to position
player.seek(1024.0)

# play/pause
player.play_pause()

# mute/unmute
player.muted = True

# show/hide controls
player.controls = True

# change source
player.url = 'https://vimeo.com/755209790/8e428d0213?share=copy'
```

### With voila

`voila example.ipynb`

### With Solara

From notebook

```cd solara/notebook
solara run solara.ipynb
```

As app

```
cd solara/pages
solara run .
```

## Installation

```
$ pip install ipyreactplayer
```
