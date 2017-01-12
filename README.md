# yangling

Help for wrangling the yelp academic dataset

Important: this is a pretty hacky collection of scripts used for some *very*
specific research purposes. They might be helpful, but you probably don't
want to treat these as a general solution for anything :)

## Using and Dependencies

You need:

* dmk (which requires Go)
* Python 3
* unidecode

You should install Go and Python 3 the "normal" way for your OS (and why
didn't you already have them installed?!)

`dmk` can be installed with: `go get -u github.com/CraigKelly/dmk`

You can install unidecode locallly: `pip3 install --user unidecode`

Once you have everything working, just running `dmk` should be sufficient. The
scripts assume that you've extracted the yelp academic dataset to this
directory.
