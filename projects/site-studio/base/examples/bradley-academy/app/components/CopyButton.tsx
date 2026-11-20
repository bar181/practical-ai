import { useState } from "react";

/** Copies text, then says so in words. Works without script as a plain disabled-looking button. */
export function CopyButton({ text, label, className = "btn btn-primary" }: { text: string; label: string; className?: string }) {
  const [state, setState] = useState<"idle" | "done" | "failed">("idle");
  async function copy() {
    try {
      await navigator.clipboard.writeText(text);
      setState("done");
    } catch {
      setState("failed");
    }
    window.setTimeout(() => setState("idle"), 2400);
  }
  return (
    <button type="button" className={className} onClick={copy}>
      <span aria-live="polite">{state === "done" ? "Copied. Paste it into your chatbot" : state === "failed" ? "Select the text and copy it" : label}</span>
    </button>
  );
}
