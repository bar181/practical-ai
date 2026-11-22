// AISP shown in its own notation. Every code line is copied verbatim from AI_GUIDE.md, the AISP 5.1
// specification in github.com/bar181/aisp-open-core (MIT licence, read 22 November 2026); ";; …" marks
// lines left out. The plain readings are ours. Only the open core appears here: the commercial-grade
// AISP is named, never shown (Bradley's decision, 22 November 2026).

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
  code: ["⟦Σ:Glossary⟧{", "  ;; …", "  R≜{Ω:[0,63],Γ:[64,127],∀:[128,191],Δ:[192,255],𝔻:[256,319],Ψ:[320,383],⟦⟧:[384,447],∅:[448,511]}", "  ;; …", "  ℙ(⊤,top∨true); ℙ(⊥,bottom∨false∨crash); ℙ(⊢,proves); ℙ(⊨,models); ℙ(≜,defas); ℙ(≔,assign); ℙ(λ,lambda); ℙ(μ,lfp); ℙ(fix,Y); ℙ(∎,QED)", "  ;; …", "  ℙ(∅,empty∨null); ℙ(𝒫,pocket∨powerset); ℙ(ε,epsilon∨threshold); ℙ(δ,delta∨density); ℙ(τ,tau∨threshold); ℙ(φ,phi∨completeness); ℙ(ψ,psi∨intent)", "  ;; …", "}"],
  reading: [
    { code: "R≜{Ω:[0,63],…,∅:[448,511]}", plain: "Eight categories, 64 symbols each, in fixed ranges." },
    { code: "ℙ(⊢,proves); ℙ(∎,QED)", plain: "Each symbol is bound to its meaning: ⊢ is proves, ∎ ends a proof." },
  ],
};

export const advanced: Excerpt[] = [
  {
    id: "binding",
    title: "Components that bind exactly one way",
    text: "When two components meet, the binding function returns one of four states. The specification's proof block states that it returns exactly one.",
    code: ["⟦Γ:Binding⟧{", "  Δ⊗λ≜λ(A,B).case[", "    Logic(A)∩Logic(B)⇒⊥ → 0,", "    Sock(A)∩Sock(B)≡∅   → 1,", "    Type(A)≠Type(B)     → 2,", "    Post(A)⊆Pre(B)      → 3", "  ]", "  ∀A,B:|{Δ⊗λ(A,B)}|≡1", "  ;; …", "}", "", "⟦Θ:Proofs⟧{", "  ;; …", "  ∴∀A,B:|{Δ⊗λ(A,B)}|≡1", "  π:cases exhaustive∧disjoint;exactly one∎", "  ;; …", "}"],
    reading: [
      { code: "→ 0 … → 3", plain: "Contradictory logic crashes (0), no shared socket gives null (1), different types adapt (2), and when A's post-conditions fall within B's pre-conditions, the join costs nothing (3)." },
      { code: "∀A,B:|{Δ⊗λ(A,B)}|≡1", plain: "For any pair A and B, the function gives exactly one result." },
      { code: "π:cases exhaustive∧disjoint;exactly one∎", plain: "The proof given: the cases are exhaustive and disjoint, so exactly one applies." },
    ],
  },
  {
    id: "pocket",
    title: "The Pocket architecture",
    text: "Knowledge is kept in pockets: a header, a membrane that learning updates, and a nucleus whose hash is the pocket's identity.",
    code: ["⟦Γ:Pocket⟧{", "  𝒫≜⟨ℋ:Header,ℳ:Membrane,𝒩:Nucleus⟩", "  ;; …", "  𝒩≜⟨def:AISP,ir:LLVM,wa:WASM,σ:Sig⟩", "  ;; Immutability Physics", "  ∀p:∂𝒩(p)⇒∂ℋ.id(p)", "  ∀p:∂ℳ(p)⇏∂ℋ.id(p)", "  ∀p:ℋ.id(p)≡SHA256(𝒩(p))", "  ;; …", "}"],
    reading: [
      { code: "𝒫≜⟨ℋ:Header,ℳ:Membrane,𝒩:Nucleus⟩", plain: "A pocket is a header, a membrane and a nucleus." },
      { code: "𝒩≜⟨def:AISP,ir:LLVM,wa:WASM,σ:Sig⟩", plain: "The nucleus holds the definition in AISP, LLVM and WebAssembly forms, and a signature." },
      { code: "∀p:∂𝒩(p)⇒∂ℋ.id(p)", plain: "Changing the nucleus changes the pocket's ID." },
      { code: "∀p:ℋ.id(p)≡SHA256(𝒩(p))", plain: "The ID is the SHA-256 hash of the nucleus." },
      { code: "∀p:∂ℳ(p)⇏∂ℋ.id(p)", plain: "Changing the membrane, where learning is recorded, does not change the ID." },
    ],
  },
  {
    id: "learning",
    title: "Learning from every success and failure",
    text: "The membrane records an affinity between pockets. Each success raises it by 1 and each failure lowers it by 10.",
    code: ["⟦Γ:Learning⟧{", "  α≜0.1; β≜0.05; τ_v≜0.7; τ_s≜90d", "  ⊕(A,B)⇒ℳ.aff[A,B]+=1", "  ⊖(A,B)⇒ℳ.aff[A,B]-=10", "  ℳ.aff[A,B]<τ_v⇒skip(B)", "  ;; …", "  Age(p)>τ_s∧Ref(p)≡0⇒Evict(p)", "}"],
    reading: [
      { code: "⊕(A,B)⇒ℳ.aff[A,B]+=1", plain: "A success from A to B adds 1 to their affinity." },
      { code: "⊖(A,B)⇒ℳ.aff[A,B]-=10", plain: "A failure subtracts 10." },
      { code: "ℳ.aff[A,B]<τ_v⇒skip(B)", plain: "Below the threshold τ_v (0.7), B is skipped." },
      { code: "Age(p)>τ_s∧Ref(p)≡0⇒Evict(p)", plain: "A pocket older than τ_s (90 days) with no references is evicted." },
    ],
  },
  {
    id: "search",
    title: "Searching on the gap",
    text: "The search works on the ghost: the gap between the target intent and what a beam already has.",
    code: ["⟦Γ:Search⟧{", "  ;; …", "  ;; Ghost Physics", "  ∀b:ψ_g(b)≡ψ_*⊖ψ_have(b.G)", "  ;; …", "  ∀b:|⊞(ℛ,ψ_g(b))|≡0⇒✂(b)", "  ;; …", "  ;; Safety Gate", "  ∀b:μ_r(b)>τ⇒✂(b)", "  ;; …", "  ;; Convergence", "  done(B)⇔(∀b∈B:ψ_g(b)≡∅)∨(t>T)", "}"],
    reading: [
      { code: "ψ_g(b)≡ψ_*⊖ψ_have(b.G)", plain: "For each beam, the ghost is the target minus what the beam already has." },
      { code: "|⊞(ℛ,ψ_g(b))|≡0⇒✂(b)", plain: "If a scan of the registry finds nothing for the ghost, the beam is pruned." },
      { code: "μ_r(b)>τ⇒✂(b)", plain: "A beam whose risk is above the threshold is pruned: the safety gate." },
      { code: "done(B)⇔(∀b∈B:ψ_g(b)≡∅)∨(t>T)", plain: "The search ends when every ghost is empty, or time runs out." },
    ],
  },
];

