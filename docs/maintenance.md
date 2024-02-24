# How to update Bootstrap
- Download Bootstrap into `core\static`
- Within `core\static` softlink `bootstrap` to the new version, e.g.: `bootstrap-9-9-9`
- Collect statics in Django: `python manage.py collectstatic`
- Check the paths in the `*.html` templates (mainly `base.html`) are correct.

# [How to revert all local changes in Git project to previous state?](https://stackoverflow.com/questions/1146973/how-do-i-revert-all-local-changes-in-git-managed-project-to-previous-state)
- If you want to revert changes made to your working copy, do this:
`git checkout .`

- If you want to revert changes made to the index (i.e., that you have added), do this. Warning this will reset all of your unpushed commits to master!:
`git reset`

- If you want to revert a change that you have committed, do this:
`git revert <commit 1> <commit 2>`

- If you want to remove untracked files (e.g., new files, generated files):
`git clean -f`

- Or untracked directories (e.g., new or automatically generated directories):
`git clean -fd`
