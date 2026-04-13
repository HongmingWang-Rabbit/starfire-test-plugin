"""DeepAgents adaptor for starfire-test-plugin.

Delegates to the built-in AgentskillsAdaptor, which handles the standard
rules + skills plugin shape across runtimes.
"""
from plugins_registry.builtins import AgentskillsAdaptor as Adaptor

__all__ = ["Adaptor"]
