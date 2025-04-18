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
Then you can directly use `- file: notebooks/analysis` in your `docs/_toc.yml`.

### Refresh all html file

Run the following command:
```
poetry run jupyter-book build docs/ --all
```

### Git工作流

Create you own branch for development
```
git checkout -b feature/<new-feature-name>
# After make modification on your branch
git add .
git commit -m "Describe your change"
git push origin feature/<new-feature-name>
```

When you finish your code, there are two approaches:

+ Method one: Make a Pull Request on Github, when you get the permit, click "Merge Pull Request".

+ Method two: Use command line
```
git checkout main
git merge feature/<new-feature-name>
git push origin main
```

#### In case you made modification on your main branch code

Stash your changes
```
git stash push -m "temporary stash" 
```

Switch to feature branch
```
git checkout existing-feature-branch-name
```
or 
```
git checkout -b new-feature-branch-name
```

Apply the stashed changes
```
git stash pop
```

### Prior Estimator

The investor's prior beliefs about assets' return and covariance.

Popular Prior:
+ [Empirical](notebooks/empirical_estimation.ipynb)
+ [Black & Litterman](notebooks/black_litterman.ipynb)
+ [Factor Model](notebooks/factor_model.ipynb)
