# Architecture

```text
Data Sources
      │
      ▼
 Data Collector
      │
      ▼
 Statistics Engine
      │
      ▼
 Thermal Model
      │
      ▼
 Prediction Engine
      │
      ▼
 Recommendation Engine
      │
      ▼
 Home Assistant
```

The Home Assistant integration is only one consumer of the engine.
The core domain model remains independent from any vendor or heating technology.
