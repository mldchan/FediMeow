import asyncio
import os
import random
import dotenv

from misskey import Misskey

dotenv.load_dotenv()

if not os.getenv('MI_SERVER') or not os.getenv('MI_TOKEN'):
    print('Need MI_SERVER or MI_TOKEN variable')
    exit(1)

mi = Misskey(os.getenv('MI_SERVER'), i=os.getenv('MI_TOKEN'))

meows = ['mraw :3', 'mraow :3c', 'meow :3', 'mrow', 'meow', 'nya', 'nya~', 'nya~ :3', 'nya :3', 'にゃ', 'にゃ～', 'にゃ～：３']

async def main():
    while True:
        mi.notes_create(text=random.choice(meows))
        await asyncio.sleep(3600)

if __name__ == '__main__':
    asyncio.run(main())
