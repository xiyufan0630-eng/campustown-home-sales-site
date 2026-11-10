# Agent log

Add a dated entry each time you work with your AI coding agent, with the newest entry at the bottom. Each entry records what you asked the agent, what it produced, and what you checked or changed. Paste your key prompts in exactly as you typed them. Include at least one time the agent got something wrong, and how you caught it.

Copy this outline for each entry:

```markdown
## YYYY-MM-DD: What you worked on

- **Asked:** "Paste your prompt here."
- **Agent produced:** What it made or changed.
- **Checked or changed:** How you checked it, and what you fixed.
```

## 2026-11-10: Median sale price bar chart on index.html

- **Asked:** "Read AGENTS.md and docs/data_description_sheet.md first. Then add a horizontal bar chart of the median sale price for each city above the table on index.html. Keep the table and the $10,000 rule as they are."
- **Agent produced:** `scripts/city_median_sale_price.py`, which computes each city's median sale price from the CSV with sales under $10,000 left out, and writes `data/city_median_sale_price.json`. `index.html` now shows a horizontal bar chart of those medians, with the page's placeholder text replaced.
- **Checked or changed:** The request said to keep an existing table and $10,000 rule, but the repository had neither. The chart was built with the $10,000 rule applied. Medians for the 14 cities listed in the description sheet match it, apart from small differences from the sheet's $1,000 threshold. Rendered at desktop and phone widths; fixed overlapping axis labels and truncated city names on the phone.
