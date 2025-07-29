import feedparser

README_PATH = "README.md"

til_feed = "https://your-username.github.io/TIL/feed.xml"  # Đổi thành blog hoặc TIL feed của bạn
entries = feedparser.parse(til_feed).entries[:5]  # Lấy 5 bài mới nhất

with open(README_PATH, "r", encoding="utf-8") as f:
    content = f.read()

new_section = "\n".join(
    [f"- [{entry.title}]({entry.link})" for entry in entries]
)

start = "<!-- TIL_SECTION -->"
end = "<!-- END_TIL_SECTION -->"

updated_content = content.split(start)[0] + start + "\n" + new_section + "\n" + end + content.split(end)[1]

with open(README_PATH, "w", encoding="utf-8") as f:
    f.write(updated_content)
