import solara
from ipyreactplayer import VideoPlayer

videos = [
    {'title': '[YOUTUBE] Bryan Brothers Win Olympia 2006', 'url': 'https://www.youtube.com/watch?v=A_GsZsFbhgc'},
    {'title': '[VIMEO] Edberg vs Gilbert - Cincinatti 1992', 'url': 'https://vimeo.com/663967148/fb7c372be3?share=copy'},
]

# Create a mapping from title to URL for easy lookup
title_to_url_map = {video['title']: video['url'] for video in videos}

# Reactive variable for the currently selected video title
selected_title = solara.reactive(videos[0]['title'])

@solara.component
def Page():
    with solara.Column(align="center"):
        with solara.Card(title="Ipyreactplayer", subtitle="As standalone Solara App."):
            solara.Markdown(
                "Lorem ipsum dolor sit amet consectetur adipisicing elit. "\
                "Commodi, ratione debitis quis est labore voluptatibus! "\
                "Eaque cupiditate minima, at placeat totam, magni doloremque "\
                "veniam neque porro libero rerum unde voluptatem!"
            )
            
            # Dropdown to select videos by title
            solara.Select(label="Video", value=selected_title, values=[video['title'] for video in videos])
            
            # VideoPlayer component that uses the URL corresponding to the selected title
            video_url = title_to_url_map[selected_title.value]
            solara.Row(children=[VideoPlayer(url=video_url)])