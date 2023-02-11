function change() {
  text = document.getElementById("text").value;
  document.getElementById("submit-button").value = text;
}

function shareText(text, music) {
  url =
    "https://twitter.com/share?text=「" +
    text +
    "」なあなたにおすすめな曲は「" +
    music +
    "」です！%0D%0A";
  document.getElementById("twitter-share").setAttribute("href", url);
}
