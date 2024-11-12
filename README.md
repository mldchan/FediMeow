
# FediMeow: A bot for meowing hourly on the Fediverse

## How to Start

### Docker

1. Create a Docker compose file
```yml

services:
  mi_meower:
    build: .
    # image: localhost:5000/fedimeow:latest
    environment:
      MI_TOKEN: token
      MI_SERVER: social.mldchan.dev
```

2. `sudo docker compose up -d`
3. Enjoy meowing every hour! :3

### Without Docker

1. Create a `.env` file with `MI_TOKEN` and `MI_SERVER`
2. Create a virtual environment
3. `pip install -U Misskey.py`
4. `python meow.py`

## Development

Anyone can register on my instance, although I choose to approve certain users.

If enough interest is shown in this project, I will set up mirroring with Codeberg or GitHub, but time will see.

## Contributions

Suggestions are welcome! `@mld@social.mldchan.dev` me on the Fediverse to suggest stuff!

Financial donations are also welcome! You can [donate to me here.](https://mldchan.dev/donate) [(Backup link)](https://mldkyt.nekoweb.org/donate).

