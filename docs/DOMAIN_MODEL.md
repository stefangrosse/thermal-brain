# Domain Model

## Building

A physical structure consisting of one or more thermal zones.

## Zone

A thermally connected space with measurable properties.

## Heat Source

Anything that injects thermal energy into a building.

Examples:
- Oil boiler
- Gas boiler
- Heat pump
- Split AC
- Wood stove
- District heating

## Heat Consumer

A system distributing heat.

Examples:
- Radiators
- Floor heating
- Fan coils

## Thermal State

Current thermal condition of the building.

## Observation

A measured or calculated fact about the building at a specific point in time.
Observations always reference a registered sensor, a data source, a quantity, and
a typed value object such as `Temperature`, `Power`, `Energy`, or `Percentage`.

Observation timestamps are timezone-aware to keep data from different platforms
comparable.

## Data Source

A framework-independent description of where observations come from.

Examples:
- Home Assistant sensor import
- Weather service
- Calculated metric
- Manual reading

Data source readers expose observations through a protocol so integrations can
provide data without moving business logic into the integration layer.

## Sensor Registry

The sensor registry stores known data sources and sensors. It validates that
incoming observations match the registered sensor quantity, unit, and source.

## Time Series

Observation time series are ordered immutable collections of observations.
They support filtering by time range and sensor without depending on a storage
backend.

## Statistics

Descriptive statistics summarize numeric observation series using count,
minimum, maximum, mean, median, variance, and standard deviation.
The first statistics API is exposed on `ObservationTimeSeries`.

## Thermal Charge (experimental)

A normalized representation of the amount of usable thermal energy currently stored in the building.

## Recommendation

An explainable proposal generated from measured data.
Recommendations never directly modify the heating system.
