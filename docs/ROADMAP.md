# Roadmap

Thermal Brain is developed incrementally. Each milestone builds upon the previous one and results in a mergeable, production-ready state.

---

# M0 – Engineering Foundation

Establish the engineering standards for the project.

## Goals

- Repository structure
- CI/CD
- Ruff
- MyPy
- Pytest
- Pre-Commit
- Semantic Versioning
- GitHub Actions
- Development workflow

Deliverable:

A production-ready engineering environment.

---

# M1 – Core Domain

Build the language of the project.

## Goals

- Domain Model
- Value Objects
- Entities
- Interfaces
- ADRs
- Unit Tests

Deliverable:

A framework independent domain model.

---

# M2 – Observation Engine

Collect and validate observations.

## Goals

- Observation Model
- Sensor Registry
- Data Sources
- Unit Handling
- Validation
- Time Series

Deliverable:

Reliable and validated observations.

---

# M3 – Statistics Engine

Generate useful metrics from observations.

## Goals

- Heating Degree Days
- Burner Runtime
- Burner Starts
- Runtime Distribution
- Daily Energy
- Weekly Trends
- Seasonal Trends

Deliverable:

Meaningful building statistics.

---

# M4 – Building Model

Create the digital twin of the building.

## Goals

- Thermal Capacity
- Heat Loss
- Solar Gain
- Internal Gains
- Wind Influence
- Thermal Charge

Deliverable:

A continuously improving building model.

---

# M5 – Forecast Engine

Predict future building behaviour.

## Goals

- Temperature Forecast
- Heat Loss Forecast
- Remaining Thermal Charge
- Heating Demand Forecast

Deliverable:

Reliable thermal predictions.

---

# M6 – Simulation Engine

Evaluate virtual changes before implementation.

## Goals

Simulate:

- Insulation improvements
- Window replacement
- Heat Pump
- Split Air Conditioner
- Additional PV
- Heating curve changes
- Radiator replacement

Deliverable:

"What if?" analysis for buildings.

---

# M7 – Recommendation Engine

Generate explainable recommendations.

## Goals

- Explainable Recommendations
- Confidence Score
- Recommendation Ranking
- Energy Saving Potential

Deliverable:

Actionable recommendations with explanations.

---

# M8 – Optimization Engine

Perform controlled optimisation.

## Goals

- Heating Curve Optimisation
- Flow Temperature Optimisation
- Heat Source Scheduling
- EMHASS Integration

Deliverable:

Safe optimisation based on measured data.

---

# M9 – Home Assistant Integration

Provide the first official integration.

## Goals

- Config Flow
- Diagnostics
- Services
- Dashboard
- Entity Model

Deliverable:

Official Home Assistant integration.

---

# M10 – Platform Integrations

Support additional automation platforms.

## Goals

- EMS-ESP
- KNX
- MQTT
- Modbus
- Homematic
- openHAB
- ioBroker

Deliverable:

Vendor independent integration layer.

---

# M11 – Learning Engine

Continuously improve the building model.

## Goals

- Parameter Identification
- Self Calibration
- Model Validation
- Confidence Improvements

Deliverable:

Self-learning building intelligence.

---

# M12 – Assistant

Provide explainable insights.

## Goals

- Explain Recommendations
- Explain Energy Consumption
- Explain Optimisation Decisions

Deliverable:

Natural language explanations based on measured data.