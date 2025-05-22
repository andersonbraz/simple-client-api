# Desafios

## Agregação

```sql
SELECT organization, language, count(*) as counter FROM data WHERE organization = 'AWS' GROUP BY organization, language;
```