import pyshorteners

short= pyshorteners.Shortener()

your_url = "https://cataz.to/watch-tv/watch-stranger-things-2016-39444.4874221"

shorten_url = short.tinyurl.short(your_url)

print("The desired URL is :", shorten_url)
