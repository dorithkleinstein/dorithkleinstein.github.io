# Share cards

The pictures shown when a page of dorithkleinstein.com is shared on Facebook, WhatsApp or LinkedIn. 1200 by 630 pixels.

- `card.html` is the template. The words for each card are in `CARDS`, near the bottom. It uses the site's fonts: Assistant for Hebrew, Source Sans 3 for English.
- `lines.svg` is the faint lines behind the words: average birth weight by state, 2016 to 2024, from the birth outcomes dbt project. `make-lines.py` draws it again if needed.
- `card-he.png` and `card-en.png` are the finished cards.

## Making a card again

In Terminal, from this folder, one line per language:

    "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome" --headless=new --hide-scrollbars --force-device-scale-factor=1 --user-data-dir=/tmp/cards --window-size=1200,630 --virtual-time-budget=8000 --screenshot=card-he.png "file://$PWD/card.html?lang=he"

Change `he` to `en` for the English card. If Chrome does not return after the file appears, press Control + C.

## A new card

Add a line to `CARDS` in `card.html`, for example `answers_he: { name: '...', line: '...', dir: 'rtl' }`, and make it with `?lang=answers_he`.
