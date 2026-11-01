import os
from flask import Flask, jsonify, render_template, request

app = Flask(__name__)

# Esnek video listesi (Veritabanı altyapısı)
videos = [
    {
        "id": 1,
        "title": "İlk Efsane Video - Platform Açıldı!",
        "author": "Metin Yiğit",
        "verified": True,
        "views": "1.4K",
        "url": "https://www.youtube.com/embed/dQw4w9WgXcQ",
    }
]


@app.route("/")
def index():
  return render_template("index.html")


@app.route("/api/videos", methods=["GET"])
def get_videos():
  return jsonify(videos)


@app.route("/api/videos", methods=["POST"])
def upload_video():
  data = request.json
  if not data or "title" not in data or "url" not in data:
    return jsonify({"status": "error", "message": "Eksik bilgi!"}), 400

  new_video = {
      "id": len(videos) + 1,
      "title": data.get("title"),
      "author": "Metin Yiğit",
      "verified": True,
      "views": "1",
      "url": data.get("url"),
  }
  videos.append(new_video)
  return jsonify({"status": "success", "video": new_video})


if __name__ == "__main__":
  port = int(os.environ.get("PORT", 5000))
  app.run(host="0.0.0.0", port=port)