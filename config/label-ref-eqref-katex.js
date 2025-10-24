trust: (context) => ['\\htmlId', '\\href'].includes(context.command),
macros: {
  "\\eqref": "\\href{###1}{(\\text{#1})}",
  "\\ref": "\\href{###1}{\\text{#1}}",
  "\\label": "\\htmlId{#1}{}"
}
