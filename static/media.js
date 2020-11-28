let audioElem = document.getElementById("audio");
let playButton = document.getElementById("playbutton");

console.log(playButton);
playButton.addEventListener("click", handlePlayButton, false);
audioElem.addEventListener("ended", handleAudioEnd, false);
playAudio();

async function playAudio() {
  try {
    playButton.classList.add("playing");
    await audioElem.play();
  } catch(err) {
    playButton.classList.remove("playing");
  }
}

function handlePlayButton() {
  if (audioElem.paused) {
    playAudio();
  } else {
    audioElem.currentTime = 0;
    playAudio();
  }
}

function handleAudioEnd() {
    playButton.classList.remove("playing");
}
