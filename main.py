from flask import Flask, request, render_template, send_file
from rembg import remove
from PIL import Image
import io

MAX_FILE_SIZE = 10 * 1024 * 1024  # 10MB in bytes
app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def main():
  if (request.method == "POST"):
    return handle_submit()
  return render_template('index.html')

def handle_submit():
  if "img" not in request.files:
    return "No file selected", 400
  file = request.files['img']
  if file.filename == '':
    return "No file selected", 400
  if request.content_length and request.content_length > MAX_FILE_SIZE:
    return "File size exceeds 10MB limit", 400
  try:
    input_img = Image.open(file.stream)
    output_img = remove(input_img)

    img_io = io.BytesIO()
    output_img.save(img_io, 'webp')
    img_io.seek(0)
    return send_file(
      img_io,
      as_attachment=True,
      download_name=f"bg_removed_{file.name.split(".")[0]}.webp",
      mimetype="image/webp"
    )
  except Exception as e:
    return f'Error processing Image: {str(e)}', 500

