import { CopyButton } from "./CopyButton";

/** A prompt to paste into a chatbot: the card, the words, and one copy button. */
export function PromptCard({ prompt, label, id }: { prompt: string; label: string; id?: string }) {
  return (
    <figure className="prompt" id={id}>
      <figcaption className="prompt-bar">
        <span>Paste into Claude, ChatGPT or Gemini</span>
      </figcaption>
      <pre tabIndex={0}><code>{prompt}</code></pre>
      <div className="prompt-actions">
        <CopyButton text={prompt} label={label} />
      </div>
    </figure>
  );
}
