# Terms

## The licence

NovelForge is released under the MIT Licence. The full text is in
[LICENSE](LICENSE). In short: you may use, copy, modify, merge, publish,
distribute, sublicense, and sell copies, provided the copyright notice and licence
text travel with them.

Copyright (c) 2026 ShinZero.

## What you are licensing

The plugin's own material: the skills, templates, commands, images, scripts, hook,
and documentation in this repository.

## What you are not licensing

**Your novel.** Anything NovelForge writes or that you write using it is yours. The
plugin claims no rights over your work, and the skills instruct agents to keep canon
in your project files precisely so that your novel remains your own, in your format,
on your disk.

## Third-party material

None is vendored. All content in this repository is original to it, apart from the
MIT Licence text itself. The repository's own dependencies are Python's standard
library, plus Pillow for one optional validator check, and GitHub Actions for CI.
Installing skills through a registry such as [skills.sh](https://skills.sh) brings
that registry's terms into play for the installer, not for this licence.

## No warranty

The software is provided "as is", without warranty of any kind, as stated in the
MIT Licence. In practice: the skills are instruction files that shape how an AI model
writes, and no validator can prove a skill's instructions are *useful*. They can only
prove they are structurally sound.

Run the validator before trusting a change:

```bash
python3 scripts/validate.py --schema --strict
```

## Contributions

Contributions are accepted under the same MIT Licence. See
[CONTRIBUTING.md](CONTRIBUTING.md). If you contribute a skill, you are agreeing to
license it under MIT.

## Security

Report vulnerabilities through
<https://github.com/20Youssef10/NovelForge/issues>, or privately to the maintainer
at <https://github.com/20Youssef10>.

The plugin executes one script, `hooks/session_start.py`, described in
[PRIVACY.md](PRIVACY.md). It is worth reading before installing.