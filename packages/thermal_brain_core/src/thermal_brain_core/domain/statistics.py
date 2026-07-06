from collections.abc import Iterable
from math import sqrt
from statistics import mean, median

from pydantic import BaseModel, ConfigDict


class DescriptiveStatistics(BaseModel):
    model_config = ConfigDict(frozen=True)

    count: int
    minimum: float | None = None
    maximum: float | None = None
    mean: float | None = None
    median: float | None = None
    variance: float | None = None
    standard_deviation: float | None = None


def descriptive_statistics(values: Iterable[float]) -> DescriptiveStatistics:
    values_list = list(values)
    count = len(values_list)
    if count == 0:
        return DescriptiveStatistics(count=0)

    minimum = min(values_list)
    maximum = max(values_list)
    average = mean(values_list)
    middle = median(values_list)
    variance = sum((value - average) ** 2 for value in values_list) / count

    return DescriptiveStatistics(
        count=count,
        minimum=minimum,
        maximum=maximum,
        mean=average,
        median=middle,
        variance=variance,
        standard_deviation=sqrt(variance),
    )
