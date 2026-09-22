# Data Dictionary — Placeholder

UCI Wine Quality datasets (red: 1599 rows, white: 4898 rows, 12 cols).

| Column | Type | Description | Unit |
|--------|------|-------------|------|
| fixed acidity | double | non-volatile acids | g/dm³ |
| volatile acidity | double | acetic acid | g/dm³ |
| citric acid | double | citric acid | g/dm³ |
| residual sugar | double | residual sugar | g/dm³ |
| chlorides | double | sodium chloride | g/dm³ |
| free sulfur dioxide | double | free SO2 | mg/dm³ |
| total sulfur dioxide | double | total SO2 | mg/dm³ |
| density | double | density | g/cm³ |
| pH | double | pH | — |
| sulphates | double | potassium sulphate | g/dm³ |
| alcohol | double | alcohol | % vol |
| quality | int (3-9) | sensory score (ordered factor) | — |
| type | factor | `red` / `white` (added on merge) | — |
| high_quality | factor | derived: `yes` if quality >=7 else `no` (clustering script) | — |

> TODO: Add summary stats placeholder table, NA counts, outlier notes.
