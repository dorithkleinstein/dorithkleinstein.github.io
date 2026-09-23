# dorithkleinstein.com

The source of dorithkleinstein.com. GitHub Pages builds it with Jekyll.

## Where things are

- `index.md` is the Hebrew home page. `en/index.md` is the English one.
- `_articles/he/` holds Hebrew articles. `_articles/en/` holds English ones.
- `_data/ui.yml` holds the small fixed words: the name, section headings, month names.
- `_config.yml` holds the email address and the Looker Studio and GitHub links.

## Adding an article

Make a new file in `_articles/he/` or `_articles/en/`. The file name becomes the address:
`_articles/en/the-measuring-stick.md` appears at `/en/articles/the-measuring-stick/`.

Start the file with:

    ---
    ref: the-measuring-stick
    title: The measuring stick
    date: 2026-10-01
    description: One sentence for the list of articles and for Facebook.
    ---

When a Hebrew and an English article share the same `ref`, each links to the other at the top of the page.
