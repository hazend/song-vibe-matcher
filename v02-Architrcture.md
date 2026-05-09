
# Architecture Overview in this v0.2 for the project

```
┌─────────────────────────────────────────────────────────────┐
│                        Browser                              │
│  ┌──────────────────────────────────────────────────────┐   │
│  │          Frontend  (HTML + CSS + Vanilla JS)         │   │
│  │  • Song name input field                             │   │
│  │  • Animated vibe result card (mood, keywords, score) │   │
│  │  • [Placeholder] AI image output area                │   │
│  └────────────────────────┬─────────────────────────────┘   │
└───────────────────────────│─────────────────────────────────┘
                            │ HTTP (fetch)
                            ▼
┌─────────────────────────────────────────────────────────────┐
│               FastAPI Gateway  (backend/)                   │
│  • POST /analyze  → orchestrates DB + ML service            │
│  • GET  /songs    → lists all songs in DB                   │
│  • POST /songs    → adds a new song to DB  (dev helper)     │
│  • Static file serving for the frontend                     │
└────────────────┬───────────────────────────┬────────────────┘
                 │                           │
          reads / writes               calls internally
                 │                           │
                 ▼                           ▼
┌───────────────────────┐     ┌──────────────────────────────┐
│  Local JSON Database  │     │      ML Service  (ml/)       │
│  data/Songs.json      │     │  • VADER sentiment scores    │
│  (existing schema +   │     │  • TextBlob subjectivity     │
│   vibe cache field)   │     │  • Keyword / theme extract   │
└───────────────────────┘     │  • Vibe label mapping        │
                              │  • [Stub] GenAI image gen    │
                              └──────────────────────────────┘
```

---
