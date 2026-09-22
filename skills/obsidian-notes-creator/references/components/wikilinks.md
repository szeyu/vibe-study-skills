# Wikilinks and Embeds

```markdown
[[Note]]
[[Note|Readable label]]
[[Note#Heading]]
[[#Heading in this note]]
[[Note#^block-id]]
![[Note#Heading]]
![[assets/figure.svg|640]]
```

Use links for prerequisites, related reasoning, and follow-up material. Give the connection in a few words when it is not obvious. Do not invent a prerequisite or force a Related section simply to meet a link quota.

## Resolution checks

- Resolve against the actual vault root and current note location. Check path-qualified targets and assets, not just basenames.
- If multiple notes share a basename, use enough of the path to identify the intended file. A bare `[[README]]` is risky in a multi-subject vault.
- Check that referenced headings and block IDs actually exist. Preserve stable anchors when editing headings.
- In Markdown table cells, escape the alias separator: `[[Note\|Label]]`.
- Check regular Markdown links and image embeds as well as wikilinks. Ignore illustrative syntax inside code examples when auditing actual dependencies.
- If an authorised rename is necessary, update incoming links and embeds too; do not rename as a cosmetic cleanup.

Use section embeds for genuinely shared material. Avoid making readers jump among many files to follow one calculation, or transcluding entire notes where a concise link would suffice.
