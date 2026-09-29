# dorithkleinstein.com

The source of dorithkleinstein.com. GitHub Pages builds it with Jekyll.

## Where things are

- `index.md` is the Hebrew home page. `en/index.md` is the English one.
- `_articles/he/` holds Hebrew articles. `_articles/en/` holds English ones.
- `_data/ui.yml` holds the small fixed words: the name, the link headings, the notes about English.
- `_config.yml` holds the email address and the Looker Studio and GitHub links.

## Adding an article

Make a new file in `_articles/he/` or `_articles/en/`. The file name becomes the address:
`_articles/en/the-measuring-stick.md` appears at `/en/articles/the-measuring-stick/`.

Start the file with:

    ---
    ref: the-measuring-stick
    order: 5
    title: 'The measuring stick'
    description: 'One sentence for the i hint in the site map and for Facebook.'
    ---

When a Hebrew and an English article share the same `ref`, each links to the other at the top of the page.

`order` sets the article's place in the site map at the bottom of every page.

Add `looker: true` and/or `github: true` to show the Looker Studio report and the GitHub repository at the end of the article.
