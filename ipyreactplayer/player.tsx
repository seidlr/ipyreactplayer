import React, { useRef, useEffect, useState } from "react";
import ReactPlayer from "https://esm.sh/react-player@2.13.0";

const App = ({
  url,
  width,
  height,
  playing,
  loop,
  controls,
  light,
  volume,
  muted,
  playbackRate,
  progressInterval,
  playsinline,
  config,
  time,
  seek_position,
  set_time,
  set_seek_position,
  set_playing,
}) => {
  const [shouldRenderPlayer, setShouldRenderPlayer] = useState(false);
  const player = useRef(null);

  useEffect(() => {
    const timer = setTimeout(() => {
      setShouldRenderPlayer(true);
    }, 2000); // Wait for 2 seconds before rendering the player

    return () => clearTimeout(timer); // Clean up the timer on component unmount
  }, []);

  function seekTo(position) {
    if (position !== null) {
      console.log(`Seek to ${position}`);
      player.current?.seekTo(position);
    }
  }

  function handleProgress(state) {
    const { playedSeconds } = state;
    set_time(playedSeconds);
  }

  function handleSeek() {
    const time = player.current?.getCurrentTime();
    if (time !== null) {
      set_seek_position(time);
      set_time(time);
    }
  }

  function handlePause(state) {
    const time = player.current?.getCurrentTime();
    set_playing(false);
    set_time(time);
    set_seek_position(time);
  }

  function handlePlay(state) {
    set_playing(true);
    set_seek_position(null);
  }

  const MyUpdater = ({ seek_position }) => {
    seekTo(seek_position);
    return <span></span>;
  };

  return (
    <>
      <div className="App">
        {!shouldRenderPlayer ? (
          <div>Loading...</div>
        ) : (
          <ReactPlayer
            ref={player}
            url={url}
            width={width}
            height={height}
            playing={playing}
            loop={loop}
            controls={controls}
            light={light}
            volume={volume}
            muted={muted}
            playbackRate={playbackRate}
            progressInterval={progressInterval}
            playsinline={playsinline}
            config={config}
            onProgress={handleProgress}
            onPause={handlePause}
            onPlay={handlePlay}
            onSeek={handleSeek}
          />
        )}
        <MyUpdater seek_position={seek_position} />
      </div>
    </>
  );
};

export default App;
