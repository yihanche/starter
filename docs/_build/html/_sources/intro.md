# Welcome to your Jupyter Book

This is a small sample book to give you a feel for how book content is
structured.
It shows off a few of the major file types, as well as some sample content.
It does not go in-depth into any particular topic - check out [the Jupyter Book documentation](https://jupyterbook.org) for more information.

Check out the content pages bundled with this sample book to see more.

```{tableofcontents}
```

## Learning Notes

### 符号连接
To use jupyter notebooks directly from an upper directory, we need to create a symlink to connect, such that it can be recognized:
```
cd docs/
ln -s ../notebooks ./notebooks
```
Then you can directly use `notebooks/analysis` in your docs/_toc.yml

### Refresh all html file

Run the following command:
```
poetry run jupyter-book build docs/ --all
```
