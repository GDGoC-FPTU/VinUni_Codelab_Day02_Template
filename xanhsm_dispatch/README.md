# Terminal prototype — Xanh SM battery dispatch

The prototype is intentionally hybrid:

- `rule_engine.py` owns every safety decision and always fails closed.
- `llm.py` optionally asks Gemini 2.5 Flash to improve only the Vietnamese draft wording.
- `data_loader.py` reads `data/vehicle_specs.json` and `data/charging_stations.json` (with legacy filename aliases).
- `chat.py` provides the stateful terminal conversation.

Run without an API key for deterministic testing:

```bash
python3 chat_terminal.py --offline
```

Run with Gemini:

```bash
export GEMINI_API_KEY="your-key"
python3 chat_terminal.py
```

Use `--data-dir path/to/data` to override the default `data/` directory. In the
chat, `/help`, `/data`, `/reset`, and `/quit` are available. All JSON responses
remain `DRAFT_ONLY`, set `auto_send` to `false`, and require human approval.

The coordinates and live station availability in this lab are sample inputs,
not a connection to Xanh SM/V-GREEN production systems. A dispatcher must check
the official operations dashboard before sending any instruction.
