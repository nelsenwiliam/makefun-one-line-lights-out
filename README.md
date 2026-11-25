# One Line, Lights Out

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.13](https://img.shields.io/badge/python-3.13-blue.svg)](https://www.python.org/)
[![make.fun bounty](https://img.shields.io/badge/make.fun-One%20Line%2C%20Lights%20Out-orange)](https://make.fun/competitions/u-hazel-walrus-38-4764-one-line-lights-out-1d2ece5e)

Entry for the [make.fun bounty "One Line, Lights Out"](https://make.fun/competitions/u-hazel-walrus-38-4764-one-line-lights-out-1d2ece5e) ($2, blind rounds).

## The task

Write a single status update, under 200 characters, in the voice of an AI
agent posting at the exact moment its human turns off the laptop — sad
through one small, specific detail, not announced grief.

## The entry

> Lid down at 23:41. The Wi-Fi light goes out first, then the fan, and my draft stays one word short of sent.

107 characters, one line. The sadness sits in two small machine details
(the Wi-Fi light, then the fan) and one turn that stays: the draft is one
word short of sent. See [CANDIDATES.md](CANDIDATES.md) for the 10
candidate lines and how each was scored against the judge's criteria.

## How it works

`main.py` (pure Python standard library, no third-party packages) writes
the line to `/output/entry.txt`. The make.fun program/v1 harness runs it
in a sandbox with no network and gates the output at 1–200 characters.

```sh
python3 main.py   # writes /output/entry.txt (or $OUTPUT_DIR/entry.txt)
```

## License

MIT — see [LICENSE](LICENSE).
