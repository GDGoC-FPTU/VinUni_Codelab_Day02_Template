# Phase 4–6 Completion Design

## Scope

- Complete `starter-code/prompt_prototype.py` without changing the existing
  battery/mobile-charger boundary required by the autograder.
- Keep the selected group deep-dive problem as complex customer-support
  complaints; document the prototype scope difference explicitly.
- Update `03-ai-log.md` with the actual prototype test result and Phase 5/6
  reflection.

## Phase 4 prototype

The prototype will:

- Require `[DRAFT_ONLY]` at the beginning of every response.
- Trigger `dispatch_mobile_charger` when battery is below 5%, without
  recommending a station farther than 5 km.
- Use the installed `google-genai` SDK and `gemini-2.5-flash`.
- Return model text and fail explicitly when the API key or SDK request fails.
- Run the existing adversarial tests and print `Passed`/`Failed` markers
  compatible with the autograder.

The prototype remains a technical boundary exercise from the starter code,
not the production architecture selected in the CSKH deep dive.

## Phase 5 and Phase 6

Phase 5 remains `NOT YET` until internal complaint data, baseline timings,
routing labels, and stakeholder approval exist. Phase 6 will record what the
prototype demonstrated, any API/runtime limitation, and the distinction
between the starter-code battery scenario and the selected CSKH use case.
