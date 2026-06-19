# Sprint Tickets — PromptManagement-Chatbot

**Sprint goal:** Ship PMC-1 (conversation memory). PMC-2 and PMC-3 are stretch goals if time allows.

---

## PMC-1 — Add conversation memory to the chatbot

| | |
|---|---|
| **Type** | Feature |
| **Priority** | P1 (must-do) |
| **Estimate** | ~half day |
| **Status** | ☐ To Do |

**Context**
Right now every query is stateless — the bot doesn't remember earlier turns. After "Where is my order?", a follow-up like "how long will it take?" loses all context. A real chatbot needs memory across turns.

**Acceptance Criteria**
- [ ] `main.py` maintains a `chat_history` list that persists across the whole conversation
- [ ] `run_agent()` accepts the history and uses it via `MessagesPlaceholder`
- [ ] After each turn, the user message + bot reply are appended to the history
- [ ] In a 3-turn conversation, a follow-up question correctly uses prior context
- [ ] `exit` still works cleanly

**Technical notes**
- Add `MessagesPlaceholder("chat_history")` after the system message in the template
- Change the signature to `run_agent(agent_name, query, history)`
- Pass the history into `.invoke(...)`
- After getting the reply, append `HumanMessage(content=query)` and `AIMessage(content=reply)` to the history
- (This is the Level 3 pattern — same as the MessagesPlaceholder practice.)

**Definition of Done**
A screenshot of a 3-turn conversation where the bot clearly remembers earlier context.

---

## PMC-2 — Make routing reliable with structured output

| | |
|---|---|
| **Type** | Enhancement |
| **Priority** | P2 (stretch) |
| **Estimate** | ~1-2 hrs |
| **Status** | ☐ To Do |

**Context**
The router currently returns plain text that we clean with `.strip().upper()` — fragile. A Pydantic schema gives a reliable, typed output instead.

**Acceptance Criteria**
- [ ] A `RouteDecision` Pydantic model exists (field `agent`, value is one of the 4 categories)
- [ ] The router uses `model.with_structured_output(RouteDecision)`
- [ ] `route()` returns a clean typed result without manual string-cleaning
- [ ] All 4 test queries route correctly

**Technical notes**
- Level 6 pattern (`with_structured_output`)
- Consider an `Enum` for the 4 categories for extra cleanliness

**Definition of Done**
Router returns a typed result; routing tests pass.

---

## PMC-3 — Update README & roadmap after memory ships

| | |
|---|---|
| **Type** | Task |
| **Priority** | P3 (quick) |
| **Estimate** | ~30 min |
| **Status** | ☐ To Do |

**Context**
Keep the docs current and honest as features land.

**Acceptance Criteria**
- [ ] Move "memory" from Roadmap into the main features/flow; tick the checkbox `[x]`
- [ ] Add the memory step to the "How it works" mermaid diagram
- [ ] Use a clean commit message (e.g. `feat: add conversation memory`)

**Definition of Done**
README reflects the new capability and is pushed.

---

### Notes for tomorrow's discussion
- Wherever I get stuck, note the error/screenshot — we'll pick up from there.
- Focus is PMC-1; the rest are bonus.
