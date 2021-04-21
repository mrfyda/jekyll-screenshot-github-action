# mkdocs-preview-action

Takes a screenshot of your MkDocs changes and comment the screenshots on the pull request.

## Example workflow

This workflow stores your screenshot as a build artifact:

```yaml
name: mkdocs preview

on: pull_request

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
    - uses: actions/checkout@master
    - uses: mrfyda/jekyll-screenshot-github-action@master
    - uses: actions/upload-artifact@v1
      with:
        name: screenshot
        path: /home/runner/work/_temp/_github_home/screenshot.png
```
