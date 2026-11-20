import { CopyButton } from "./CopyButton";

/** A prompt to paste into a chatbot: one copy button first, then the words, folded away when long. */
export function PromptCard({ prompt, label, id }: { prompt: string; label: string; id?: string }) {
  const lines = prompt.split("\n").length;
  const long = lines > 14;
  const body = <pre tabIndex={0}><code>{prompt}</code></pre>;
  return (
    <figure className="prompt" id={id}>
      <figcaption className="prompt-bar">
        <span>Paste into Claude, ChatGPT or Gemini</span>
      </figcaption>
      <div className="prompt-actions">
        <CopyButton text={prompt} label={label} />
      </div>
      {long ? (
        <details className="prompt-more">
          <summary>Read the whole prompt ({lines} lines) before you copy it</summary>
          {body}
        </details>
      ) : body}
    </figure>
  );
}
