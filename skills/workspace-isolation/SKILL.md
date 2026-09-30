---
name: workspace-isolation
description: Deprecated alias retained for backwards compatibility. Project registries, namespace resolution, active-project selection, and cross-novel isolation now live in workspace-manager; route all workspace work there.
---
# Multi-Novel Workspace Isolation (deprecated alias)

This skill has been merged into `workspace-manager`, which owns the WORKSPACE → NOVEL → BRANCH namespace model, the project registry, active-project selection, switching protocol, and cross-novel isolation rules.

**Route all workspace and isolation work to `workspace-manager`.**

Kept in place so that existing projects, prompts, and command references that invoke `workspace-isolation` continue to resolve rather than failing. It carries no independent behaviour; the records in `workspace/` are shared.

The isolation guarantee is unchanged: never retrieve another novel's canon, characters, terminology, plot, or research on the basis of similarity alone. Cross-novel reuse requires explicit author instruction.
