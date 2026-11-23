// AISP shown in its own notation. Every code line is copied verbatim from AI_GUIDE.md, the AISP 5.1
// specification in github.com/bar181/aisp-open-core (MIT licence, read 22 November 2026); ";; …" marks
// lines left out. The plain readings are ours. Only the notation and foundation of the open core
// appear here, never its deeper mechanisms, and nothing beyond the open core.

export const aispSource = { href: "https://github.com/bar181/aisp-open-core/blob/main/AI_GUIDE.md", label: "AI_GUIDE.md, the AISP 5.1 specification" };

export type Excerpt = {
  id: string;
  title: string;
  text: string;
  code: string[];
  reading: { code: string; plain: string }[];
};

export const aispIntro = {
  heading: "AISP, in its own notation",
  lead: "AISP adds no new symbols. Its 512 come from formal logic, type theory and category theory, the notation of mathematics papers and of proof languages such as Lean, Coq and TLA+. The AISP paper argues that frontier models have already learned these symbols from that literature, so AISP only fixes one grammar over them: every well-formed document parses one way, with no fine-tuning.",
  sigma: { big: "Σ₅₁₂", text: "512 symbols in eight categories of 64, each pinned to its meaning in the glossary." },
  categories: [
    { glyph: "Ω", name: "Transmuters", range: "0 to 63", role: "transform, derive, prove" },
    { glyph: "Γ", name: "Topologics", range: "64 to 127", role: "structure, shape, relation" },
    { glyph: "∀", name: "Quantifiers", range: "128 to 191", role: "scope, range, extent" },
    { glyph: "Δ", name: "Contractors", range: "192 to 255", role: "binding, state, contract" },
    { glyph: "𝔻", name: "Domains", range: "256 to 319", role: "types and their domains" },
    { glyph: "Ψ", name: "Intents", range: "320 to 383", role: "intent and scoring" },
    { glyph: "⟦⟧", name: "Delimiters", range: "384 to 447", role: "blocks and structure" },
    { glyph: "∅", name: "Reserved", range: "448 to 511", role: "operators" },
  ],
  proofLine: "In a blind pilot, Gemini and GPT-5.5 each read three AISP documents cold, with no glossary, and recovered every decision point. One run per model.",
};

export const foundation: Excerpt = {
  id: "foundation",
  title: "One reading, by definition",
  text: "The specification opens by defining ambiguity and setting its bound. Every document then follows one block order, ending in its own evidence.",
  code: ["⟦Ω:Foundation⟧{", "  ;; …", "  ∀D∈AISP:Ambig(D)<0.02", "  Ambig≜λD.1-|Parse_u(D)|/|Parse_t(D)|", "  Doc≜𝔸≫CTX?≫⟦Ω⟧≫⟦Σ⟧≫⟦Γ⟧≫⟦Λ⟧≫⟦Χ⟧?≫⟦Ε⟧", "}"],
  reading: [
    { code: "∀D∈AISP:Ambig(D)<0.02", plain: "The specification requires every AISP document to have an ambiguity below 2%." },
    { code: "Ambig≜λD.1-|Parse_u(D)|/|Parse_t(D)|", plain: "Ambiguity is defined as one minus the share of a document's parses that are unique." },
    { code: "Doc≜𝔸≫CTX?≫⟦Ω⟧≫…≫⟦Ε⟧", plain: "A document runs header, context, foundation, types, rules, functions, errors, and closes with evidence." },
  ],
};

export const glossary: Excerpt = {
  id: "glossary",
  title: "The 512 symbols",
  text: "The glossary fixes the eight category ranges and pins each symbol to its meaning.",
  code: ["⟦Σ:Glossary⟧{", "  ;; …", "  R≜{Ω:[0,63],Γ:[64,127],∀:[128,191],Δ:[192,255],𝔻:[256,319],Ψ:[320,383],⟦⟧:[384,447],∅:[448,511]}", "  ;; …", "  ℙ(⊤,top∨true); ℙ(⊥,bottom∨false∨crash); ℙ(⊢,proves); ℙ(⊨,models); ℙ(≜,defas); ℙ(≔,assign); ℙ(λ,lambda); ℙ(μ,lfp); ℙ(fix,Y); ℙ(∎,QED)", "  ;; …", "}"],
  reading: [
    { code: "R≜{Ω:[0,63],…,∅:[448,511]}", plain: "Eight categories, 64 symbols each, in fixed ranges." },
    { code: "ℙ(⊢,proves); ℙ(∎,QED)", plain: "Each symbol is bound to its meaning: ⊢ is proves, ∎ ends a proof." },
  ],
};
