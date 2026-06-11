# Wikilinks & Embeds Reference

---

## Basic Link Forms

```markdown
[[Note Name]]                    Link to a note by name
[[Note Name|Display Text]]       Link with custom label
[[Note Name#Heading]]            Link to a specific heading
[[Note Name#Heading|Label]]      Link to heading with custom label
[[#Heading in same note]]        Anchor link within the same note
[[Note Name#^block-id]]          Link to a specific block
```

---

## Embeds (Inline Transclusion)

```markdown
![[Note Name]]                   Embed entire note
![[Note Name#Heading]]           Embed from a heading downward
![[Note Name#^block-id]]         Embed a single block
![[image.png]]                   Embed an image
![[image.png|300]]               Embed image at 300px width
```

---

## Block References

Add a block ID at the end of a paragraph to make it linkable:

```markdown
The momentum encoder update ensures consistency across queue entries. ^moco-momentum

Then link to it elsewhere:
See [[19-self-supervised-learning#^moco-momentum]]
```

---

## When to Add Wikilinks

| Situation | Do this |
|---|---|
| Mentioning a concept covered in another note | `[[note-name\|concept name]]` |
| Referencing a prerequisite at the top | List under **Prerequisites:** heading |
| Referencing follow-up material | List under **Related:** heading |
| Embedding a shared diagram or table | `![[shared-note#diagram-section]]` |

---

## Linking Strategy for Study Notes

Every note should have at minimum:

```markdown
**Prerequisites:** [[prior-concept]] — why you need it
**See also:** [[related-technique]] — where this leads
```

And a **Related** section at the bottom:
```markdown
## Related

- [[prior-concept]] — foundation for this topic
- [[next-concept]] — builds on this
- [[example-note]] — worked examples
```

---

## Path Resolution

Obsidian resolves links by note name, not file path.
You don't need to write the full path — just the filename (without `.md`):

```markdown
[[19-self-supervised-learning]]       ✓ works
[[UM/CV/concepts/19-self-supervised-learning]]  ✓ also works (explicit)
```

Use explicit paths only when two notes share the same name.
