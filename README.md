# YoutubeDataScaraper

This is a simple tool that scrapes data from Youtube playlist and displays the data in an Excelsheet.
<p>Data include video URL, video title, description, upload date and time, channel handle, channel name.</p>
<h3> Two ways to use it:</h3>
1. Download the YouTubePlaylistExporter.exe tool.
<p>
<p>
Or
<p>
<p>
<p>2. Download the Python file and run the following ependency commands in Powershell and in the same directory</p>
<p>* python -m pip install -U yt-dlp</p> 
<p>* python -m yt_dlp -J "PUT_PLAYLIST_URL_HERE" --encoding utf-8 | Out-File -Encoding utf8 playlist.json</p>
<p>* python -m pip install openpyxl</p>
