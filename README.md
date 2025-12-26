# YoutubeDataScaraper

This is a simple tool that scrapes data from Youtube playlist and displays the data in an Excelsheet.

<h3> Two ways to use it:</h3>
1. Download the [YouTubePlaylistExporter.exe](https://github.com/saddiboi/YoutubeDataScaraper/blob/main/YouTubePlaylistExporter.exe) tool.
<p>
<p>
Or
<p>
<p>
<p>2. Download the Python file and run the following ependency commands in Powershell and in the same directory</p>
* python -m pip install -U yt-dlp
* python -m yt_dlp -J "Put the URL of the Playlist" --encoding utf-8 | Out-File -Encoding utf8 playlist.json
* python -m pip install openpyxl
