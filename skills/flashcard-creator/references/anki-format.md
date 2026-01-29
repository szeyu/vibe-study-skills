# Anki Import Format Reference

Complete specification for Anki-compatible export formats.

## Basic Import Format

Anki expects **tab-separated values** in a `.txt` file.

### Minimum Format
```
Front	Back
```

### With Tags
```
Front	Back	tag1::subtag tag2
```

### With Deck
Use filename or import into specific deck via Anki UI.

---

## Field Separator Options

| Separator | Use Case |
|-----------|----------|
| Tab (`\t`) | Default, most reliable |
| Semicolon | Alternative if tabs problematic |
| Comma | Avoid (content often has commas) |

---

## Cloze Deletion Syntax

### Single Cloze
```
{{c1::hidden text}}
```

### Multiple Clozes (Shown Together)
```
The {{c1::mitochondria}} produces {{c1::ATP}}.
```
Both revealed at same time.

### Multiple Clozes (Separate Cards)
```
The {{c1::mitochondria}} produces {{c2::ATP}}.
```
Creates 2 cards - one hiding each item.

### Cloze with Hint
```
{{c1::mitochondria::cellular organelle}}
```
Shows "cellular organelle" as hint.

---

## HTML in Cards

Anki supports HTML:

```
Front: What is <b>photosynthesis</b>?
Back: The process where plants convert <span style="color:green">sunlight</span> to energy.
```

### Useful HTML Tags
- `<b>bold</b>` - emphasis
- `<i>italic</i>` - terms
- `<br>` - line breaks
- `<ul><li>` - lists
- `<img src="">` - images

---

## Media References

Images in Anki:
```
<img src="image.jpg">
```

Place media files in Anki's `collection.media` folder.

---

## Import Settings in Anki

When importing:
1. **File → Import**
2. Select `.txt` file
3. Set:
   - Type: "Basic" or "Cloze"
   - Deck: Target deck
   - Field separator: Tab
   - Allow HTML: Yes (if using formatting)