export const evidenceBlock: Excerpt = {
  id: "evidence",
  title: "Every document carries its evidence",
  text: "The specification ends the way every AISP document ends: with an evidence block stating its density, its tier and what it asserts.",
  code: ["⟦Ε⟧⟨", "δ≜0.81", "|𝔅|≜18/18", "φ≜98", "τ≜◊⁺⁺", "⊢ND", "⊢CAT:𝔽,𝔾,η,ζ,ε⊣ρ,𝕄_val", "⊢ΠΣ:Vec,Fin,𝕍,𝔻oc", "⊢𝕃:𝕃₀(Signal),𝕃₁(Pocket),𝕃₂(Search)", "⊢μ:fix,opt_δ,learn,gen,prove,refine,bridge", "⊢Θ:T₁₋₁₄∎", "⊢Σ_512:8cat×64sym,R,ℙ", "⊢Γ:Inference[12rules]", "⊢Χ:Errors[11typed]", "⊢Grammar:Doc,Block,Expr,Prec,Assoc", "⊢Template:Minimal,Full", "⊢Rosetta:Prose↔Code↔AISP", "⊢Agent:Enforce,AntiDrift,NorthStar", "⊢Ambig<0.02", "⟩"],
  reading: [
    { code: "δ≜0.81 … τ≜◊⁺⁺", plain: "Semantic density 0.81, which earns the top tier, ◊⁺⁺ (0.75 or more)." },
    { code: "⊢𝕃:𝕃₀(Signal),𝕃₁(Pocket),𝕃₂(Search)", plain: "It asserts its three layers: signal, pocket and search." },
    { code: "⊢Ambig<0.02", plain: "It asserts its own ambiguity bound." },
  ],
};

export const commercial = {
  heading: "Open core, and the commercial grade",
  text: "Everything shown here is from the open core, MIT licensed and free to use. Research partners work with the commercial-grade AISP, which extends it, including the full Pocket architecture and mass-parallel machine learning on CPU.",
};
