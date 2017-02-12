# my-papers

My list of publications + formatting script.

Just run `make` to get formatted `index.html`.

The input is in the `.txt` files, and these files are listed in the beginning
of the script. The record format is simple:

authors,title,source,link,link to pdf

These fields are separated by one empty line, and records are separated by two
empty lines. The link, and link to pdf, fields are optional. All formatting is
specified by inline CSS in `1-top.html`, so you get one standalone html file.

If you'd like to use these scripts, you can under the BSD 2-clause license.
