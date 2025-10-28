# rmbg

Remove background using [`rembg`](https://github.com/danielgatis/rembg)

## Model

download the model: https://github.com/danielgatis/rembg?tab=readme-ov-file#models

For this project, choose `u2net`

Save to `u2net` folder in this project dir.

## Install

install all the necessary requirements

```bash
pip install -r requirements.txt
```

#### Recommendation

install it inside virtual environment

## How to Run

locally, just run

```bash
uwsgi --http localhost:1234 --master -p 4 -w main:app
```

### Docker

Even simpler, just run this (`sudo` maybe required)

```bash
docker build -t rmbg .

docker run -p 1234:1234 rmbg
```

you can change `rmbg` to any other name.
