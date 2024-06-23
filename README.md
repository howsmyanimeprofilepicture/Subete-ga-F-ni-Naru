# kakarot

![alt text](assets/kakarot.png)

Functools-like Library

## Install

```
pip install git+https://github.com/howsmyanimeprofilepicture/kakarot
```

## Example

```python
>>> import kakarot
>>> super_saiyans = ["Son Goku", "Vegeta", "Trunks"]
>>> ops = kakarot.Sequential(
...     kakarot.map(lambda x: x + " ちゃん"),
...     kakarot.reduce(lambda x, y: x+" 🎈 "+y)
... )
>>> ops(super_saiyans)
'Son Goku ちゃん 🎈 Vegeta ちゃん 🎈 Trunks ちゃん'
```