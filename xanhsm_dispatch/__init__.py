"""Xanh SM low-battery dispatch co-pilot.

The package deliberately keeps deterministic safety rules separate from the
language model.  The public helpers are small so they can also be used by the
lab's automated tests.
"""

from .rule_engine import DispatchRuleEngine, evaluate_offline

__all__ = ["DispatchRuleEngine", "evaluate_offline"]

