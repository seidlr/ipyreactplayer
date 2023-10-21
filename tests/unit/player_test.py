import ipyreactplayer


def test_create_player():
    url = 'https://vimeo.com/663967148/fb7c372be3?share=copy'
    player = ipyreactplayer.VideoPlayer(url=url)
    assert player.url == url


