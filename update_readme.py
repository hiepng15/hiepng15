import feedparser

README_PATH = "README.md"

til_feed = "https://hiepng15.github.io/TIL/feed.xml"
blog_feed = "https://hiepng15.github.io/feed.xml"

def get_entries(feed_url, max_entries=5):
    feed = feedparser.parse(feed_url)
    return feed.entries[:max_entries]

def format_entries(entries):
    return "\n".join([f"- [{entry.title}]({entry.link})" for entry in entries])

with open(README_PATH, "r", encoding="utf-8") as f:
    content = f.read()

til_entries = get_entries(til_feed)
til_section = format_entries(til_entries)

blog_entries = get_entries(blog_feed)
blog_section = format_entries(blog_entries)

start_til = "<!-- TIL_SECTION -->"
end_til = "<!-- END_TIL_SECTION -->"
content = content.split(start_til)[0] + start_til + "\n" + til_section + "\n" + end_til + content.split(end_til)[1]

start_blog = "<!-- BLOG_SECTION -->"
end_blog = "<!-- END_BLOG_SECTION -->"
content = content.split(start_blog)[0] + start_blog + "\n" + blog_section + "\n" + end_blog + content.split(end_blog)[1]

with open(README_PATH, "w", encoding="utf-8") as f:
    f.write(content)
