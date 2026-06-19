Bilkul — proper sprint tickets de deta hu, company-style. Tu kal tak karke rakhna, kal isi pe discuss karenge. **PMC-1 zaroor karna** (main task); PMC-2 aur PMC-3 stretch hain agar time bache.

---

**🎟️ PMC-1 — Add conversation memory to the chatbot**
**Type:** Feature | **Priority:** P1 (must-do) | **Estimate:** ~half day

**Context:** Abhi har query stateless hai — bot pichli baat yaad nahi rakhta. "Where is my order?" ke baad "how long will it take?" pucho to context khO jaata hai. Real chatbot ke liye memory chahiye.

**Acceptance Criteria:**
- [ ] `main.py` mein ek `chat_history` list maintain ho, jo poori conversation mein chale
- [ ] `run_agent()` history accept kare aur `MessagesPlaceholder` ke through use kare
- [ ] Har turn ke baad user message + bot reply history mein append ho
- [ ] Ek 3-turn conversation mein follow-up sawaal sahi context use kare
- [ ] `exit` abhi bhi clean kaam kare

**Technical notes:** Template mein `MessagesPlaceholder("chat_history")` system ke baad daal; `run_agent(agent_name, query, history)` signature; invoke mein history pass kar; reply ke baad `HumanMessage` + `AIMessage` append kar. (Level 3 wala pattern.)

**Definition of Done:** 3-turn baat-cheet ka screenshot jisme bot pichli baat yaad rakhta dikhe.

---

**🎟️ PMC-2 — Make routing reliable with structured output**
**Type:** Enhancement | **Priority:** P2 (stretch) | **Estimate:** ~1-2 hrs

**Context:** Router abhi plain text deta hai jise `.strip().upper()` se saaf karte hain — fragile. Pydantic schema se reliable, typed output milega.

**Acceptance Criteria:**
- [ ] Ek `RouteDecision` Pydantic model bane (field: `agent`, value 4 categories mein se ek)
- [ ] Router `model.with_structured_output(RouteDecision)` use kare
- [ ] `route()` ek typed object/clean category return kare, manual string-cleaning ke bina
- [ ] 4 test queries sahi route hon

**Technical notes:** Level 6 wala `with_structured_output`. Categories ke liye Enum use kar sakta hai (extra clean).

**Definition of Done:** Router typed result deta dikhe, test pass.

---

**🎟️ PMC-3 — Update README & roadmap after memory ships**
**Type:** Task | **Priority:** P3 (quick) | **Estimate:** ~30 min

**Context:** Docs hamesha current + honest rakhne hain.

**Acceptance Criteria:**
- [ ] Memory ko Roadmap se nikaal ke main features/flow mein le aao, checkbox `[x]`
- [ ] "How it works" mermaid diagram mein memory ka step add ho
- [ ] Commit message clean ho (jaise `feat: add conversation memory`)

**Definition of Done:** README new capability reflect kare, push ho jaaye.

---

**Sprint goal:** PMC-1 complete (memory live), baaki do agar time mile.

Kal jab discuss karenge, jahan atke wahan se uthaa lenge. Ab SattvikBhojanam pe focus kar — wahi asli priority hai. All the best. 🙏