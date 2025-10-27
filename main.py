from flask import Flask, request, Request, render_template, send_file
from rembg import remove
from PIL import Image
import io

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def main():
  if (request.method == "POST"):
    return handle_submit(request)
  return render_template('index.html')

def handle_submit(request: Request):
  if "img" not in request.files:
    return "No file selected", 400
  file = request.files['img']
  if file.filename == '':
    return "No file selected", 400
  try:
    input_img = Image.open(file.stream)
    output_img = remove(input_img, model_path="model/u2net.onnx")

    img_io = io.BytesIO()
    output_img.save(img_io, 'PNG')
    img_io.seek(0)
    return send_file(
      img_io,
      as_attachment=True,
      download_name=f"bg_removed_{file.name.split(".")[0]}.png",
      mimetype="image/png"
    )
  except Exception as e:
    return f'Error processing Image: {str(e)}', 500
