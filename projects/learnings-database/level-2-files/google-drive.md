# Keeping the log in Google Sheets

The log can be a Google Sheet. What the assistant can do with it depends on the chatbot and the
plan, as checked on 19 November 2026. **None of these routes has been tried for this project yet.**

| Chatbot | Reads the sheet | Adds a row itself |
| --- | --- | --- |
| ChatGPT, paid plans, with the Google Drive app connected | Yes | Yes, after your yes in the chat |
| ChatGPT, free plan | No connections on free plans | No: use a project file or upload |
| Claude, with the Google Drive connector | Yes, as a CSV export | No: it gives the row to paste. Claude for Google Workspace, inside the sheet, on paid plans, can work in the sheet itself |
| Any chatbot with the level 3 database | Through the MCP tools | Yes, as "proposed" |

## Set up

1. Upload [`learnings.xlsx`](../base/template/learnings.xlsx) to Google Drive and open it with
   Google Sheets (**File > Save as Google Sheets**). Keep the three tabs.
2. Delete the twelve invented rows on the Learnings tab, and put your own projects on the Lists tab.
3. In ChatGPT: connect the Google Drive app in settings, then in a chat say which sheet is your log:
   "My learnings log is the Google Sheet named Learnings." In Claude: connect Google Drive in
   settings and add the sheet to the project or the chat.
4. Use the skill as usual. When it can write, it shows the row and asks "Add it to Learnings?"
   before adding anything. It adds rows at the bottom and changes no other row.

**Keep the sheet private** unless your team shares the log, and keep rows marked `sensitive = yes`
out of anything you paste elsewhere; the skill does this for you.
