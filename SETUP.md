# Cursor setup for Production RAG

Extract this package at the root of the `production-rag` repository.

Expected structure:

```text
production-rag/
|-- .cursor/
|   `-- rules/
|       |-- 00-project-context.mdc
|       |-- 10-roadmap-executor.mdc
|       `-- 20-git-autocommit.mdc
`-- ROADMAP.md
```

Then open the repository root in Cursor and start a new Agent chat.

Recommended first prompt:

```text
Read ROADMAP.md and the project rules. Validate P1.00 against the current repository. If its Definition of Done is already satisfied, mark only P1.00 as complete, validate the repository, and create the automatic commit according to the Git rule. If it is not satisfied, complete only P1.00. Do not start P1.01.
```

After that, for each step you can use:

```text
Execute the next unchecked roadmap task only. Follow its Definition of Done, validate it, update ROADMAP.md, and create the automatic commit. Do not push and do not start the following task.
```
