import { useState } from "react";

const chatbots = [
  { href: "https://claude.ai/new", label: "Claude" },
  { href: "https://chatgpt.com/", label: "ChatGPT" },
  { href: "https://gemini.google.com/app", label: "Gemini" },
];

/** Copies text, says so in a live region, then offers the next step: open a chatbot to paste it into. */
export function CopyButton({ text, label, className = "btn btn-light", next = true }: { text: string; label: string; className?: string; next?: boolean }) {
  const [state, setState] = useState<"idle" | "done" | "failed">("idle");
  async function copy() {
    try {
      await navigator.clipboard.writeText(text);
      setState("done");
    } catch {
      setState("failed");
    }
  }
  return (
    <span className="copy js-only">
      <button type="button" className={className} onClick={copy}>
        {state === "done" ? "Copied" : label}
      </button>
      <span className="copy-status" role="status">
        {state === "done" && next ? (
          <>
            Copied. Now paste it into{" "}
            {chatbots.map((c, i) => (
              <span key={c.href}>
                <a href={c.href} target="_blank" rel="noopener">{c.label}<span className="sr-only"> (opens a new tab)</span></a>
                {i < chatbots.length - 2 ? ", " : i === chatbots.length - 2 ? " or " : "."}
              </span>
            ))}
          </>
        ) : state === "done" ? "Copied." : state === "failed" ? "Your browser blocked copying. Select the prompt text and copy it." : ""}
      </span>
    </span>
  );
}
