# Commercial grade: what a commercial build adds

This folder explains. It never holds a project.

## What changes

| Area | In this repository | In a commercial build |
| --- | --- | --- |
| Environments | One site | Separate test and live sites, each with its own address |
| Access | Public, or a shared link | Sign-in, roles, and private areas for clients |
| Safety | You can delete the project | Backups, monitoring, and a rehearsed way to roll back |
| Review | One person approves | Named approvers, with security and accessibility checks on every change |
| Record | The repository history | An audit trail of who published what, and when |

## What does not change

- No invented facts.
- A person approves anything that goes out.

## Signs you have outgrown the levels here

- A page went live that nobody remembers approving
- A client saw another client's page
- The site went down and nobody knew for a day
