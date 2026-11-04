"""EN: Deterministic test input for a memory integration case study.
TR: Hafıza entegrasyon vaka çalışması için deterministik test girdisi.
"""

import math
import statistics


def test_population_stddev() -> None:
    """EN: Verify the synthetic result. TR: Sentetik sonucu doğrula."""
    values = [10, 20, 30, 40, 50]
    actual = statistics.pstdev(values)
    expected = math.sqrt(200)
    assert math.isclose(actual, expected, rel_tol=1e-12)
    print(f"Population standard deviation: {actual}")


if __name__ == "__main__":
    test_population_stddev()
